# -*- coding: utf-8 -*-
from lib import T, TB, X, R, QC, QT, QO, M

# =====================================================================
M1 = M('a1-01', 'A1', '1. ders', 'Tanışma: ben, sen, o ve „съм“', 'Здравейте!',
  'Selamlaşmayı, kendini tanıtmayı ve "olmak" fiili съм\'ü öğreneceksin.',
  [
    T('Selamlaşma', """
Bulgarcada günün saatine göre selam verilir:
**Добро утро!** — Günaydın! · **Добър ден!** — İyi günler! · **Добър вечер!** — İyi akşamlar! · **Лека нощ!** — İyi geceler!

Tanıdığın birine **Здравей!** (Merhaba!), birden fazla kişiye ya da kibar hitapta **Здравейте!** dersin. Ayrılırken **Довиждане!** ya da arkadaşça **Чао!**
"""),
    TB('Kişi zamirleri', ['Bulgarca', 'Türkçe', 'Not'], [
        ['аз', 'ben', ''], ['ти', 'sen', ''],
        ['той', 'o (erkek)', 'Türkçede tek "o" var; Bulgarcada üç tane!'],
        ['тя', 'o (kadın)', ''], ['то', 'o (nötr: çocuk, nesne)', ''],
        ['ние', 'biz', ''], ['вие / Вие', 'siz / kibar "Siz"', 'Kibar hitapta büyük harfle yazılır'],
        ['те', 'onlar', 'тя (o, kadın) ile karıştırma']]),
    T('„съм“ = Türkçedeki -ım, -sın, -dır', """
Türkçede "olmak" çoğu zaman bir **ek**tir: öğrenci**yim**, doktor**sun**.
Bulgarcada bu ek **ayrı bir kelimedir: съм**. Ünlü uyumu yoktur; sadece kişiye göre değişir.

Öğrenci**yim** → Аз **съм** студент.
Türk**üm** → Аз **съм** турчин.
""", 'tr'),
    TB('съм çekimi', ['Kişi', 'съм', 'Türkçe karşılığı'], [
        ['аз', 'съм', '-ım/-im/-um/-üm'], ['ти', 'си', '-sın/-sin'], ['той/тя/то', 'е', '(ek yok) / -dır'],
        ['ние', 'сме', '-ız/-iz'], ['вие', 'сте', '-sınız/-siniz'], ['те', 'са', '-lar/-ler']],
        'Ezber kalıbı: съм – си – е · сме – сте – са'),
    X('Örnekler', [
        ('Аз съм Мехмет.', "Ben Mehmet'im."),
        ('Аз съм от Турция.', "Türkiye'denim."),
        ('Ти си студентка.', 'Sen öğrencisin. (kadına)'),
        ('Той е лекар.', 'O doktor.'),
        ('Тя е от България.', "O Bulgaristan'dan."),
        ('Ние сме приятели.', 'Biz arkadaşız.'),
        ('Вие сте от София.', "Siz Sofya'dansınız."),
        ('Те са колеги.', 'Onlar iş arkadaşı.'),
    ]),
    T('Zamir düşebilir — ama съм cümleye başlamaz', """
Türkçede "Ben öğrenciyim" yerine "Öğrenciyim" deriz. Bulgarcada da zamir düşebilir, çünkü fiil kişiyi zaten gösterir.
Ama **съм, си, е, сме, сте, са** cümlenin **ilk kelimesi olamaz**:

❌ Съм студент. ✅ **Студент съм.** ✅ **Аз съм студент.**
""", 'warn'),
    T('Olumsuz ve soru', """
**Olumsuz:** fiilin önüne **не** gelir: Аз **не съм** лекар. — Doktor değilim.
"не съм" bir blok olduğu için cümleye bununla başlanabilir: **Не съм** от тук. — Buralı değilim.

**Soru:** Türkçedeki **mi/mı** ekinin karşılığı **ли**'dir ve tıpkı Türkçede olduğu gibi **sorduğun kelimenin arkasına** gelir:
Лекар **ли** си? — Doktor **mu**sun?
От България **ли** сте? — Bulgaristan'dan **mı**sınız?
""", 'tr'),
    TB('Soru kelimeleri', ['Bulgarca', 'Türkçe', 'Örnek'], [
        ['кой / коя', 'kim (erkek / kadın)', 'Кой е той?'],
        ['откъде', 'nereden', 'Откъде си?'],
        ['как', 'nasıl', 'Как си? · Как се казваш?'],
        ['какъв / каква / какви', 'ne (meslek, milliyet)', 'Какъв е той? — Лекар.'],
    ], 'Soru kelimesi varsa ли kullanılmaz: Откъде си? (❌ Откъде ли си?)'),
    T('„Казвам се“ — adım …', """
**Как се казваш?** — Adın ne? (sana) · **Как се казвате?** — Adınız ne? (kibar)
**Казвам се Айше.** — Adım Ayşe. (kelime kelime: "Ayşe diye çağrılırım")
**Аз се казвам Айше.** — zamirle de olur; **се** zamirden sonra, fiilden önce gelir.
"""),
    T('и ve а', """
**и** = ve: Иван **и** Мария са приятели.
**а** = "peki / ise", karşılaştırma ve soru geri yöneltme: Аз съм от Турция, **а** ти? — Ben Türkiye'denim, ya sen?
"""),
    TB('Sayılar 1–10', ['', '', '', ''], [
        ['1 едно', '2 две', '3 три', '4 четири'], ['5 пет', '6 шест', '7 седем', '8 осем'], ['9 девет', '10 десет', '', '']],
        '1 ve 2 isimle birlikte değişir (един/една/едно, два/две) — 3. derste.'),
    X('Günlük kalıplar', [
        ('Как си? — Добре съм, благодаря. А ти?', 'Nasılsın? — İyiyim, teşekkürler. Ya sen?'),
        ('Приятно ми е.', 'Memnun oldum.'),
        ('Откъде сте? — От Турция.', "Nerelisiniz? — Türkiye'den."),
        ('Всичко хубаво!', 'Her şey gönlünce olsun!'),
    ]),
  ],
  R('Ново запознанство', [
      ('Добър ден! Казвам се Мехмет.', 'İyi günler! Adım Mehmet.'),
      ('Аз съм от Турция, от Бурса.', "Türkiye'denim, Bursa'dan."),
      ('Сега съм в София.', "Şimdi Sofya'dayım."),
      ('Аз съм студент.', 'Ben öğrenciyim.'),
      ('Това е Елена.', 'Bu Elena.'),
      ('Тя е българка, от Пловдив.', "O Bulgar, Plovdiv'den."),
      ('Елена е лекарка.', 'Elena doktor.'),
      ('Ние сме приятели.', 'Biz arkadaşız.'),
      ('— Как си, Елена?', '— Nasılsın Elena?'),
      ('— Добре съм, благодаря. А ти?', '— İyiyim, teşekkürler. Ya sen?'),
      ('— И аз съм добре.', '— Ben de iyiyim.'),
  ], [
      '**Аз съм от Турция** — "-den" anlamı **от** ile verilir.',
      '**Сега съм в София** — zamir düştü, съм ikinci sırada.',
      '**Това е Елена** — birini tanıtırken **Това е …** (Bu …).',
      '**И аз** — "ben de". и burada "de/da" anlamında.',
  ], 'Yeni bir tanışma'),
  [
    QC('Аз ___ студент.', ['съм', 'си', 'е'], 'Ben öğrenciyim.', 'аз → съм'),
    QC('Те ___ от Варна.', ['са', 'е', 'сте'], "Onlar Varna'dan.", 'те → са'),
    QC('Тя ___ лекарка.', ['е', 'са', 'сме'], 'O doktor.', 'тя → е'),
    QC('Лекар ___ си?', ['ли', 'не', 'и'], 'Doktor musun?', 'Soru eki ли sorulan kelimenin arkasına gelir.'),
    QC('___ си? — От Турция.', ['Откъде', 'Кой', 'Как'], "Nerelisin? — Türkiye'den.", 'nereden = откъде'),
    QT('Doktor değilim.', ['Не съм лекар.', 'Съм не лекар.', 'Лекар не ли съм.'], 'не, fiilin önüne gelir.'),
    QT('Öğrenciyim.', ['Студент съм.', 'Съм студент.', 'Студент си.'], 'съм cümleye başlayamaz.'),
    QO("Ben Türkiye'denim.", 'Аз съм от Турция.', ['си']),
    QO('Adın ne?', 'Как се казваш?', ['ли']),
  ])

