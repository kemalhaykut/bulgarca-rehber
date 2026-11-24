# -*- coding: utf-8 -*-
from lib import T, TB, X, R, QC, QT, QO, M

# =====================================================================
M12 = M('a2-12', 'A2', '12. ders', 'Gündelik hayat: ще / няма да, да-yapıları, се fiilleri', 'Ежедневие',
  'Gelecek zamanı (olumlu, olumsuz, soru), искам да / мога да / трябва да yapılarını ve günlük се fiillerini öğreneceksin.',
  [
    T('Gelecek zaman: ще + fiil', """
Türkçede gelecek bir ektir (gel**eceğ**im). Bulgarcada **ще** adlı değişmeyen bir kelime fiilin önüne gelir; fiil şimdiki zamandaki gibi çekilir:
**Ще** работя. — Çalışacağım. · **Ще** работиш. — Çalışacaksın.

**Olumsuz:** *не ще* denmez → **няма да** + fiil: **Няма да** работя. — Çalışmayacağım.
**Soru:** ли fiilin arkasına: Ще дойдеш **ли**? — Gelecek misin?
Soru kelimesiyle ли yok: **Кога ще** дойдеш? — Ne zaman geleceksin?
""", 'tr'),
    TB('Gelecekte sık kullanılan tek seferlik hâller', ['Şimdiki zaman', 'Gelecek', 'Türkçe'], [
        ['отивам', 'ще отида', 'gideceğim'], ['идвам', 'ще дойда', 'geleceğim'], ['започвам', 'ще започна', 'başlayacağım'],
        ['виждам', 'ще видя', 'göreceğim'], ['казвам', 'ще кажа', 'söyleyeceğim'], ['правя', 'ще направя', 'yapacağım']],
        'Bir işi bir kez yapıp bitireceksen genelde ikinci hâl kullanılır.'),
    T('да-yapıları: искам да, мога да, трябва да', """
Bulgarcada mastar olmadığı için ikinci fiil **да** ile bağlanır ve **çekilir**:
**Искам да** спя. — Uyumak istiyorum. · Искам **да спиш**. — Uyumanı istiyorum.
**Мога да** дойда. — Gelebilirim. · **Трябва да** тръгвам. — Gitmem lazım.

Süreç mi tek sefer mi?
Мога да **говоря** турски. (genel yetenek → süreç)
Мога да **дойда** в пет. (tek bir olay → tek sefer)
"""),
    TB('Günlük се fiilleri', ['Bulgarca', 'Türkçe', 'Örnek'], [
        ['събуждам се', 'uyanmak', 'Събуждам се в седем.'], ['обличам се', 'giyinmek', 'Обличам се бързо.'],
        ['мия се', 'yıkanmak', 'Мия се със студена вода.'], ['смея се', 'gülmek', 'Защо се смееш?'],
        ['тревожа се', 'endişelenmek', 'Не се тревожи!'], ['шегувам се', 'şaka yapmak', 'Шегувам се!'],
        ['прибирам се', 'eve dönmek', 'Прибирам се късно.']],
        'Olumsuzda sıra: не + се + fiil → Не се тревожа.'),
    TB('Sıklık zarfları', ['Bulgarca', 'Türkçe'], [
        ['винаги', 'her zaman'], ['обикновено', 'genellikle'], ['често', 'sık sık'], ['понякога', 'bazen'],
        ['рядко', 'nadiren'], ['никога не', 'asla (+ olumsuz fiil)']],
        'Türkçe gibi çift olumsuz: Никога не закъснявам. — Asla gecikmem.'),
    X('Örnekler', [
        ('Утре ще стана рано.', 'Yarın erken kalkacağım.'),
        ('Няма да закъснея, обещавам!', 'Gecikmeyeceğim, söz veriyorum!'),
        ('Ще дойдеш ли довечера?', 'Bu akşam gelecek misin?'),
        ('Искам да започна нова работа.', 'Yeni bir işe başlamak istiyorum.'),
        ('Обикновено се прибирам в шест.', 'Genellikle altıda eve dönerim.'),
        ('Никога не пия кафе вечер.', 'Akşamları asla kahve içmem.'),
    ]),
  ],
  R('Утре е важен ден', [
      ('Утре Мехмет ще започне нова работа.', 'Yarın Mehmet yeni bir işe başlayacak.'),
      ('Той малко се тревожи.', 'Biraz endişeleniyor.'),
      ('Обикновено се събужда в осем, но утре трябва да стане в шест.', 'Genellikle sekizde uyanıyor ama yarın altıda kalkması gerekiyor.'),
      ('Ще се облече хубаво и ще отиде с метрото.', 'Güzel giyinecek ve metroyla gidecek.'),
      ('Няма да пие много кафе, защото после е нервен.', 'Çok kahve içmeyecek, çünkü sonra gergin oluyor.'),
      ('Съпругата му казва: „Не се тревожи! Всичко ще бъде наред.“', 'Eşi diyor ki: "Endişelenme! Her şey yolunda olacak."'),
      ('Мехмет се смее: „Знам, знам. Просто искам да направя добро впечатление.“', 'Mehmet gülüyor: "Biliyorum, biliyorum. Sadece iyi bir izlenim bırakmak istiyorum."'),
      ('Вечерта той ще се прибере и ще разкаже всичко.', 'Akşam eve dönecek ve her şeyi anlatacak.'),
  ], [
      '**ще започне** — "başlayacak": ще + tek seferlik hâl.',
      '**трябва да стане** — трябва değişmez, стане "o kalksın".',
      '**Няма да пие** — olumsuz gelecek: няма да.',
      '**Не се тревожи!** — olumsuz emir + се.',
  ], 'Yarın önemli bir gün'),
  [
    QC('Утре ___ работя.', ['ще', 'съм', 'ли'], 'Yarın çalışacağım.', 'gelecek → ще'),
    QC('Утре ___ работя.', ['няма да', 'не ще', 'не'], 'Yarın çalışmayacağım.', 'olumsuz gelecek → няма да'),
    QC('Ще дойдеш ___?', ['ли', 'да', 'не'], 'Gelecek misin?', 'soru → ли fiilin arkasına'),
    QC('Кога ___ дойдеш?', ['ще', 'ли ще', 'ще ли'], 'Ne zaman geleceksin?', 'soru kelimesi → ли yok'),
    QC('Искам ___ спя.', ['да', 'че', 'ще'], 'Uyumak istiyorum.', 'iki fiil → да'),
    QC('Не ___ тревожи!', ['се', 'си', 'ще'], 'Endişelenme!', 'тревожа се → се'),
    QC('Никога ___ закъснявам.', ['не', 'няма', 'ли'], 'Asla gecikmem.', 'никога + не (çift olumsuz)'),
    QT('Gecikmeyeceğim.', ['Няма да закъснея.', 'Не ще закъснея.', 'Ще не закъснея.'], ''),
    QO('Yarın erken kalkacağım.', 'Утре ще стана рано.', ['няма']),
  ])

