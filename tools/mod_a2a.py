# -*- coding: utf-8 -*-
from lib import T, TB, X, R, QC, QT, QO, M

# =====================================================================
M8 = M('a2-08', 'A2', '8. ders', 'Öğle yemeği: мога, трябва да, sıfat uyumu', 'На обяд',
  '"Yapabilmek" ve "gerekmek" yapılarını, ходя / играя / пея fiillerini ve durum sıfatlarını öğreneceksin.',
  [
    TB('Yeni fiiller', ['Kişi', 'ходя (gitmek, yürümek)', 'играя (oynamak)', 'пея (şarkı söylemek)'], [
        ['аз', 'ходя', 'играя', 'пея'], ['ти', 'ходиш', 'играеш', 'пееш'], ['той/тя', 'ходи', 'играе', 'пее'],
        ['ние', 'ходим', 'играем', 'пеем'], ['вие', 'ходите', 'играете', 'пеете'], ['те', 'ходят', 'играят', 'пеят']],
        'ходя = düzenli gitmek (Ходя на фитнес), отивам = şu an/bir kez gitmek (Отивам на фитнес).'),
    TB('мога — -ebilmek', ['Kişi', 'мога', 'Türkçe'], [
        ['аз', 'мога', 'yapabilirim'], ['ти', 'можеш', 'yapabilirsin'], ['той/тя', 'може', 'yapabilir'],
        ['ние', 'можем', 'yapabiliriz'], ['вие', 'можете', 'yapabilirsiniz'], ['те', 'могат', 'yapabilirler']],
        'г → ж değişir: мога, можеш … ama те могат.'),
    T('мога да / трябва да', """
Türkçede "-ebilmek" ve "-meli" ekleri Bulgarcada ayrı kelimelerdir ve **да** ile bağlanır:

**Мога да** плувам. — Yüzebilirim.
**Не мога да** дойда. — Gelemem.
**Трябва да** уча. — Çalışmalıyım. / Çalışmam lazım.
**Трябва ли да** чакам? — Beklemem gerekiyor mu?

⭐ **трябва** hiç değişmez: аз трябва да, ти трябва да, те трябва да…
Değişen, да'dan sonraki fiildir: Трябва да **уча** (ben) · Трябва да **учиш** (sen).
""", 'tr'),
    X('Örnekler', [
        ('Можеш ли да готвиш? — Мога малко.', 'Yemek yapabilir misin? — Biraz yapabilirim.'),
        ('Не мога да ям лук.', 'Soğan yiyemem.'),
        ('Трябва да пиеш повече вода.', 'Daha çok su içmelisin.'),
        ('Може ли менюто, моля?', 'Menüyü alabilir miyim lütfen?'),
        ('Децата играят в двора.', 'Çocuklar avluda oynuyor.'),
        ('Всяка събота ходим на пазар.', 'Her cumartesi pazara gideriz.'),
    ]),
    T('Sıfat isimle aynı "kıyafeti" giyer', """
Sıfat ismin cinsiyet ve sayısına uyar:
вкусен сандвич · вкусна супа · вкусно пиле · вкусни ястия
печен картоф · печена риба · печено пиле
"""),
    TB('Durum sıfatları', ['eril', 'dişil', 'çoğul', 'Türkçe'], [
        ['гладен', 'гладна', 'гладни', 'aç'], ['жаден', 'жадна', 'жадни', 'susamış'],
        ['уморен', 'уморена', 'уморени', 'yorgun'], ['доволен', 'доволна', 'доволни', 'memnun'],
        ['зает', 'заета', 'заети', 'meşgul / dolu'], ['свободен', 'свободна', 'свободни', 'boş / müsait']],
        'Kadın konuşuyorsa: Гладна съм. Erkek: Гладен съм. (-ен\'deki е düşer: гладен → гладна)'),
    T('Dikkat: "Ben açım" ama "Benim karnım…" değil', """
Türkçe "Acıktım" → Bulgarca sıfatla: **Гладен съм.**
"Susadım" → **Жаден съм.** · "Yoruldum" → **Уморен съм.**
Türkçede geçmiş zaman kullansak da Bulgarcada **şimdiki** durum söylenir.
""", 'warn'),
  ],
  R('Обяд в ресторанта', [
      ('Днес Елена и колегите ѝ обядват в ресторант.', 'Bugün Elena ve iş arkadaşları bir restoranda öğle yemeği yiyor.'),
      ('Всички са гладни и малко уморени.', 'Hepsi aç ve biraz yorgun.'),
      ('— Може ли менюто, моля?', '— Menüyü alabilir miyim lütfen?'),
      ('Елена иска пилешка супа и салата.', 'Elena tavuk çorbası ve salata istiyor.'),
      ('Стоян не може да яде месо и поръчва печена риба.', 'Stoyan et yiyemiyor ve fırında balık sipariş ediyor.'),
      ('Ресторантът е пълен, всички маси са заети.', 'Restoran dolu, bütün masalar dolu.'),
      ('Храната е много вкусна.', 'Yemekler çok lezzetli.'),
      ('След обяда те трябва да се върнат на работа.', 'Öğle yemeğinden sonra işe dönmeleri gerekiyor.'),
      ('Всички са доволни.', 'Herkes memnun.'),
  ], [
      '**колегите ѝ** — "onun iş arkadaşları": ѝ = onun (kadın). 9. derste.',
      '**не може да яде** — "yiyemiyor": може + да + yiyen kişinin fiili.',
      '**всички маси са заети** — çoğul isim, çoğul sıfat: заети.',
      '**трябва да се върнат** — трябва değişmez; върнат = "onlar dönsün".',
  ], 'Restoranda öğle yemeği'),
  [
    QC('Ти ___ ли да плуваш?', ['можеш', 'мога', 'могат'], 'Yüzebilir misin?', 'ти → можеш'),
    QC('Те не ___ да дойдат.', ['могат', 'можат', 'можем'], 'Gelemezler.', 'те → могат'),
    QC('Утре ___ да работя.', ['трябва', 'трябвам', 'трябваш'], 'Yarın çalışmam lazım.', 'трябва değişmez'),
    QC('Трябва да ___ повече вода.', ['пиеш', 'пия', 'пие'], 'Daha çok su içmelisin.', 'sana söylüyoruz → пиеш'),
    QC('Гладн___ съм.', ['а', 'и', 'о'], 'Acıktım. (kadın konuşuyor)', 'kadın → гладна'),
    QC('Супата е много вкусн___.', ['а', 'о', 'и'], 'Çorba çok lezzetli.', 'супа dişil'),
    QC('Децата ___ в парка.', ['играят', 'играе', 'играем'], 'Çocuklar parkta oynuyor.', 'деца = те → играят'),
    QT('Gelemem.', ['Не мога да дойда.', 'Мога не да дойда.', 'Не можеш да дойда.'], ''),
    QO('Menüyü alabilir miyim lütfen?', 'Може ли менюто, моля?', ['мога']),
  ])