# =====================================================================
M2 = M('a1-02', 'A1', '2. ders', 'Bu ne? — има / няма, имам / нямам', 'Какво е това?',
  '"Var/yok" demeyi, sahipliği ve 11–20 arası sayıları öğreneceksin.',
  [
    T('Какво е това? — Bu ne?', """
Bir nesneyi sorarken: **Какво е това?** — Bu ne?
Bir kişiyi sorarken: **Кой е това?** — Bu kim?
Cevap: **Това е** книга. — Bu bir kitap. · **Това е** Иван. — Bu İvan.

⚠️ "Bu bir kitap" derken "bir" (една) çoğu zaman söylenmez: Това е книга.
"""),
    X('Örnekler', [
        ('Какво е това? — Това е телефон.', 'Bu ne? — Bu bir telefon.'),
        ('Това химикалка ли е? — Не, това е молив.', 'Bu tükenmez kalem mi? — Hayır, bu kurşun kalem.'),
        ('Кой е това? — Това е моят колега.', 'Bu kim? — Bu benim iş arkadaşım.'),
    ]),
    T('има = var, няма = yok', """
Türkçedeki **var** ve **yok** Bulgarcada **има** ve **няма**'dır. Türkçedeki gibi **hiç değişmezler**: tekil, çoğul fark etmez.

Тук **има** кафене. — Burada bir kafe var.
Тук **няма** банка. — Burada banka yok.
**Има ли** вода? — Su var mı?

⚠️ "Yok" için asla *не има* denmez → her zaman **няма**.
""", 'tr'),
    T('имам = bende var (sahiplik)', """
Türkçede "Arabam var" deriz. Bulgarcada kişiye göre çekilen bir fiil kullanılır: **Имам кола.** (Sahibim araba.)
Olumsuzu da tek kelime: **нямам** — bende yok.
"""),
    TB('имам / нямам', ['Kişi', 'имам', 'нямам', 'Türkçe'], [
        ['аз', 'имам', 'нямам', 'benim var / yok'], ['ти', 'имаш', 'нямаш', 'senin var / yok'],
        ['той, тя', 'има', 'няма', 'onun var / yok'], ['ние', 'имаме', 'нямаме', 'bizim var / yok'],
        ['вие', 'имате', 'нямате', 'sizin var / yok'], ['те', 'имат', 'нямат', 'onların var / yok']],
        'Ekler Türkçe kişi ekleri gibi: -м (ben), -ш (sen), — (o), -ме (biz), -те (siz), -т (onlar)'),
    X('Örnekler', [
        ('Имам брат и сестра.', 'Bir erkek, bir kız kardeşim var.'),
        ('Имаш ли време? — Нямам.', 'Vaktin var mı? — Yok.'),
        ('Тя има куче.', 'Onun köpeği var.'),
        ('Нямаме въпроси.', 'Sorumuz yok.'),
        ('В стаята има маса и два стола.', 'Odada bir masa ve iki sandalye var.'),
        ('Тук няма никой.', 'Burada kimse yok.'),
    ]),
    T('има mı, е mi?', """
Türkçede de bu fark var:
"Burada **bir banka var**." (varlık, belirsiz) → **Тук има банка.**
"**Banka** burada." (belli bir şeyin yeri) → **Банката е тук.**
""", 'key'),
    T('Kelime sırası: съм ve се nereye gelir?', """
Zamir varsa: **Аз съм** Иван. · **Аз се казвам** Иван.
Zamir yoksa: **Иван съм.** · **Казвам се** Иван. (съм / се cümleye başlamaz)
Soru: **Студент ли си?** · **Как се казвате?**
"""),
    TB('Sayılar 11–20', ['', '', ''], [
        ['11 единайсет', '12 дванайсет', '13 тринайсет'], ['14 четиринайсет', '15 петнайсет', '16 шестнайсет'],
        ['17 седемнайсет', '18 осемнайсет', '19 деветнайсет'], ['20 двайсет', '', '']],
        '"-найсет" = "on üstüne". Yazı dilinde: единадесет, дванадесет … двадесет.'),
  ],
  R('В стаята', [
      ('Това е моята стая.', 'Bu benim odam.'),
      ('Тук има легло, маса и стол.', 'Burada bir yatak, bir masa ve bir sandalye var.'),
      ('На масата има лаптоп и книга.', 'Masanın üstünde bir dizüstü bilgisayar ve bir kitap var.'),
      ('Няма телевизор, но имам радио.', 'Televizyon yok ama radyom var.'),
      ('— Имаш ли интернет тук?', '— Burada internetin var mı?'),
      ('— Да, имам.', '— Evet, var.'),
      ('— А имаш ли кафе?', '— Peki kahven var mı?'),
      ('— Не, нямам. Но има чай!', '— Hayır, yok. Ama çay var!'),
  ], [
      '**Тук има …** — "Burada … var". има tekil/çoğul fark etmeden aynı.',
      '**На масата** — "masanın üstünde": на = üstünde.',
      '**Да, имам.** — Türkçedeki gibi cevapta fiil tekrarlanır.',
  ], 'Odada'),
  [
    QC('Тук ___ банка.', ['няма', 'не има', 'нямам'], 'Burada banka yok.', 'yok = няма'),
    QC('Ти ___ ли кола?', ['имаш', 'имам', 'има'], 'Araban var mı?', 'ти → имаш'),
    QC('Ние ___ време.', ['нямаме', 'нямате', 'нямат'], 'Vaktimiz yok.', 'ние → -ме'),
    QC('___ е това? — Това е Иван.', ['Кой', 'Какво', 'Откъде'], 'Bu kim? — Bu İvan.', 'kişi → кой'),
    QC('Банката ___ тук.', ['е', 'има', 'са'], 'Banka burada.', 'Belli bir şeyin yeri → е'),
    QT('Su var mı?', ['Има ли вода?', 'Вода ли има е?', 'Имам ли вода?'], 'има + ли'),
    QT('Adım İvan.', ['Казвам се Иван.', 'Се казвам Иван.', 'Иван казвам.'], 'се cümleye başlamaz.'),
    QO('Bir kız kardeşim var.', 'Имам една сестра.', ['има']),
    QO('Burada kimse yok.', 'Тук няма никой.', ['не']),
  ])

