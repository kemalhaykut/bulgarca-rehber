# -*- coding: utf-8 -*-
from lib import T, TB, X, R, QC, QT, QO, M

# =====================================================================
M5 = M('a1-05', 'A1', '5. ders', 'Buluşma: fiil grupları ve „два стола“', 'Среща',
  'Üç fiil grubunu, ям ve пия gibi önemli fiilleri, sayılardan sonraki özel biçimi ve ще ile geleceği öğreneceksin.',
  [
    T('Fiiller üç gruba ayrılır', """
Bulgarca fiiller "sen" hâlindeki sese göre üç aileye ayrılır. Türkçedeki ünlü uyumu gibi düşün: ek aynı görevi yapar, sadece içindeki ünlü değişir.

• **а/я-grubu (-м):** чака**м**, чака**ш** — en kolayı
• **е-grubu:** пи**я**, пи**еш**
• **и-grubu:** говор**я**, говор**иш**

İpucu: yeni bir fiili **iki hâliyle** öğren: ben + sen (пия – пиеш, говоря – говориш).
""", 'tr'),
    TB('Üç grup yan yana', ['Kişi', 'чакам (beklemek)', 'пия (içmek)', 'говоря (konuşmak)'], [
        ['аз', 'чакам', 'пия', 'говоря'], ['ти', 'чакаш', 'пиеш', 'говориш'], ['той/тя', 'чака', 'пие', 'говори'],
        ['ние', 'чакаме', 'пием', 'говорим'], ['вие', 'чакате', 'пиете', 'говорите'], ['те', 'чакат', 'пият', 'говорят']],
        '"Ben" ve "onlar" aynı harfle biter: пия → пият, говоря → говорят.'),
    T('Bir zaman, iki anlam', """
Bulgarca şimdiki zaman hem **-yor** hem **-r** demektir:
**Пия** кафе. — Kahve içiyorum. / Kahve içerim.
Anlamı bağlam belirler: **Сега** пия кафе (şimdi) · **Всяка сутрин** пия кафе (her sabah).
"""),
    TB('ям ve мисля', ['Kişi', 'ям (yemek)', 'мисля (düşünmek)'], [
        ['аз', 'ям', 'мисля'], ['ти', 'ядеш', 'мислиш'], ['той/тя', 'яде', 'мисли'],
        ['ние', 'ядем', 'мислим'], ['вие', 'ядете', 'мислите'], ['те', 'ядат', 'мислят']],
        'ям düzensizdir: -м ile biter ama ядеш, яде diye devam eder.'),
    X('Fiillerle örnekler', [
        ('Чакам те пред киното.', 'Seni sinemanın önünde bekliyorum.'),
        ('Плащам аз!', 'Ben ödüyorum!'),
        ('Какво ядеш за закуска?', 'Kahvaltıda ne yersin?'),
        ('Мисля, че е късно.', 'Bence geç oldu.'),
        ('Говориш ли английски?', 'İngilizce konuşuyor musun?'),
        ('Бързам, извинявай!', 'Acelem var, kusura bakma!'),
        ('Той пита, а тя отговаря.', 'O soruyor, kadın cevap veriyor.'),
    ]),
    T('Sayıdan sonra eril isim: два стола', """
Türkçede sayıdan sonra tekil kullanırız: iki sandalye. Bulgarcada sayıdan sonra **çoğul** gerekir.
**Eril** isimler (insan değilse) ise özel bir **sayma biçimi** alır: **-а / -я**

стол → столове (çoğul) → **два стола**
билет → билети → **три билета**
час → часове → **пет часа**

Dişil ve nötrde normal çoğul: две кафета, три чаши.
**два** eril ile, **две** dişil/nötr ile: два билета · две кафета
""", 'tr'),
    X('Sayılarla', [
        ('Два билета, моля.', 'İki bilet, lütfen.'),
        ('Три кафета и две води.', 'Üç kahve ve iki su.'),
        ('Чакам те от два часа!', 'İki saattir seni bekliyorum!'),
        ('Колко струва? — Пет евро.', 'Ne kadar? — Beş euro.'),
    ]),
    T('ще ile gelecek — ilk bakış', """
Geleceği söylemek çok kolay: fiilin önüne **ще** koy. ще hiç değişmez.
Утре **ще** чакам. — Yarın bekleyeceğim. · **Ще** пием кафе. — Kahve içeceğiz.
(Ayrıntısı 12. derste.)
"""),
  ],
  R('Среща в центъра', [
      ('Иван чака Ани пред театъра.', "İvan, Ani'yi tiyatronun önünde bekliyor."),
      ('Тя закъснява.', 'Ani gecikiyor.'),
      ('Иван пише съобщение: „Къде си?“', 'İvan mesaj yazıyor: "Neredesin?"'),
      ('Ани отговаря: „Идвам! Пет минути!“', 'Ani cevap veriyor: "Geliyorum! Beş dakika!"'),
      ('След десет минути тя идва.', 'On dakika sonra geliyor.'),
      ('— Извинявай! Идвам направо от работа.', '— Kusura bakma! Doğrudan işten geliyorum.'),
      ('— Няма проблем. Искаш ли кафе?', '— Sorun yok. Kahve ister misin?'),
      ('Те вземат две кафета и два сандвича.', 'İki kahve ve iki sandviç alıyorlar.'),
      ('Иван плаща. Ани казва: „Следващия път плащам аз!“', 'İvan ödüyor. Ani diyor ki: "Gelecek sefer ben ödüyorum!"'),
  ], [
      '**два сандвича** — eril isim + sayı → sayma biçimi -а.',
      '**две кафета** — nötr isim + sayı → normal çoğul.',
      '**плащам аз** — vurgu için zamir sona alınabilir: "BEN ödüyorum".',
  ], 'Şehir merkezinde buluşma'),
  [
    QC('Ти какво ___?', ['пиеш', 'пием', 'пиете'], 'Sen ne içiyorsun?', 'е-grubu, ти → -еш'),
    QC('Те ___ английски.', ['говорят', 'говорат', 'говори'], 'Onlar İngilizce konuşuyor.', 'говоря → говорят'),
    QC('Ние ___ хляб.', ['ядем', 'ямаме', 'яме'], 'Ekmek yiyoruz.', 'ям düzensiz: ядем'),
    QC('Два ___, моля.', ['билета', 'билети', 'билет'], 'İki bilet, lütfen.', 'eril + sayı → -а'),
    QC('___ кафета, моля.', ['Две', 'Два', 'Двама'], 'İki kahve, lütfen.', 'nötr → две'),
    QC('Утре ___ чакам.', ['ще', 'съм', 'да'], 'Yarın bekleyeceğim.', 'gelecek → ще'),
    QT('Ben ödüyorum!', ['Плащам аз!', 'Плаща аз!', 'Аз плащаш!'], ''),
    QO('Kahvaltıda ne yersin?', 'Какво ядеш за закуска?', ['ям']),
  ])