# =====================================================================
M9 = M('a2-09', 'A2', '9. ders', 'Kiralık daire: belirli sıfat, karşılaştırma, iyelik', 'Апартамент под наем',
  'Sıfatı belirli yapmayı, "daha" ve "en" demeyi, benim/senin gibi iyelik biçimlerini ve yer edatlarını öğreneceksin.',
  [
    T('Tanımlık sıfata gelir', """
Sıfat + isim grubunda tanımlık **ilk kelimeye**, yani sıfata eklenir. İsim çıplak kalır:
голям**ата** стая (büyük oda) — ❌ голяма стаята
нов**ото** легло · стар**ите** мебели
"""),
    TB('Belirli sıfat', ['', 'belirsiz', 'belirli'], [
        ['eril (özne)', 'нов апартамент', 'новият апартамент'], ['eril (diğer)', 'нов апартамент', 'новия апартамент'],
        ['dişil', 'голяма кухня', 'голямата кухня'], ['nötr', 'малко легло', 'малкото легло'],
        ['çoğul', 'светли стаи', 'светлите стаи']],
        'Eril: -ият (özne) / -ия (diğer) — isimdeki -ът / -а kuralının aynısı.'),
    T('Karşılaştırma: по- ve най-', """
Türkçedeki **daha** = **по-**, **en** = **най-** (kısa çizgiyle yazılır!)
голям → **по-голям** (daha büyük) → **най-голям** (en büyük)
**-den** = **от**: Тази стая е **по-голяма от** онази. — Bu oda şundan daha büyük.

Zarflarda da aynı: добре → **по-добре** → **най-добре**
⚠️ "Daha çok" = **повече** (❌ по-много)
""", 'tr'),
    X('Karşılaştırma örnekleri', [
        ('Кухнята е по-малка от хола.', 'Mutfak salondan daha küçük.'),
        ('Това е най-хубавата стая.', 'Bu en güzel oda.'),
        ('В центъра е по-скъпо.', 'Merkezde daha pahalı.'),
        ('Този квартал е по-тих.', 'Bu semt daha sakin.'),
    ]),
    T('İyelik: Türkçe ek gibi ismin arkasına!', """
Türkçede sahiplik bir ektir: ev**im**, ev**in**. Bulgarcada **ismin arkasına kısa bir kelime** gelir ve isim tanımlıklı olur:
стая**та ми** = odam · стая**та ти** = odan · стая**та му** = (erkeğin) odası · стая**та ѝ** = (kadının) odası
стая**та ни** = odamız · стая**та ви** = odanız · стая**та им** = odaları

Aile kelimeleri tekilken tanımlık almaz: **майка ми** (annem), **брат ми** (kardeşim).
""", 'tr'),
    TB('Kısa iyelik', ['Sahip', 'Kelime', 'Örnek'], [
        ['benim', 'ми', 'колата ми'], ['senin', 'ти', 'колата ти'], ['onun (erkek)', 'му', 'колата му'],
        ['onun (kadın)', 'ѝ', 'колата ѝ'], ['bizim', 'ни', 'колата ни'], ['sizin', 'ви', 'колата ви'],
        ['onların', 'им', 'колата им']]),
    T('Yer edatları', """
**в** içinde · **на** üstünde · **под** altında · **над** üstünde (değmeden) · **до** yanında
**пред** önünde · **зад** arkasında · **между** arasında · **срещу** karşısında
Котката е **под** леглото. · Лампата е **над** масата. · Банката е **между** аптеката и пощата.
"""),
    T('гледам ↔ виждам, слушам ↔ чувам', """
**гледам** = bakmak, izlemek (bilinçli) — **виждам** = görmek
**слушам** = dinlemek — **чувам** = duymak
Гледам телевизия. — Televizyon izliyorum. · Виждаш ли морето? — Denizi görüyor musun?
Стаята **гледа към** парка. — Oda parka bakıyor (manzarası park).
"""),
    TB('живея — yaşamak', ['Kişi', 'живея'], [
        ['аз', 'живея'], ['ти', 'живееш'], ['той/тя', 'живее'], ['ние', 'живеем'], ['вие', 'живеете'], ['те', 'живеят']]),
  ],
  R('Търся квартира', [
      ('Али търси апартамент под наем в София.', "Ali Sofya'da kiralık bir daire arıyor."),
      ('Сега живее при приятел, но стаята му е много малка.', 'Şu an bir arkadaşının yanında yaşıyor ama arkadaşının odası çok küçük.'),
      ('Агентът показва два апартамента.', 'Emlakçı iki daire gösteriyor.'),
      ('Първият е в центъра, близо до метрото.', 'Birincisi merkezde, metroya yakın.'),
      ('Той е по-скъп, но е светъл и уютен.', 'Daha pahalı ama aydınlık ve sıcak.'),
      ('Вторият е в тих квартал, далече от центъра.', 'İkincisi merkezden uzak, sakin bir semtte.'),
      ('Неговата кухня е по-голяма, а холът гледа към парка.', 'Onun mutfağı daha büyük, salonu da parka bakıyor.'),
      ('Али мисли, че вторият е най-добрият.', 'Ali ikincisinin en iyisi olduğunu düşünüyor.'),
      ('Той харесва тишината и голямата кухня.', 'Sessizliği ve büyük mutfağı seviyor.'),
  ], [
      '**стаята му** — "(arkadaşın) odası": му = onun (erkek).',
      '**Първият / Вторият** — sıra sayısı belirli: "birincisi, ikincisi".',
      '**по-скъп** — "daha pahalı"; по- kısa çizgiyle.',
      '**най-добрият** — en + iyi + belirli: "en iyisi".',
  ], 'Ev arıyorum'),
  [
    QC('___ стая е светла.', ['Голямата', 'Голяма', 'Голямото'], 'Büyük oda aydınlık.', 'Tanımlık sıfata gelir: голямата'),
    QC('___ апартамент е в центъра.', ['Новият', 'Новия', 'Новата'], 'Yeni daire merkezde.', 'Eril özne → -ият'),
    QC('Тази стая е по-голяма ___ онази.', ['от', 'на', 'с'], 'Bu oda şundan daha büyük.', '-den = от'),
    QC('Това е ___ хубавият ден!', ['най-', 'по-', 'много'], 'Bu en güzel gün!', 'en = най-'),
    QC('Колата ___ е нова.', ['ѝ', 'му', 'им'], 'Onun (kadının) arabası yeni.', 'kadının → ѝ'),
    QC('Котката е ___ леглото.', ['под', 'над', 'между'], 'Kedi yatağın altında.', 'altında = под'),
    QC('Къде ___? — В Пловдив.', ['живееш', 'живеш', 'живея'], "Nerede yaşıyorsun? — Plovdiv'de.", 'живея → живееш'),
    QT('Annem doktor.', ['Майка ми е лекарка.', 'Майката ми е лекарка.', 'Ми майка е лекарка.'], 'Aile kelimesi tekil → tanımlıksız'),
    QO('Bu oda daha sakin.', 'Тази стая е по-тиха.', ['най-']),
  ])