# =====================================================================
M3 = M('a1-03', 'A1', '3. ders', 'Kafede: cinsiyet, „bir“ ve tanımlık', 'В кафето',
  'İsimlerin cinsiyetini, един/една/едно\'yu, belirli tanımlığı (-та, -то, -ът) ve -м fiillerini öğreneceksin.',
  [
    T('Her ismin bir cinsiyeti var', """
Türkçede kelimelerin cinsiyeti yoktur. Bulgarcada her isim **eril, dişil** veya **nötr**dür ve bu **son harften** anlaşılır.
Bu anlamla ilgili değil, kelimenin **sesiyle** ilgilidir: masa (маса) "dişi"dir, sandalye (стол) "erkek"tir.
""", 'tr'),
    TB('Son harfe bak', ['Son harf', 'Cinsiyet', '"bir"', 'Örnek'], [
        ['ünsüz, -й', 'eril', 'един', 'един сок, един чай'],
        ['-а, -я', 'dişil', 'една', 'една вода, една баница'],
        ['-о, -е', 'nötr', 'едно', 'едно кафе, едно мляко'],
        ['-и, -у, -ю (yabancı)', 'nötr', 'едно', 'едно такси, едно меню']],
        'İstisnalar: баща (baba), дядо (dede) eril; нощ (gece), сол (tuz), вечер (akşam) dişil.'),
    T('Belirli tanımlık: ismin SONUNA eklenir', """
Türkçede "Kahve**yi** içtim" derken bildiğimiz kahveden bahsederiz. Bulgarcada "bilinen şey" için ismin sonuna bir ek gelir — tıpkı Türkçe gibi **sona**:

кафе → кафе**то** (o kahve) · вода → вода**та** (o su) · сок → сок**ът** (o meyve suyu)
""", 'tr'),
    TB('Tekil tanımlık', ['Cinsiyet', 'Ek', 'Örnek'], [
        ['dişil', '-та', 'водата, баницата, сметката'],
        ['nötr', '-то', 'кафето, млякото'],
        ['eril (özne)', '-ът / -ят', 'сокът, чаят, хлябът'],
        ['eril (özne değil)', '-а / -я', 'Пия сока. · Искам чая.']],
        'Eril hilesi: Türkçede ek almıyorsa (özne) -ът; -ı, -da, -e gibi ek alıyorsa -а.'),
    X('Örnekler', [
        ('Едно кафе, моля.', 'Bir kahve, lütfen.'),
        ('Кафето е горещо.', 'Kahve sıcak.'),
        ('Сокът е студен.', 'Meyve suyu soğuk.'),
        ('Искам сока, не водата.', 'Meyve suyunu istiyorum, suyu değil.'),
        ('Сметката, моля!', 'Hesap, lütfen!'),
        ('Една баница и един айрян.', 'Bir banitsa ve bir ayran.'),
    ]),
    T('Sıfatlar da cinsiyete uyar', """
Sıfat, Türkçedeki gibi ismin önüne gelir ama **ismin cinsiyetini taklit eder**:
голям чай · голям**а** вода · голям**о** кафе
малък сок · малк**а** баница · малк**о** мляко (малък'ta ъ düşer)
топъл · топл**а** · топл**о** — студен · студен**а** · студен**о**
"""),
    T('-м ile biten fiiller (3. grup)', """
**искам** (istemek), **вземам** (almak), **обичам** (sevmek), **закусвам** (kahvaltı yapmak), **разбирам** (anlamak), **предпочитам** (tercih etmek)
Hepsi **имам** gibi çekilir: -м, -ш, —, -ме, -те, -т.
Bulgarcada **mastar yoktur**; sözlükte fiil "ben" hâliyle yazılır: искам = "istiyorum" / "istemek".
"""),
    X('Fiillerle', [
        ('Какво искате? — Искам чай.', 'Ne istersiniz? — Çay istiyorum.'),
        ('Вземам едно кафе без захар.', 'Şekersiz bir kahve alıyorum.'),
        ('Тя предпочита чай с мляко.', 'O sütlü çayı tercih ediyor.'),
        ('Обичаме баница.', 'Banitsayı severiz.'),
        ('Разбираш ли?', 'Anlıyor musun?'),
    ]),
    T('с / със, без, в / във', """
**с** = ile: кафе **с** мляко (sütlü kahve) · **със** önce с/з ile başlayan kelimede: **със** захар
**без** = -sız: кафе **без** захар (şekersiz kahve)
**в** = -de: **в** кафето (kafede) · **във** önce в/ф: **във** Варна
**тук** = burada · **там** = orada
"""),
    TB('Sayılar 20–100', ['', '', ''], [
        ['20 двайсет', '30 трийсет', '40 четирийсет'], ['50 петдесет', '60 шейсет', '70 седемдесет'],
        ['80 осемдесет', '90 деветдесет', '100 сто']],
        '21 = двайсет и едно · 35 = трийсет и пет (son sayıdan önce и = "ve")'),
  ],
  R('В кафенето', [
      ('Мария и Али са в кафенето.', 'Maria ve Ali kafedeler.'),
      ('Сервитьорът пита: „Какво обичате?“', 'Garson soruyor: "Ne arzu edersiniz?"'),
      ('Мария иска едно кафе с мляко.', 'Maria sütlü bir kahve istiyor.'),
      ('Али не обича кафе.', 'Ali kahve sevmez.'),
      ('Той предпочита чай без захар.', 'O şekersiz çayı tercih ediyor.'),
      ('Те вземат и една баница.', 'Bir de banitsa alıyorlar.'),
      ('Баницата е топла и вкусна.', 'Banitsa sıcak ve lezzetli.'),
      ('Чаят е малко студен.', 'Çay biraz soğuk.'),
      ('— Сметката, моля!', '— Hesap, lütfen!'),
  ], [
      '**Сервитьорът** — eril, özne → **-ът**.',
      '**Какво обичате?** — garsonun kalıbı: "Ne arzu edersiniz?" (kelime kelime "ne seversiniz?").',
      '**Баницата е топла** — dişil isim, dişil sıfat: топл**а**.',
      '**Чаят** — -й ile biten eril isim: чай → ча**ят**.',
  ], 'Kafede'),
  [
    QC('___ кафе, моля.', ['Едно', 'Един', 'Една'], 'Bir kahve, lütfen.', 'кафе nötr → едно'),
    QC('___ вода, моля.', ['Една', 'Един', 'Едно'], 'Bir su, lütfen.', 'вода dişil → една'),
    QC('Кафе___ е горещо.', ['то', 'та', 'ът'], 'Kahve sıcak.', 'nötr → -то'),
    QC('Сок___ е студен.', ['ът', 'а', 'то'], 'Meyve suyu soğuk.', 'eril özne → -ът'),
    QC('Искам сок___.', ['а', 'ът', 'та'], 'Meyve suyunu istiyorum.', 'özne değil → -а'),
    QC('Чай ___ захар.', ['без', 'със', 'във'], 'Şekersiz çay.', '-sız = без'),
    QC('Тя ___ чай.', ['предпочита', 'предпочитам', 'предпочитат'], 'O çayı tercih ediyor.', 'тя → ek yok'),
    QT('Banitsa sıcak.', ['Баницата е топла.', 'Баница е топъл.', 'Баницата е топло.'], 'dişil isim + dişil sıfat'),
    QO('Sütlü bir kahve istiyorum.', 'Искам едно кафе с мляко.', ['една']),
  ])

