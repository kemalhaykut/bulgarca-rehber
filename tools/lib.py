# -*- coding: utf-8 -*-
"""Bulgarca Rehber içerik yardımcıları: sözlük, çekim üreticileri, okunuş."""
import re

ACC = '́'
CYR = 'а-яА-ЯѝЍ'
WORD_RE = re.compile(r'[а-яА-ЯѝЍ́]+')

def plain(s): return s.replace(ACC, '')

# ---------------------------------------------------------------- sözlük
# DICT: yüzey biçimi (küçük harf, vurgusuz) -> list of entries
# entry: {f: vurgulu biçim, tr, g: dilbilgisi, n: not, l: kök (vurgulu)}
DICT = {}
LEMMAS = []

def _add(form, tr, g, n='', lemma=None):
    key = plain(form).lower()
    e = {'f': form, 'tr': tr, 'g': g}
    if n: e['n'] = n
    if lemma and plain(lemma) != plain(form): e['l'] = lemma
    lst = DICT.setdefault(key, [])
    # aynı biçim aynı anlamla iki kez eklenmesin
    for x in lst:
        if x['tr'] == tr and x['g'] == g: return
    lst.append(e)

def W(form, tr, g='', n='', forms=None):
    """Tek kelime + isteğe bağlı ek biçimler: forms='biçim:açıklama;biçim:açıklama'"""
    _add(form, tr, g, n)
    LEMMAS.append(form)
    if forms:
        for part in forms.split(';'):
            part = part.strip()
            if not part: continue
            f, _, lab = part.partition(':')
            _add(f.strip(), tr, (lab.strip() or g), lemma=form)

def acc1(form):
    """Tek heceli kelimeye vurgu işareti ekler (türetilen biçimler için)."""
    if not form or ACC in form: return form
    idx = [i for i, c in enumerate(form) if c.lower() in VOW]
    if len(idx) != 1: return form
    i = idx[0]
    return form[:i + 1] + ACC + form[i + 1:]

def N(form, tr, gender, pl=None, n='', defs=None, count=None, extra=''):
    """İsim. gender: m/f/n. pl: çoğul (vurgulu). defs: belirli tekil biçimleri elle."""
    form = acc1(form); pl = acc1(pl) if pl else pl
    gname = {'m': 'eril isim', 'f': 'dişil isim', 'n': 'nötr isim', 'p': 'çoğul isim'}[gender]
    info = gname + (f' · çoğ. {plain(pl)}' if pl else '')
    _add(form, tr, info, n)
    LEMMAS.append(form)
    p = plain(form)
    if defs is None:
        if gender == 'm':
            if p.endswith('й'):
                defs = [form[:-1] + 'ят', form[:-1] + 'я']
            elif p.endswith('тел') or p.endswith('ар') and len(p) > 3 and p not in ('пазар', 'базар', 'шкаф') or p in ('ден', 'кон', 'път', 'сън'):
                defs = [form + 'ят', form + 'я']
            elif p.endswith('а') or p.endswith('я'):
                defs = [form + 'та']
            elif p.endswith('о') or p.endswith('е'):
                defs = [form + 'то']
            else:
                defs = [form + 'ът', form + 'а']
        elif gender == 'f':
            defs = [form + 'та']
        elif gender == 'n':
            defs = [form + 'то']
        else:
            defs = []
    labels = ['belirli (özne)', 'belirli (özne değil)'] if len(defs) == 2 else ['belirli']
    for d, lab in zip(defs, labels):
        _add(d, tr, f'{gname} · {lab}', lemma=form)
    if pl:
        _add(pl, tr + ' (çoğul)', f'{gname} · çoğul', lemma=form)
        pp = plain(pl)
        art = 'та' if pp.endswith('а') or pp.endswith('я') else 'те'
        _add(pl + art, tr + ' (çoğul)', f'{gname} · çoğul, belirli', lemma=form)
    if count:
        _add(count, tr, f'{gname} · sayı sonrası biçim (два {plain(count)})', lemma=form)
    for part in extra.split(';'):
        if part.strip():
            f, _, lab = part.partition(':')
            _add(f.strip(), tr, f'{gname} · {lab.strip()}', lemma=form)

def A(m, tr, f=None, n_=None, pl=None, note=''):
    """Sıfat: eril, dişil, nötr, çoğul + belirli biçimler üretilir."""
    m = acc1(m)
    f = f or m + 'а'; n_ = n_ or m + 'о'; pl = pl or m + 'и'
    g = f'sıfat · {plain(m)} / {plain(f)} / {plain(n_)} / {plain(pl)}'
    _add(m, tr, g + ' · eril', note); LEMMAS.append(m)
    _add(f, tr, g + ' · dişil', lemma=m)
    _add(n_, tr, g + ' · nötr', lemma=m)
    _add(pl, tr, g + ' · çoğul', lemma=m)
    _add(pl + 'ят', tr, 'sıfat · eril, belirli (özne)', lemma=m)
    _add(pl + 'я', tr, 'sıfat · eril, belirli', lemma=m)
    _add(f + 'та', tr, 'sıfat · dişil, belirli', lemma=m)
    _add(n_ + 'то', tr, 'sıfat · nötr, belirli', lemma=m)
    _add(pl + 'те', tr, 'sıfat · çoğul, belirli', lemma=m)