# =====================================================================
M10 = M('a2-10', 'A2', '10. ders', 'Aile: zamirlerin yeri, „който“ ve aktarma', 'Семейство',
  'ме, те, го gibi zamirlerin cümledeki yerini, "-an/-en" anlamı veren който\'yi ve başkasının sözünü aktarmayı öğreneceksin.',
  [
    TB('Kısa nesne zamirleri', ['Kişi', 'Kelime', 'Türkçe', 'Örnek'], [
        ['аз', 'ме', 'beni', 'Познаваш ли ме?'], ['ти', 'те', 'seni', 'Обичам те.'],
        ['той / то', 'го', 'onu', 'Не го виждам.'], ['тя', 'я', 'onu', 'Чакам я.'],
        ['ние', 'ни', 'bizi', 'Канят ни на гости.'], ['вие', 'ви', 'sizi', 'Каня ви!'], ['те', 'ги', 'onları', 'Познавам ги.']]),
    T('Yer kuralı', """
Bu kısa kelimeler cümlenin **başına gelemez**:
• Önünde bir kelime varsa → **fiilin önüne**: Аз **те** обичам. · Не **го** познавам. · Утре **ще ги** видя.
• Fiil cümle başındaysa → **fiilin arkasına**: Обичам **те**. · Чакам **я**.
• Soruda ли ile: Познаваш **ли ме**?
""", 'key'),
    T('който — "-an / -en"', """
Türkçede "**konuşan** kadın" dediğimiz yapı Bulgarcada ismin **arkasından** gelen bir cümleyle kurulur:
жената, **която** говори — konuşan kadın
мъжът, **който** чака — bekleyen adam
детето, **което** спи — uyuyan çocuk
хората, **които** живеят тук — burada yaşayan insanlar

който / която / което / които — önündeki ismin cinsiyetine göre seçilir.
""", 'tr'),
    T('Söz aktarma: казва, че… / пита дали…', """
Türkçede "geleceğ**ini** söylüyor" deriz. Bulgarcada **че** (ki) ile cümle olduğu gibi devam eder:
Тя казва: „Уморена съм.“ → Тя казва, **че** е уморена. — Yorgun olduğunu söylüyor.

Soru aktarma: soru kelimesi korunur; evet/hayır sorusunda **дали** (-ip -mediğini) gelir:
Той пита: „Къде живееш?“ → Той пита **къде** живея.
Той пита: „Студент ли си?“ → Той пита **дали** съм студент.
"""),
    TB('Aile', ['Bulgarca', 'Türkçe', 'Bulgarca', 'Türkçe'], [
        ['майка', 'anne', 'баща', 'baba'], ['сестра', 'kız kardeş', 'брат', 'erkek kardeş'],
        ['дъщеря', 'kız evlat', 'син', 'oğul'], ['баба', 'nine', 'дядо', 'dede'],
        ['леля', 'teyze / hala', 'чичо', 'amca'], ['съпруга', 'eş (kadın)', 'съпруг', 'eş (erkek)']],
        'Benim annem = майка ми · Onun babası = баща му / баща ѝ'),
    X('Örnekler', [
        ('Познаваш ли сестра ми?', 'Kız kardeşimi tanıyor misin?'),
        ('Аз не я познавам.', 'Onu tanımıyorum.'),
        ('Момчето, което играе футбол, е брат ми.', 'Futbol oynayan çocuk benim kardeşim.'),
        ('Мама казва, че обядът е готов.', 'Annem öğle yemeğinin hazır olduğunu söylüyor.'),
        ('Баба пита дали сме гладни.', 'Ninem aç olup olmadığımızı soruyor.'),
        ('Каним ви на гости в събота.', 'Sizi cumartesi misafirliğe davet ediyoruz.'),
    ]),
  ],
  R('Семейство Димитрови', [
      ('Семейство Димитрови живее в Бургас.', "Dimitrov ailesi Burgaz'da yaşıyor."),
      ('Бащата, Георги, е инженер, който работи в пристанището.', 'Baba Georgi, limanda çalışan bir mühendis.'),
      ('Майката, Радка, е учителка.', 'Anne Radka öğretmen.'),
      ('Те имат две деца — Мира и Борис.', 'İki çocukları var — Mira ve Boris.'),
      ('Мира учи в София и рядко идва вкъщи.', "Mira Sofya'da okuyor ve eve nadiren geliyor."),
      ('Борис е малък и много обича футбол.', 'Boris küçük ve futbolu çok seviyor.'),
      ('В неделя баба Мария ги кани на обяд.', 'Pazar günleri Maria nine onları öğle yemeğine davet ediyor.'),
      ('Тя винаги пита дали Мира ще дойде.', 'Her zaman Mira\'nın gelip gelmeyeceğini soruyor.'),
      ('Борис казва, че сестра му е най-добрата!', 'Boris, ablasının en iyisi olduğunu söylüyor!'),
  ], [
      '**инженер, който работи** — "çalışan mühendis": който eril, инженер eril.',
      '**ги кани** — "onları davet ediyor": ги fiilin önünde, çünkü öncesinde kelime var.',
      '**пита дали Мира ще дойде** — evet/hayır sorusu aktarılıyor → дали.',
      '**сестра му** — aile kelimesi, tekil → tanımlıksız.',
  ], 'Dimitrov ailesi'),
  [
    QC('Обичам ___.', ['те', 'ти', 'теб'], 'Seni seviyorum.', 'seni = те'),
    QC('Не ___ познавам.', ['го', 'я', 'му'], 'Onu (erkeği) tanımıyorum.', 'erkek → го'),
    QC('Жената, ___ говори, е учителка.', ['която', 'който', 'които'], 'Konuşan kadın öğretmen.', 'жена dişil → която'),
    QC('Хората, ___ живеят тук, са добри.', ['които', 'който', 'което'], 'Burada yaşayan insanlar iyi.', 'çoğul → които'),
    QC('Тя казва, ___ е уморена.', ['че', 'дали', 'ли'], 'Yorgun olduğunu söylüyor.', 'aktarma → че'),
    QC('Той пита ___ съм студент.', ['дали', 'че', 'който'], 'Öğrenci olup olmadığımı soruyor.', 'evet/hayır sorusu → дали'),
    QT('Beni tanıyor musun?', ['Познаваш ли ме?', 'Ме познаваш ли?', 'Познаваш ме ли?'], 'ли + ме sırası'),
    QO('Seni bekliyorum.', 'Чакам те.', ['ти']),
  ])