# =====================================================================
M13 = M('a2-13', 'A2', '13. ders', 'İnternet kafe: tamamlanan eylemler', 'Интернет кафе',
  'вляза, изляза, отворя, затворя, намеря gibi tek seferlik fiilleri, но / и bağlaçlarını ve fiilden isim yapmayı öğreneceksin.',
  [
    T('Tek seferlik hâl ne zaman zorunlu?', """
Tek seferlik (свършен) hâl **tek başına şimdiki zamanda** neredeyse kullanılmaz. Genelde şu kelimelerden sonra gelir:
**да** (искам да, мога да, трябва да) · **ще** · **ако** (eğer) · **когато** (-dığında)

Искам да **отворя** прозореца. — Pencereyi açmak istiyorum.
Може ли да **вляза**? — Girebilir miyim?
Когато **намеря** работа, ще ти кажа. — İş bulduğumda sana söyleyeceğim.
""", 'key'),
    TB('Yeni çiftler', ['Süreç', 'Tek sefer', 'Türkçe'], [
        ['влизам', 'вляза', 'girmek'], ['излизам', 'изляза', 'çıkmak'], ['отварям', 'отворя', 'açmak'],
        ['затварям', 'затворя', 'kapatmak'], ['качвам се', 'кача се', 'binmek / çıkmak'], ['свалям', 'сваля', 'indirmek'],
        ['правя', 'направя', 'yapmak'], ['намирам', 'намеря', 'bulmak'], ['изпращам', 'изпратя', 'göndermek']]),
    T('Bilgisayar dili', """
**компютър** · **мишка** · **клавиатура** · **екран** · **принтер**
**пиша имейл** · **изпращам съобщение** · **свалям файл** (dosya indirmek) · **влизам в сайта** (siteye girmek) · **парола** (şifre)
"""),
    T('и / но / а', """
**и** = ve: Влизам **и** сядам.
**но** = ama: Искам да изпратя имейл, **но** няма интернет.
**а** = ise / oysa (karşılaştırma): Аз пиша, **а** той чете.
"""),
    T('Fiilden isim: -не', """
Türkçedeki **-me / -ma** (okuma, yazma) Bulgarcada çoğu zaman **-не**'dir:
чета → **четене** (okuma) · пиша → **писане** (yazma) · пазарувам → **пазаруване** (alışveriş) · уча → **учене** (öğrenme)
**Четенето** е полезно. — Okumak faydalıdır.
""", 'tr'),
    X('Örnekler', [
        ('Може ли да отворя прозореца?', 'Pencereyi açabilir miyim?'),
        ('Трябва да изляза за малко.', 'Biraz dışarı çıkmam lazım.'),
        ('Не мога да намеря паролата.', 'Şifreyi bulamıyorum.'),
        ('Искам да изпратя този файл, но интернетът не работи.', 'Bu dosyayı göndermek istiyorum ama internet çalışmıyor.'),
        ('Когато влезеш в сайта, натисни тук.', 'Siteye girdiğinde buraya bas.'),
        ('Ученето на езици ми харесва.', 'Dil öğrenmeyi seviyorum.'),
    ]),
  ],
  R('Проблем с принтера', [
      ('Борис влиза в интернет кафето до университета.', 'Boris üniversitenin yanındaki internet kafeye giriyor.'),
      ('Той трябва да принтира една курсова работа.', 'Bir ödevin çıktısını alması gerekiyor.'),
      ('— Добър ден! Може ли да използвам компютър?', '— İyi günler! Bir bilgisayarı kullanabilir miyim?'),
      ('— Разбира се. Седнете на номер пет.', '— Tabii ki. Beş numaraya oturun.'),
      ('Борис отваря имейла си, но не може да намери файла.', 'Boris e-postasını açıyor ama dosyayı bulamıyor.'),
      ('После се сеща, че го има в облака.', 'Sonra dosyanın bulutta olduğunu hatırlıyor.'),
      ('Сваля го и натиска „Принтирай“.', 'Onu indiriyor ve "Yazdır"a basıyor.'),
      ('Принтерът не работи! Служителят идва и го оправя.', 'Yazıcı çalışmıyor! Görevli geliyor ve onu düzeltiyor.'),
      ('Борис плаща, излиза и бърза към лекцията.', 'Boris ödüyor, çıkıyor ve derse yetişmek için acele ediyor.'),
  ], [
      '**може ли да използвам** — "kullanabilir miyim": да + fiil.',
      '**не може да намери** — да\'dan sonra tek seferlik hâl (намеря → намери).',
      '**имейла си** — "kendi e-postası": си = kendi (14. ders).',
      '**го има в облака** — "bulutta var": го = o dosya.',
  ], 'Yazıcı sorunu'),
  [
    QC('Може ли да ___?', ['вляза', 'влизам', 'влиза'], 'Girebilir miyim? (içeri)', 'да + tek sefer → вляза'),
    QC('Всеки ден ___ в 8 часа.', ['излизам', 'изляза', 'излезе'], 'Her gün saat 8\'de çıkarım.', 'her gün → süreç'),
    QC('Искам да ___ прозореца.', ['отворя', 'отварям', 'отвори'], 'Pencereyi açmak istiyorum.', 'да + tek sefer'),
    QC('Не мога да ___ ключовете.', ['намеря', 'намирам', 'намериш'], 'Anahtarları bulamıyorum.', 'да + tek sefer, ben → намеря'),
    QC('Искам да дойда, ___ нямам време.', ['но', 'и', 'а'], 'Gelmek istiyorum ama vaktim yok.', 'ama = но'),
    QC('чета → ___', ['четене', 'четя', 'четец'], 'okuma', 'fiilden isim -не'),
    QT('Pencereyi kapatabilir miyim?', ['Може ли да затворя прозореца?', 'Може ли да затварям прозореца?', 'Може ли затворя прозореца?'], ''),
    QO('Biraz dışarı çıkmam lazım.', 'Трябва да изляза за малко.', ['излизам']),
  ])