PERS = ['ben', 'sen', 'o', 'biz', 'siz', 'onlar']

def _stress_end(form):
    """Vurgu son harfte mi?"""
    return form.endswith(ACC)

def V(first, tr, grp, n='', stem=None, forms=None, aspect=''):
    """Şimdiki zaman çekimi üretir.
    grp: 'e' (чета, четеш), 'i' (говоря, говориш), 'a' (имам, имаш)."""
    p = plain(first)
    asp = {'nsv': ' · süreç (несвършен)', 'sv': ' · tek sefer/tamamlanan (свършен)', '': ''}[aspect]
    g = {'e': 'fiil · е-grubu', 'i': 'fiil · и-grubu', 'a': 'fiil · а/я-grubu (-м)'}[grp] + asp
    ex = forms or {}
    if grp == 'a':
        st = first[:-1]  # и́ма
        res = [first, st + 'ш', st, st + 'ме', st + 'те', st + 'т']
    else:
        end_stress = first.endswith('а' + ACC) or first.endswith('я' + ACC)
        base = first[:-2] if end_stress else first[:-1]  # без последната гласна
        if stem: base = stem
        last = plain(first)[-1]  # а / я
        v = 'е' if grp == 'e' else 'и'
        a = ACC if end_stress else ''
        res = [first, base + v + a + 'ш', base + v + a, base + v + a + 'м', base + v + a + 'те',
               base + last + a + 'т']
    for i, fm in enumerate(res):
        fm = ex.get(i, fm)
        if i == 0:
            _add(fm, tr, g + ' · ben (sözlük biçimi)', n)
        else:
            _add(fm, tr, f'{g} · {PERS[i]}', lemma=first)
    LEMMAS.append(first)

# ---------------------------------------------------------------- okunuş
TL = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'y',
      'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
      'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ç', 'ш': 'ş', 'щ': 'şt', 'ъ': 'ı', 'ь': 'y', 'ю': 'yu', 'я': 'ya', 'ѝ': 'i'}
VOW = set('аеиоуъюяѝ')

def translit_word(accented):
    """Vurgulu Kiril kelime → Türkçe harflerle okunuş, vurgulu hece BÜYÜK."""
    w = accented.lower()
    letters = []  # (cyr, stressed)
    for ch in w:
        if ch == ACC and letters:
            letters[-1] = (letters[-1][0], True)
        else:
            letters.append((ch, False))
    vowels = [i for i, (c, _) in enumerate(letters) if c in VOW]
    si = next((i for i, (c, s) in enumerate(letters) if s), None)
    out = [TL.get(c, c) for c, _ in letters]
    if si is None or len(vowels) < 2:
        return ''.join(out)
    # hece sınırları
    vi = vowels.index(si)
    start = si
    prev_v = vowels[vi - 1] if vi > 0 else -1
    cons_before = si - prev_v - 1
    if cons_before >= 1: start = si - 1
    if vi == 0: start = 0
    nxt = vowels[vi + 1] if vi + 1 < len(vowels) else None
    if nxt is None:
        end = len(letters)
    else:
        between = nxt - si - 1
        end = si + 1 + max(0, between - 1)
    up = ''.join(out[start:end]).replace('i', 'İ').replace('ı', 'I').upper()
    return ''.join(out[:start]) + up + ''.join(out[end:])

# ---------------------------------------------------------------- içerik yapıları
def T(title, body, kind=''):
    """Metin bölümü. kind: '' | 'tr' (Türkçe karşılaştırma) | 'warn' | 'tip' | 'key'"""
    return {'t': 'text', 'title': title, 'body': body.strip(), 'kind': kind}

def TB(title, headers, rows, note=''):
    return {'t': 'table', 'title': title, 'headers': headers, 'rows': rows, 'note': note}

def X(title, items):
    return {'t': 'ex', 'title': title, 'items': [{'bg': i[0], 'tr': i[1], **({'n': i[2]} if len(i) > 2 else {})} for i in items]}

def R(title, sents, notes, title_tr=''):
    return {'title': title, 'title_tr': title_tr, 'sents': [{'bg': b, 'tr': t} for b, t in sents], 'notes': notes}

def QC(q, opts, tr='', why=''):
    """Boşluk doldurma: q içinde ___ ; opts[0] doğru."""
    assert '___' in q, q
    return {'k': 'fill', 'q': q, 'o': opts, 'tr': tr, 'why': why}

def QT(tr, opts, why=''):
    """Türkçe cümlenin doğru Bulgarcasını seç; opts[0] doğru."""
    return {'k': 'pick', 'q': tr, 'o': opts, 'why': why}

def QO(tr, bg, extra=(), why=''):
    """Kelimeleri sırala."""
    return {'k': 'order', 'q': tr, 'a': bg, 'x': list(extra), 'why': why}

def M(id, level, ref, title, title_bg, goal, blocks, reading, quiz):
    return {'id': id, 'level': level, 'ref': ref, 'title': title, 'title_bg': title_bg, 'goal': goal,
            'blocks': blocks, 'reading': reading, 'quiz': quiz}