# =====================================================================
M4 = M('a1-04', 'A1', '4. ders', 'Üniversitede: çoğul, „bu/şu“, го / я / ги', 'В университета',
  'Çoğul yapmayı, çoğul tanımlığı, този/онзи\'yi ve "onu/onları" zamirlerini öğreneceksin.',
  [
    T('Çoğul — Türkçedeki -lar/-ler', """
Türkçede tek bir çoğul eki var. Bulgarcada çoğul eki **cinsiyete ve son harfe** göre değişir, ama varsayılan ek **-и**'dir.
""", 'tr'),
    TB('Çoğul ekleri', ['İsim', 'Ek', 'Örnek'], [
        ['dişil (-а/-я)', '-и', 'книга → книги, стая → стаи'],
        ['eril, çok heceli', '-и', 'студент → студенти, учебник → учебници'],
        ['eril, tek heceli', '-ове', 'град → градове, стол → столове'],
        ['nötr -о', '-а', 'писмо → писма, място → места'],
        ['nötr -е', '-ета', 'кафе → кафета, момиче → момичета'],
        ['düzensiz', '—', 'човек → хора, дете → деца, брат → братя']],
        '-к ile biten erillerde к → ц olur: учебник → учебници.'),
    T('Çoğulda tanımlık: -те / -та', """
Çoğulun **son harfine** bak:
-и / -е ile bitiyorsa → **-те**: студенти**те**, книги**те**
-а / -я ile bitiyorsa → **-та**: деца**та**, хора**та**, писма**та**
"""),
    T('Sıfatın çoğulu: -и', """
нов → нов**и** студенти · голям → **големи** стаи (я → е) · добър → добр**и** приятели
"""),
    TB('Bu / şu', ['', 'eril', 'dişil', 'nötr', 'çoğul'], [
        ['bu', 'този', 'тази', 'това', 'тези'], ['şu / o', 'онзи', 'онази', 'онова', 'онези']],
        'Bir şeyi tanıtırken cinsiyet fark etmez: Това е … / Това са …'),
    X('Örnekler', [
        ('Този учебник е нов.', 'Bu ders kitabı yeni.'),
        ('Тази зала е голяма.', 'Bu salon büyük.'),
        ('Тези студенти са от Турция.', "Bu öğrenciler Türkiye'den."),
        ('Онази сграда е библиотеката.', 'Şu bina kütüphane.'),
        ('Книгите са на масата.', 'Kitaplar masanın üstünde.'),
        ('Децата са в парка.', 'Çocuklar parkta.'),
    ]),
    T('го, я, ги = onu, onları', """
Türkçedeki **onu / onları** Bulgarcada kısa kelimelerdir ve **fiilin önüne** gelir (fiil cümle başındaysa arkasına):

**го** = onu (eril/nötr) · **я** = onu (dişil) · **ги** = onları

Виждаш ли учебника? — Да, виждам **го**. (Görüyorum onu.)
Търся Мария. Познаваш ли **я**? — Maria'yı arıyorum. Onu tanıyor musun?
Не **ги** виждам. — Onları görmüyorum.
""", 'tr'),
    T('Dikkat: "onu" neyin yerine?', """
"Onu" bir **kitap**sa книга dişil olduğu için **я**: Чета **я**.
"Onu" bir **telefon**sa eril olduğu için **го**: Търся **го**.
Kişi olsun nesne olsun, **ismin cinsiyetine** bakılır.
""", 'warn'),
    T('Yer: на, до, вляво, вдясно', """
**на** = üstünde / -de (açık yerler): на масата, на втория етаж
**до** = yanında: Кафенето е **до** библиотеката.
**вляво** = solda · **вдясно** = sağda
Fiiller: **търся** (aramak), **виждам** (görmek), **харесвам** (beğenmek), **зная / знам** (bilmek)
"""),
  ],
  R('Първи ден в университета', [
      ('Днес е първият ден на Айше в университета.', 'Bugün Ayşe\'nin üniversitedeki ilk günü.'),
      ('Тя търси зала двайсет и три.', 'Yirmi üç numaralı salonu arıyor.'),
      ('— Извинете, знаете ли къде е тази зала?', '— Affedersiniz, bu salonun nerede olduğunu biliyor musunuz?'),
      ('— Да, знам я. На втория етаж е, вдясно.', '— Evet, biliyorum. İkinci katta, sağda.'),
      ('В залата има много студенти.', 'Salonda çok öğrenci var.'),
      ('Студентите са от различни страни.', 'Öğrenciler farklı ülkelerden.'),
      ('Айше вижда едно момиче и го пита: „Ти също ли си нова?“', 'Ayşe bir kız görüyor ve ona soruyor: "Sen de mi yenisin?"'),
      ('Момичето се казва Ана. Тя е от Гърция.', "Kızın adı Ana. O Yunanistan'dan."),
      ('Айше харесва университета.', 'Ayşe üniversiteyi beğeniyor.'),
  ], [
      '**знам я** — я, "salon" (зала, dişil) yerine geçiyor.',
      '**едно момиче … го пита** — момиче nötr olduğu için **го**.',
      '**Студентите** — студенти + те (çoğul tanımlık).',
      '**университета** — nesne, özne değil → kısa tanımlık -а.',
  ], 'Üniversitede ilk gün'),
  [
    QC('книга → ___', ['книги', 'книгове', 'книгата'], 'kitaplar', 'dişil → -и'),
    QC('град → ___', ['градове', 'гради', 'града'], 'şehirler', 'tek heceli eril → -ове'),
    QC('дете → ___', ['деца', 'детета', 'дети'], 'çocuklar', 'düzensiz'),
    QC('Деца___ са в парка.', ['та', 'те', 'то'], 'Çocuklar parkta.', 'деца -а ile biter → -та'),
    QC('___ книга е интересна.', ['Тази', 'Този', 'Това'], 'Bu kitap ilginç.', 'книга dişil → тази'),
    QC('Виждаш ли Мария? — Да, виждам ___.', ['я', 'го', 'ги'], "Maria'yı görüyor musun? — Evet, onu görüyorum.", 'kadın → я'),
    QC('Къде са ключовете? Не ___ виждам.', ['ги', 'го', 'я'], 'Anahtarlar nerede? Onları göremiyorum.', 'çoğul → ги'),
    QT('Bu öğrenciler Türkiye\'den.', ['Тези студенти са от Турция.', 'Тези студента е от Турция.', 'Този студенти са от Турция.'], ''),
    QO('Onu tanıyor musun? (kadını)', 'Познаваш ли я?', ['го']),
  ])
