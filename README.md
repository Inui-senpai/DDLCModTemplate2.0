# Добро пожаловать в Новый клуб модификаций на Python 3!

<p align="center">
  <img src="./game/mod_assets/DDLCModTemplateLogo.png" width=250px/>
</p>

<p align="center">
  <img src=".github/IMAGES/Logos/SmallBronyaLogo.png" width=250px/>
</p>

<p align="center">
   <a href="https://ko-fi.com/K3K22K8SU">
      <img src="https://www.ko-fi.com/img/githubbutton_sm.svg">
   </a>
   <a href="https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases/latest">
      <img src=".github/IMAGES/download.png">
   </a>
</p>

**Новый** мод-шаблон DDLC на Python 3 - это мод-шаблон, созданный Азариэль Дель Карменом (bronya_rand) для **оригинальной** игры «Литературный клуб "Тук-тук!"», который придерживается требований [Руководства по использованию интеллектуальной собственности Team Salvato](http://teamsalvato.com/ip-guidelines/) для фанатских модификаций на движке Ren'Py 8-й версии.

> Помимо всего прочего, [здесь](./CREDITS.md) перечислены все вкладчики мод-шаблона.

### Отказы от ответственности
   - <u>Team Salvato</u>
      > Код/файлы шаблона предназначены для использования в оригинальных фанатских играх по DDLC и модификациях, которые используют ресурсы DDLC и движок Ren'Py. Он не предназначен для использования в проектах, не относящихся к DDLC. Мод-шаблон DDLC никоим образом не связан с Team Salvato.
   - <u>bronya_rand</u>
      > Вы не можете использовать шаблон для создания неофициальных патчеров, исправлений и прочего для DDLC.

### Требования к упоминаниям авторов
Вы должны указать авторство на экране титров вашей модификации и/или в файле `credits.txt`. Ниже расположен пример упоминания, который вы можете использовать:
   > Этот мод появился на свет благодаря мод-шаблону версии 2.0 от bronya_rand: https://github.com/GanstaKingofSA/DDLCModTemplate2.0

Экран авторов включён в игре по умолчанию, и открыть его можно либо через раздел Доп. контента, либо по нажатию на отдельную кнопку, если искомый раздел отключён.

Перечень необязательных, но очень ценных указаний авторства, которые вы можете добавить:
   1. Собственная заставка, на которой имеются логотипы Team Salvato (и/или логотип вашей модификации) и `Брони Рэнд` (найти последний можно [здесь](.github/IMAGES/Logos/)).
   2. Небольшое примечание во время показа Отказа от ответственности о том, что модификация появилась на свет благодаря мод-шаблону от bronya_rand.
   3. Изображение заставки предзагрузки, на котором имеется логотип `Брони Рэнд` (найти его можно [здесь](.github/IMAGES/Logos/)).
   4. Пришлите мне на утверждение свою реализацию упоминания оригинального автора в Discord или Reddit.

### Особенности шаблона
1. Сборка дистрибутивов на движке Ren'Py 8-й версии, соответствующих требованиям Team Salvato, с вставленным дисклеймером во вступлении!
2. Оригинальные RPY-файлы DDLC с пояснениями.
3. Поддержка систем macOS, Linux* и Android**!
   > \* - Пользователи ОС Linux должны запускать вашу модификацию через файл `LinuxLauncher.sh`.

   > \*\* - Только если ваша модификация использует простой код или функционал DDLC/мод-шаблона. Для более сложного кода или функционала, использование которого на мобильных устройствах может быть затруднено, может потребоваться адаптация для корректной работы оного. См. файл *Android Mod Guide.pdf* или посетите сервер DDMC в Дискорде, чтобы получить помощь.
4. Поддержка Xcode! Открыв этот проект в Xcode, вы сможете редактировать, собирать и запускать модификацию, не открывая Лаунчер Ren'Py!
    > Примечание: Вам понадобится изменить значение переменной `RENPY_TOOL` и директорию пакета приложения Ren'Py в целевой схеме Xcode. [Подробнее &rsaquo;](XCODE.md)
5. Режим «Без цензуры» и Режим летсплейщика! - Предоставьте возможность показать в игре более "чувствительный" контент и скройте реальную информацию игрока во время стриминга/записи!
6. Автоматическое раскрашивание интерфейса и разноцветные кнопки меню! - Раскрасьте интерфейс и/или кнопки меню в самой игре так, как вашей душе угодно, никоим образом не изменяя сами ресурсы!
7. Подробное руководство по мини-игре по написанию стихотворения от Terra!
8. Поддержка NVL, спасибо Yagamirai01!
9. Патчи для некоторых версий Ren'Py и функционала систем Windows.
10. Теперь можно использовать код, написанный под Python 3!
11. Динамическое супер-разрешение/Динамические супер-позиции (DSR/DSP) и пользовательские разрешения! - Увеличивайте позиции и/или свои ресурсы ещё больше, чем обычно, и отображайте контент DDLC в различных разрешениях экрана. Мод-шаблон DDLC теперь является шаблоном, поддерживающим абсолютно любые разрешения экрана!
12. Смена имени игрока! - Вы опечатались при вводе или просто хотите изменить имя? Теперь вы можете сделать это с невероятной лёгкостью!
13. Новые консоль Моники и Реакции на стихотворения! - Наслаждайтесь простой консолью, в которую можно ввести команды, а также более понятными и простыми реакциями на стихи!

Помимо вышеперечисленных базовых функций, данный шаблон идёт вместе с такими дополнительными функциями, которые вы можете использовать:
- **[БЕТА]** Поддержка местоимений! - Дайте возможность игрокам выбрать подходящее для них местоимение!
    > См. файл *mod_extras/pronouns.rpy* в папке `game`, чтобы ознакомиться с примером использования этой функции.
- Улучшенный Синий экран смерти! - С лёгкостью создавайте свой внутриигровой Синий экран смерти на любой ОС!
- Меню Галереи и меню Достижений! - Дайте игрокам возможность посмотреть внутри игры, какую работу вы проделали, а также заработать достижения, играя в вашу модификацию!
- **[БЕТА]** Игровая активность в Дискорде!

> Чтобы получить этот набор функций, скачайте файл `DDLCModTemplate-X.X.X-Extras.zip` вместе с основной игрой.

### Возвращённые функции
1. Призрачное меню (жуткая пасхалка от Дэна).
2. Скрипт убийства Сайори (запускается, если файл персонажа Сайори был удалён перед запуском игры).
3. Скрипт убийства Моники (запускается, если файл персонажа Моники был удалён перед запуском игры).
4. Особые стихотворения (случайные стихи, появляющиеся во втором акте DDLC) <u>[были улучшены!]</u>.

### Начало работы
Следуйте шагам, приведённым [здесь](https://ganstakingofsa.github.io/information/guides/Installing-the-Mod-Template-Recent.html), чтобы установить мод-шаблон.
> Как только вы закончите писать свой скрипт, выберите *Построить дистрибутивы*. Снимите флажки со всех вариантов и отметьте только `DDLC-совместимый мод на Ren'Py 8`, после чего нажмите на <u>Построить</u>. Это создаст кроссплатформенный .ZIP-архив, имеющий *Renpy8-DDLCMod* в названии, с файлами вашей модификации.

### Начало работы для портирования/моддинга на Android
Прочтите файл [*Руководство по моддингу DDLC на Android*](./Documentation/Android%20Mod%20Guide.pdf) чтобы узнать больше о том, как заставить вашу модификацию работать на ОС Android.

Авторское право © 2019-настоящее время Азариэль Дель Кармен (bronya_rand). Все права защищены.

Игра «Литературный клуб "Тук-тук!"» и её составляющие являются собственностью Team Salvato (Dan Salvato LLC). Авторское право © 2017 Team Salvato. Все права защищены.

Перевод оригинального сценария (с рядом мелких правок) и прочие оптимизации для кроссплатформенности позаимствованы из русификатора от Энтузиасты Team.

### Текущая схема перевода
- Перевод скриптов: по мере возможности;
- Если коммитов "позади" меньше 100: производится дробление и объединение (Squash and merge);
- Если коммитов "позади" больше 100: производится переписывание (Rebase).