# =====================================================================
M11 = M('a2-11', 'A2', '11. ders', 'Pazarda: „bana / sana“, emir kipi, fiil çiftleri', 'На пазар',
  'ми, ти, му gibi "bana, sana" zamirlerini, emir kipini ve fiillerin iki görünüşünü (купувам / купя) öğreneceksin.',
  [
    TB('Kısa dolaylı zamirler — "bana, sana…"', ['Kişi', 'Kelime', 'Türkçe', 'Örnek'], [
        ['аз', 'ми', 'bana', 'Дай ми!'], ['ти', 'ти', 'sana', 'Казвам ти.'], ['той', 'му', 'ona (erkek)', 'Помагам му.'],
        ['тя', 'ѝ', 'ona (kadın)', 'Давам ѝ цветя.'], ['ние', 'ни', 'bize', 'Покажете ни!'],
        ['вие', 'ви', 'size', 'Благодаря ви!'], ['те', 'им', 'onlara', 'Отговарям им.']],
        'Bunlar iyelikle aynı kelimeler (колата ми = arabam). Fiil yanındaysa "bana", isim yanındaysa "benim".'),
    T('Hangi fiiller "-e" ister?', """
Türkçede "**ona** yardım ediyorum" dediğimiz gibi Bulgarcada da bu fiiller dolaylı zamir alır:
помагам **на** някого (birine yardım etmek) · давам **на** (vermek) · казвам **на** (söylemek) · благодаря **на** (teşekkür etmek) · отговарям **на** (cevap vermek)
Помагам **на** Мария → Помагам **ѝ**.
"""),
    T('Emir kipi', """
Türkçedeki **oku! / okuyun!** gibi:
е- ve и-grubu: kök + **-и / -ете**: пиша → **пиши! / пишете!** · уча → **учи!**
а/я-grubu (-м): kök + **-й / -йте**: чакам → **чакай! / чакайте!** · слушам → **слушай!**
Düzensiz: **ела! / елате!** (gel / gelin) · **дай!** (ver) · **виж!** (bak)

Zamir emrin **arkasına** gelir: **Дай ми** хляб! · **Кажи ми!** · **Покажете ни!**
""", 'tr'),
    T('Fiilin iki yüzü: süreç ve tek sefer', """
Bulgarcada fiillerin çoğunun **iki hâli** vardır. Türkçede bunu bağlamdan anlarız:
• **купувам** — alırım / alıyorum (süreç, alışkanlık)
• **купя** — alayım, alıp bitireyim (tek sefer, sonuçlu)

Ne zaman hangisi?
✓ "her gün, genellikle, bazen" → süreç: **Всеки ден купувам** хляб.
✓ "да / ще" sonrasında tek iş → tek sefer: **Искам да купя** хляб. · **Трябва да платя.**
""", 'key'),
    TB('Önemli çiftler', ['Süreç (несвършен)', 'Tek sefer (свършен)', 'Türkçe'], [
        ['купувам', 'купя', 'satın almak'], ['вземам', 'взема', 'almak'], ['плащам', 'платя', 'ödemek'],
        ['слагам', 'сложа', 'koymak'], ['помагам', 'помогна', 'yardım etmek'], ['давам', 'дам', 'vermek']]),
    X('Pazarda', [
        ('Дайте ми един килограм домати, моля.', 'Bana bir kilo domates verin lütfen.'),
        ('Колко струват ябълките?', 'Elmalar ne kadar?'),
        ('Искам да купя малко сирене.', 'Biraz peynir almak istiyorum.'),
        ('Сложете ги в торбичка, моля.', 'Onları poşete koyun lütfen.'),
        ('Мога ли да платя с карта?', 'Kartla ödeyebilir miyim?'),
        ('Благодаря ви! Довиждане!', 'Teşekkür ederim! Hoşça kalın!'),
    ]),
    T('İnsan sayarken: двама, трима', """
Erkek (ya da karışık) insanlar için özel sayılar: **двама** (2), **трима** (3), **четирима** (4), **петима** (5)
**двама** продавачи · **трима** приятели — kadınlar için normal: две продавачки
"""),
    T('когато, където', """
**когато** = -dığında: **Когато** ходя на пазар, купувам плодове. — Pazara gittiğimde meyve alırım.
**където** = -diği yer: Магазинът, **където** работи, е голям. — Çalıştığı mağaza büyük.
"""),
  ],
  R('Съботен пазар', [
      ('В събота Айше ходи на пазара в квартала.', 'Cumartesi günü Ayşe semt pazarına gidiyor.'),
      ('Там има много сергии с плодове и зеленчуци.', 'Orada meyve ve sebze dolu birçok tezgâh var.'),
      ('— Добър ден! Дайте ми два килограма картофи, моля.', '— İyi günler! Bana iki kilo patates verin lütfen.'),
      ('— Заповядайте! Искате ли и домати? Днес са много хубави.', '— Buyurun! Domates de ister misiniz? Bugün çok güzeller.'),
      ('— Да, дайте ми един килограм.', '— Evet, bir kilo verin.'),
      ('Продавачът слага доматите в торбичка.', 'Satıcı domatesleri poşete koyuyor.'),
      ('Когато Айше иска да плати, вижда, че няма пари в брой.', 'Ayşe ödemek istediğinde nakit parası olmadığını görüyor.'),
      ('— Може ли с карта? — Разбира се!', '— Kartla olur mu? — Tabii ki!'),
      ('Айше му благодари и тръгва към къщи.', 'Ayşe ona teşekkür ediyor ve eve doğru yola çıkıyor.'),
  ], [
      '**Дайте ми** — kibar emir (Дай → Дайте) + ми "bana".',
      '**два килограма** — eril isim + sayı → sayma biçimi.',
      '**иска да плати** — да\'dan sonra tek seferlik hâl: платя → плати (o).',
      '**му благодари** — "ona teşekkür ediyor": благодаря на + му.',
  ], 'Cumartesi pazarı'),
  [
    QC('Дай ___ хляб, моля!', ['ми', 'ме', 'аз'], 'Bana ekmek ver lütfen!', 'bana = ми'),
    QC('Помагам ___.', ['ѝ', 'я', 'му'], 'Ona (Maria\'ya) yardım ediyorum.', 'kadına → ѝ (dolaylı)'),
    QC('Благодаря ___!', ['ви', 'ни', 'ги'], 'Size teşekkür ederim!', 'size = ви'),
    QC('___ тук!', ['Ела', 'Идвам', 'Елате'], 'Gel buraya! (sana)', 'sen → ела'),
    QC('Искам да ___ хляб.', ['купя', 'купувам', 'купи'], 'Ekmek almak istiyorum.', 'да + tek sefer → купя'),
    QC('Всеки ден ___ хляб.', ['купувам', 'купя', 'купи'], 'Her gün ekmek alırım.', 'her gün → süreç'),
    QC('___ приятели', ['трима', 'три', 'трети'], 'üç (erkek) arkadaş', 'erkekler → трима'),
    QT('Kartla ödeyebilir miyim?', ['Мога ли да платя с карта?', 'Мога ли да плащам с карта?', 'Мога да платя ли с карта?'], 'Tek bir ödeme → платя'),
    QO('Bana söyle!', 'Кажи ми!', ['ме']),
  ])