# =====================================================================
M14 = M('a2-14', 'A2', '14. ders', 'Cumartesi akşamı: се / си, „benim için“, davet', 'Събота вечер',
  'се ile си farkını, edattan sonraki uzun zamirleri (за мен, с теб) ve davet etme / kabul / ret kalıplarını öğreneceksin.',
  [
    T('се ve си farkı', """
**се** = kendini (eylem kişinin kendisine): **Мия се.** — Yıkanıyorum.
**си** = kendi … -ımı / kendime: **Мия си ръцете.** — Ellerimi yıkıyorum.

Türkçe ipucu: "kendimi" → **се** · "kendime / kendi …-ımı" → **си**
Обличам **се**. — Giyiniyorum. · Обличам **си** палтото. — Paltomu giyiyorum.
Купих **си** нов телефон. — Kendime yeni telefon aldım.
""", 'tr'),
    T('си ile sahiplik: "kendi"', """
Özne ile sahip aynı kişiyse **си** kullanılır:
Той чете книгата **си**. — (Kendi) kitabını okuyor.
Той чете книгата **му**. — (Başka birinin) kitabını okuyor.
""", 'warn'),
    TB('Edattan sonra uzun zamirler', ['Kişi', 'Uzun biçim', 'Örnek', 'Türkçe'], [
        ['аз', 'мен', 'за мен', 'benim için'], ['ти', 'теб', 'с теб', 'seninle'], ['той', 'него', 'без него', 'onsuz'],
        ['тя', 'нея', 'при нея', 'onun yanında'], ['ние', 'нас', 'за нас', 'bizim için'],
        ['вие', 'вас', 'с вас', 'sizinle'], ['те', 'тях', 'от тях', 'onlardan']],
        'Edattan sonra kısa biçim (ме, те, го) kullanılmaz: ❌ за ме → ✅ за мен'),
    T('Vurgu için uzun biçim', """
Normalde kısa biçim: Обичам **те**.
Vurgu yapmak için uzun biçim cümle başına gelir ve kısa biçim de kalır:
**Теб те** обичам, не него! — **Seni** seviyorum, onu değil!
"""),
    T('искам да дойда — çekim', """
**да + дойда** çekimi: аз искам да **дойда** · ти искаш да **дойдеш** · той иска да **дойде** · ние искаме да **дойдем** · вие искате да **дойдете** · те искат да **дойдат**
"""),
    TB('Davet: kabul ve ret', ['Durum', 'Bulgarca', 'Türkçe'], [
        ['davet', 'Искаш ли да излезем довечера?', 'Bu akşam dışarı çıkalım mı?'],
        ['davet', 'Каня те на кино.', 'Seni sinemaya davet ediyorum.'],
        ['kabul', 'С удоволствие!', 'Memnuniyetle!'], ['kabul', 'Добра идея!', 'İyi fikir!'],
        ['ret', 'Съжалявам, но не мога.', 'Üzgünüm ama yapamam.'], ['ret', 'Може би друг път.', 'Belki başka zaman.']]),
    TB('Kıyafetler', ['Bulgarca', 'Türkçe', 'Bulgarca', 'Türkçe'], [
        ['рокля', 'elbise', 'риза', 'gömlek'], ['панталон', 'pantolon', 'пола', 'etek'],
        ['яке', 'mont', 'палто', 'palto'], ['обувки', 'ayakkabı', 'чанта', 'çanta']],
        'облека се / обличам се = giyinmek · съблека се / събличам се = soyunmak'),
    X('Örnekler', [
        ('Ела с нас! Ще бъде весело.', 'Bizimle gel! Eğlenceli olacak.'),
        ('Този подарък е за теб.', 'Bu hediye senin için.'),
        ('Измий си ръцете преди вечеря!', 'Yemekten önce ellerini yıka!'),
        ('Облечи се топло, навън е студено.', 'Sıkı giyin, dışarısı soğuk.'),
        ('Без теб няма да отида.', 'Sensiz gitmeyeceğim.'),
        ('Трудно ми е да стана рано в събота.', 'Cumartesi erken kalkmak bana zor geliyor.'),
    ]),
  ],
  R('Покана за рожден ден', [
      ('В събота Ана има рожден ден и кани приятелите си на вечеря.', 'Cumartesi Ana\'nın doğum günü ve arkadaşlarını akşam yemeğine davet ediyor.'),
      ('Тя пише на Айше: „Искаш ли да дойдеш в събота вечер?“', 'Ayşe\'ye yazıyor: "Cumartesi akşamı gelmek ister misin?"'),
      ('Айше отговаря: „С удоволствие! Мога ли да доведа и Мехмет?“', 'Ayşe cevap veriyor: "Memnuniyetle! Mehmet\'i de getirebilir miyim?"'),
      ('„Разбира се! Ще се радвам да го видя.“', '"Tabii ki! Onu görmekten mutlu olurum."'),
      ('В събота Айше се облича бавно.', 'Cumartesi Ayşe yavaşça giyiniyor.'),
      ('Слага си новата рокля и купува подарък за Ана.', 'Yeni elbisesini giyiyor ve Ana için bir hediye alıyor.'),
      ('Мехмет закъснява, защото търси ключовете си.', 'Mehmet gecikiyor, çünkü anahtarlarını arıyor.'),
      ('Накрая те идват заедно и всички се смеят и танцуват.', 'Sonunda birlikte geliyorlar ve herkes gülüp dans ediyor.'),
      ('„Без вас няма да е същото!“ — казва Ана.', '"Sizsiz aynı olmaz!" diyor Ana.'),
  ], [
      '**приятелите си** — "kendi arkadaşlarını": си, özne Ana olduğu için.',
      '**се облича** — "giyiniyor" (kendini): се.',
      '**Слага си новата рокля** — "kendine yeni elbisesini koyuyor/giyiyor": си.',
      '**Без вас** — edattan sonra uzun biçim: вас.',
  ], 'Doğum günü daveti'),
  [
    QC('Мия ___ ръцете.', ['си', 'се', 'ме'], 'Ellerimi yıkıyorum.', 'kendi ellerimi → си'),
    QC('Сутрин се мия и ___ обличам.', ['се', 'си', 'ме'], 'Sabahları yıkanıp giyiniyorum.', 'kendimi giydiriyorum → се'),
    QC('Този подарък е за ___.', ['теб', 'те', 'ти'], 'Bu hediye senin için.', 'edattan sonra uzun biçim'),
    QC('Ела с ___!', ['нас', 'ни', 'ние'], 'Bizimle gel!', 'с + uzun biçim'),
    QC('Той чете книгата ___.', ['си', 'му', 'се'], 'Kendi kitabını okuyor.', 'özne = sahip → си'),
    QC('Искаш ли да ___ довечера?', ['дойдеш', 'дойда', 'идваш'], 'Bu akşam gelmek ister misin?', 'ти → дойдеш'),
    QT('Üzgünüm ama yapamam.', ['Съжалявам, но не мога.', 'Съжалявам, и не мога.', 'Съжалявам, но мога не.'], ''),
    QO('Sensiz gitmeyeceğim.', 'Без теб няма да отида.', ['те']),
  ])