# =====================================================================
M6 = M('a1-06', 'A1', '6. ders', 'Saat kaç? — zaman, günler, е/и fiilleri', 'Колко е часът?',
  'Saati, günleri, ayları, sıra sayılarını ve чета, пиша, работя, уча gibi fiilleri öğreneceksin.',
  [
    TB('е-grubu ve и-grubu', ['Kişi', 'чета (okumak)', 'пиша (yazmak)', 'работя (çalışmak)', 'уча (öğrenmek)'], [
        ['аз', 'чета', 'пиша', 'работя', 'уча'], ['ти', 'четеш', 'пишеш', 'работиш', 'учиш'],
        ['той/тя', 'чете', 'пише', 'работи', 'учи'], ['ние', 'четем', 'пишем', 'работим', 'учим'],
        ['вие', 'четете', 'пишете', 'работите', 'учите'], ['те', 'четат', 'пишат', 'работят', 'учат']],
        'ж, ч, ш\'den sonra hep -а / -ат: уча → учат, пиша → пишат.'),
    T('-м fiilleri: hareket', """
**идвам** (gelmek), **отивам** (gitmek), **ставам** (kalkmak), **забравям** (unutmak), **закъснявам** (gecikmek)
Отивам на работа. — İşe gidiyorum. · Идваш ли? — Geliyor musun?
"""),
    T('Колко е часът? — Saat kaç?', """
**Часът е три.** — Saat üç.
**Три и половина.** — Üç buçuk. · **Пет и десет.** — Beşi on geçiyor. · **Пет без десет.** — Beşe on var.
**В колко часа?** — Saat kaçta? → **В осем часа.** — Saat sekizde.
**От девет до пет** — dokuzdan beşe kadar.
"""),
    TB('Günler', ['Bulgarca', 'Türkçe', 'Bulgarca', 'Türkçe'], [
        ['понеделник', 'pazartesi', 'петък', 'cuma'], ['вторник', 'salı', 'събота', 'cumartesi'],
        ['сряда', 'çarşamba', 'неделя', 'pazar'], ['четвъртък', 'perşembe', '', '']],
        '"Pazartesi günü" = в понеделник · "salı günü" = във вторник (в → във)'),
    TB('Aylar', ['', '', '', ''], [
        ['януари', 'февруари', 'март', 'април'], ['май', 'юни', 'юли', 'август'],
        ['септември', 'октомври', 'ноември', 'декември']],
        '"Martta" = през март (ya da: в март) · "1 Mart\'ta" = на първи март'),
    T('Zaman zarfları', """
**днес** bugün · **утре** yarın · **вдругиден** öbür gün · **вчера** dün · **завчера** evvelsi gün
**сега** şimdi · **винаги** her zaman · **често** sık sık · **понякога** bazen · **никога не** asla · **обикновено** genellikle
"""),
    TB('Sıra sayıları', ['', 'eril', 'dişil', 'nötr'], [
        ['1.', 'първи', 'първа', 'първо'], ['2.', 'втори', 'втора', 'второ'], ['3.', 'трети', 'трета', 'трето'],
        ['4.', 'четвърти', 'четвърта', 'четвърто'], ['5.', 'пети', 'пета', 'пето']],
        'Tarih: днес е двайсет и трети ноември (bugün 23 Kasım) — sıra sayısıyla söylenir.'),
    X('Örnekler', [
        ('Колко е часът? — Часът е десет и половина.', 'Saat kaç? — On buçuk.'),
        ('Работя от девет до пет.', 'Dokuzdan beşe kadar çalışırım.'),
        ('В събота не работим.', 'Cumartesi çalışmıyoruz.'),
        ('Днес е петък, четиринайсети юни.', 'Bugün cuma, 14 Haziran.'),
        ('Понякога чета вестник.', 'Bazen gazete okurum.'),
        ('Тя учи български всеки ден.', 'O her gün Bulgarca çalışıyor.'),
    ]),
    T('съм: dün ve yarın (o için)', """
Днес **е** понеделник. — Bugün pazartesi.
Вчера **беше** неделя. — Dün pazardı.
Утре **ще бъде** вторник. — Yarın salı olacak.
"""),
  ],
  R('Един обикновен ден', [
      ('Петър работи в банка.', 'Petır bir bankada çalışıyor.'),
      ('Той става в седем часа.', 'Saat yedide kalkıyor.'),
      ('Закусва и чете новините.', 'Kahvaltı yapıyor ve haberleri okuyor.'),
      ('В осем и половина отива на работа.', 'Sekiz buçukta işe gidiyor.'),
      ('Работи от девет до пет.', 'Dokuzdan beşe kadar çalışıyor.'),
      ('Вечер учи турски, защото има приятели от Истанбул.', "Akşamları Türkçe çalışıyor, çünkü İstanbul'dan arkadaşları var."),
      ('Понякога пише имейли на турски.', 'Bazen Türkçe e-posta yazıyor.'),
      ('В събота и неделя не работи.', 'Cumartesi ve pazar çalışmıyor.'),
      ('Днес е петък и Петър е много доволен!', 'Bugün cuma ve Petır çok memnun!'),
  ], [
      '**в седем часа** — "saat yedide": в + sayı + часа.',
      '**от девет до пет** — "dokuzdan beşe".',
      '**Вечер** — "akşamları": gün bölümü zarf gibi kullanılır.',
      '**на турски** — "Türkçe olarak": на + dil adı.',
  ], 'Sıradan bir gün'),
  [
    QC('Аз ___ книга.', ['чета', 'чете', 'четеш'], 'Kitap okuyorum.', 'аз → чета'),
    QC('Ти къде ___?', ['работиш', 'работеш', 'работя'], 'Nerede çalışıyorsun?', 'и-grubu → -иш'),
    QC('Студентите ___ много.', ['учат', 'учят', 'учи'], 'Öğrenciler çok çalışıyor.', 'ч\'den sonra -ат'),
    QC('Часът е три и ___.', ['половина', 'половин', 'без'], 'Saat üç buçuk.', 'buçuk = и половина'),
    QC('Ще се видим ___ вторник.', ['във', 'в', 'на'], 'Salı görüşürüz.', 'в → във (в sesinden önce)'),
    QC('Вчера ___ неделя.', ['беше', 'е', 'ще бъде'], 'Dün pazardı.', 'geçmiş → беше'),
    QT('Dokuzdan beşe kadar çalışırım.', ['Работя от девет до пет.', 'Работя до девет от пет.', 'Работиш от девет до пет.'], ''),
    QO('Saat kaçta?', 'В колко часа?', ['кой']),
  ])

