# -*- coding: utf-8 -*-
"""Bulgarca Rehber: içerik + sözlük → web/data.js"""
import json, os, re, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
import lib
from lib import DICT, plain, translit_word, VOW, ACC
import dict_data  # noqa: sözlüğü doldurur
from mod_a1a import M1, M2, M3, M4
from mod_a1b import M5, M6, M7
from mod_a2a import M8, M9, M10, M11
from mod_a2b import M12, M13, M14

MODS = [M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14]
IGNORE = set('ат ите иш еш ът ят та то ото ят ем им ме те ове ета ци ия ка ко ки ма ше ще'.split()) - {'те'}
TOK = re.compile(r'(?<![-\w])[а-яА-ЯѝЍ]+')
LATIN_IN_BG = re.compile(r'[A-Za-z]')

def texts(m):
    """(metin, bulgarca_mi) çiftleri"""
    yield m['title_bg'], True
    for b in m['blocks']:
        yield b['title'], False
        if b['t'] == 'text': yield b['body'], False
        if b['t'] == 'table':
            for h in b['headers']: yield h, False
            for r in b['rows']:
                for c in r: yield c, False
            yield b['note'], False
        if b['t'] == 'ex':
            for it in b['items']: yield it['bg'], True
    r = m['reading']
    yield r['title'], True
    for s in r['sents']: yield s['bg'], True
    for n in r['notes']: yield n, False
    for q in m['quiz']:
        # Alıştırma seçenekleri bilerek etkileşimsiz (cevabı ele vermesin);
        # sadece doğru cevap sözlükte olmalı (sonuç ekranında gösterilir).
        if q['k'] == 'fill':
            yield re.sub(r'\w*___\w*', ' ', q['q']), True
            yield q['q'].replace('___', q['o'][0]), True
        elif q['k'] == 'pick':
            yield q['o'][0], True
        else:
            yield q['a'], True
        if q.get('why'): yield q['why'], False

def check():
    missing = collections.Counter(); where = {}
    for m in MODS:
        for t, isbg in texts(m):
            t = t.replace('**', '')
            if isbg and LATIN_IN_BG.search(t): print('!! Latin harf Bulgarca metinde:', m['id'], t)
            for w in TOK.findall(t):
                k = w.lower()
                if not isbg and (k in IGNORE or len(k) < 2): continue
                if k not in DICT:
                    missing[k] += 1; where.setdefault(k, m['id'] + ': ' + t[:50])
    nostress = [e['f'] for v in DICT.values() for e in v
                if ACC not in e['f'] and sum(c in VOW for c in plain(e['f']).lower()) > 1 and not e.get('u')]
    return missing, where, nostress

def pron(bg):
    """Cümlenin okunuşu: sözlükteki vurgulu biçimlerle."""
    out = []
    pos = 0
    for mt in re.finditer(r'[а-яА-ЯѝЍ]+', bg):
        out.append(bg[pos:mt.start()])
        w = mt.group(0); e = DICT.get(w.lower())
        acc = e[0]['f'] if e else w
        tl = translit_word(acc.lower())
        out.append(tl)
        pos = mt.end()
    out.append(bg[pos:])
    return ''.join(out)

if __name__ == '__main__':
    missing, where, nostress = check()
    if missing:
        print(f'EKSİK {len(missing)} kelime:')
        for k, c in sorted(missing.items(), key=lambda x: (where[x[0]], x[0])):
            print(f'  {k:18} ×{c:<3} {where[k]}')
    if nostress:
        print('VURGUSUZ çok heceli:', ' '.join(sorted(set(nostress))))
    if missing or nostress:
        if '--force' not in sys.argv: sys.exit(1)
    # okunuşları ekle
    for m in MODS:
        for b in m['blocks']:
            if b['t'] == 'ex':
                for it in b['items']: it['p'] = pron(it['bg'])
        for s in m['reading']['sents']: s['p'] = pron(s['bg'])
    def mono(f):
        return f.replace(ACC, '') if sum(c in VOW for c in plain(f).lower()) <= 1 else f
    dic = {k: [{**e, 'f': mono(e['f']), **({'l': mono(e['l'])} if 'l' in e else {}),
                'p': translit_word(e['f'].lower())} for e in v] for k, v in DICT.items()}
    data = {'modules': MODS, 'dict': dic}
    out = os.path.join(os.path.dirname(__file__), '..', 'site', 'data.js')
    js = 'window.REHBER_DATA = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n'
    open(out, 'w', encoding='utf-8').write(js)
    print('OK', len(MODS), 'ders,', len(DICT), 'sözlük biçimi,', len(lib.LEMMAS), 'kök →', os.path.getsize(out)//1024, 'KB')