# =====================================================================
M7 = M('a1-07', 'A1', '7. ders', 'Hava ve mevsimler: бях, ще бъда, обичам да', 'Време и сезони',
  '"Olmak" fiilinin geçmiş ve gelecek hâllerini, "-mayı severim" yapısını, се\'li fiilleri ve havayı anlatmayı öğreneceksin.',
  [
    TB('съм: geçmiş ve gelecek', ['Kişi', 'şimdi', 'geçmiş (-dım)', 'gelecek (-acağım)'], [
        ['аз', 'съм', 'бях', 'ще бъда'], ['ти', 'си', 'беше', 'ще бъдеш'], ['той/тя', 'е', 'беше', 'ще бъде'],
        ['ние', 'сме', 'бяхме', 'ще бъдем'], ['вие', 'сте', 'бяхте', 'ще бъдете'], ['те', 'са', 'бяха', 'ще бъдат']],
        'Olumsuz: не бях (değildim) · няма да бъда (olmayacağım). Konuşmada ще бъда yerine ще съм da denir.'),
    X('Örnekler', [
        ('Вчера бях вкъщи.', 'Dün evdeydim.'),
        ('Къде беше? — Бях на море.', 'Neredeydin? — Denizdeydim.'),
        ('Не бяхме в София.', "Sofya'da değildik."),
        ('Утре ще бъда на работа.', 'Yarın işte olacağım.'),
        ('Няма да бъда там.', 'Orada olmayacağım.'),
    ]),
    T('обичам да … — "-mayı severim"', """
Bulgarcada **mastar yok**, bu yüzden "okumayı severim" derken iki fiil **да** ile bağlanır ve **ikisi de çekilir**:
Обичам **да чета**. — Okumayı severim. (kelime kelime: "Seviyorum ki okuyayım")
Обичаш **да четеш**. — Okumayı seversin.
Започвам **да уча**. — Çalışmaya başlıyorum.
""", 'tr'),
    T('се ile biten fiiller', """
Bazı fiiller **се** ile kullanılır; Türkçedeki **-n- / -l-** dönüşlülük ekine benzer:
**разхождам се** — gezinmek · **казвам се** — adı … olmak · **връщам се** — dönmek

**се** cümleye başlamaz ve fiilin hemen önünde ya da arkasında durur:
Аз **се** разхождам. = Разхождам **се**. — Geziniyorum.
Не **се** разхождам. — Gezinmiyorum. (olumsuzda не + се + fiil)
"""),
    T('Hava nasıl?', """
**Какво е времето?** — Hava nasıl?
**Топло е.** Sıcak. · **Студено е.** Soğuk. · **Слънчево е.** Güneşli. · **Облачно е.** Bulutlu.
**Вали дъжд.** Yağmur yağıyor. · **Вали сняг.** Kar yağıyor. · **Духа вятър.** Rüzgâr esiyor.

Kişisel durum: **Топло ми е.** — Sıcakladım. · **Студено ми е.** — Üşüyorum. (kelime kelime: "Bana soğuk")
""", 'key'),
    TB('Mevsimler ve renkler', ['Mevsim', '', 'Renk (eril / dişil)', ''], [
        ['пролет', 'ilkbahar', 'бял / бяла', 'beyaz'], ['лято', 'yaz', 'черен / черна', 'siyah'],
        ['есен', 'sonbahar', 'червен / червена', 'kırmızı'], ['зима', 'kış', 'зелен / зелена', 'yeşil'],
        ['', '', 'син / синя', 'mavi'], ['', '', 'жълт / жълта', 'sarı']],
        'пролет ve есен dişildir: хубава пролет, топла есен.'),
    T('всеки, всички', """
**всеки** (her, eril) · **всяка** (dişil) · **всяко** (nötr) · **всички** (hepsi, herkes)
**всеки** ден — her gün · **всяка** сутрин — her sabah · **всички** студенти — bütün öğrenciler
"""),
  ],
  R('Картичка от морето', [
      ('Здравей, Мария!', 'Merhaba Maria!'),
      ('Тази седмица съм на море, в Созопол.', "Bu hafta deniz kenarındayım, Sozopol'de."),
      ('Времето е прекрасно — слънчево и топло.', 'Hava harika — güneşli ve sıcak.'),
      ('Всяка сутрин се разхождам на плажа.', 'Her sabah sahilde yürüyüş yapıyorum.'),
      ('Обичам да плувам и да чета на сянка.', 'Yüzmeyi ve gölgede kitap okumayı seviyorum.'),
      ('Вчера беше облачно и малко студено.', 'Dün bulutluydu ve biraz soğuktu.'),
      ('Бяхме в старата част на града.', 'Şehrin eski kısmındaydık.'),
      ('В неделя ще бъда в София.', "Pazar günü Sofya'da olacağım."),
      ('Всичко хубаво! Айше', 'Her şey gönlünce olsun! Ayşe'),
  ], [
      '**на море** — "deniz kenarında, tatilde": на + море kalıbı.',
      '**се разхождам** — се fiilin önünde, çünkü önünde başka kelime var (Всяка сутрин).',
      '**обичам да плувам и да чета** — iki fiil de "ben" hâlinde.',
      '**беше облачно** — havada "o" hâli: беше.',
  ], 'Denizden kartpostal'),
  [
    QC('Вчера аз ___ вкъщи.', ['бях', 'беше', 'бяха'], 'Dün evdeydim.', 'аз → бях'),
    QC('Те ___ в парка.', ['бяха', 'бяхме', 'беше'], 'Onlar parktaydı.', 'те → бяха'),
    QC('Утре ___ бъда на работа.', ['ще', 'не', 'да'], 'Yarın işte olacağım.', 'gelecek → ще'),
    QC('Обичам да ___.', ['чета', 'четеш', 'чете'], 'Okumayı severim.', 'да\'dan sonra fiil kişiye göre çekilir: аз → чета'),
    QC('___ ми е. Затвори прозореца!', ['Студено', 'Студен', 'Студена'], 'Üşüyorum. Pencereyi kapat!', 'Kişisel durum: … ми е (nötr biçim)'),
    QC('___ ден ходя на работа.', ['Всеки', 'Всяка', 'Всички'], 'Her gün işe giderim.', 'ден eril → всеки'),
    QT('Orada olmayacağım.', ['Няма да бъда там.', 'Не ще бъда там.', 'Не бъда там.'], 'Olumsuz gelecek: няма да'),
    QO('Her sabah yürüyüş yapıyorum.', 'Всяка сутрин се разхождам.', ['всеки']),
  ])
