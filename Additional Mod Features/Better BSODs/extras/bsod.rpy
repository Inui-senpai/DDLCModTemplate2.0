# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# bsod.rpy
# Этот файл содержит код экрана, который отображает ложный Синий экран смерти.

init python:
    cursor = 0
    purple = False

    def fakePercent(st, at, winver):

        if int(0 + (st * 5)) < 100:
            percent = int(0 + (st * 5))
        else:
            percent = 100

        if winver == 8:
            d = Text(__("автоматически выполнена перезагрузка. (выполнено: [percent]%)\n"), style="bsod_win8_text", size=28)
        else:
            d = Text(__("[percent]% завершено"), style="bsod_win10_text", line_leading=20)

        if percent < 100:
            return d, renpy.random.randint(1, 3)
        else:
            return d, None

    def constantCursor(st, at):
        global cursor
        if cursor == 0:
            cursor = 1
            return Text("  _", style="bsod_linux_text"), 0.3
        else:
            cursor = 0
            return Text("   ", style="bsod_linux_text"), 0.3

    def fake_macos_bigsur_panic(st, at):
        global purple

        if purple:
            purple = False
            return Solid("#ff41ff"), 0.15
        else:
            purple = True
            return Solid("#000"), 2


## Синий экран смерти ###########################################################
##
## Этот экран используется для мимикрии экрана сообщения об ошибке на всех платформах
## (на мобильных устройствах будет использоваться экран паники ядра Linux).
##
## Синтаксис:
##     bsodCode – Желаемый код ошибки. Если ничего не передано, будет подставлено
##                DDLC_ESCAPE_PLAN_FAILED.
##     bsodFile (только Windows 7) – Имя файла, из-за которого якобы случился сбой.
##                Если ничего не передано, будет подставлено libGLESv2.dll.
##     rsod (только Windows 11) – Делает Синий экран смерти Красным.
##               По умолчанию – False.
##     hexcodeError (только Windows 11 10.0.26100 и выше) – HEX-код ошибки.
##
## Примеры:
##     show screen bsod("DOKI_DOKI", "renpy32.dll", False) 
##     show screen bsod("EILEEN_EXCEPTION_NOT_HANDLED", rsod=True) 
##     show screen bsod("NOT_BRONYA_DUMPLING_FRIENDLY", hexcodeError="0x4A")
screen bsod(bsodCode="DDLC_ESCAPE_PLAN_FAILED", bsodFile="libGLESv2.dll", rsod=False, hexcodeError="0xFA"):

    layer "master"

    if renpy.windows:

        python:
            # Получаем версию Windows
            os = get_windows_version()

            # Проверяем, что наш HEX-код шестнадцатеричный
            if hexcodeError != "":
                try:
                    int(hexcodeError, 16)

                    if not hexcodeError.startswith("0x"):
                        hexcodeError = f"0x{hexcodeError}"

                    # Обрезаем до 2 байт (0xFF)
                    hexcodeError = hexcodeError[:4]
                except ValueError:
                    hexcodeError = "0xFA" # HEX-код ошибки по умолчанию
            else:
                hexcodeError = "0xFA" # HEX-код ошибки по умолчанию

        if os <= (6, 1): # Windows 7 и ниже
            add Solid("#000082")

            vbox:
                style_prefix "bsod_win7"

                text _("Во время работы Windows произошёл сбой, система принудительно\nзавершила работу для предотвращения дальнейшего урона компьютеру.")
                text _("Вероятно, сбой был вызван этим файлом: [bsodFile!u]")
                text bsodCode.upper()
                text _("Если вы впервые увидели это сообщение об ошибке, перезагрузите компьютер.\nПри повторном появлении данного сообщения выполните следующие действия:")
                text _("Убедитесь, что новое оборудование и ПО правильно установлены. Если оные\nбыли установлены впервые, обратитесь к их изготовителям за необходимыми\nобновлениями.")
                text _("Если проблема не была устранена, удалите или отключите недавно\nустановленное оборудование или ПО. Отключите кэширование и использование\nтеневой памяти в BIOS компьютера. Если для удаления или отключения\nкомпонентов потребуется загрузить компьютер в Безопасном режиме,\nперезагрузите его, нажмите клавишу F8 для входа в меню Особых вариантов\nзагрузки и выберите пункт Безопасный режим.")
                text _("Техническая информация:")
                text "*** STOP: 0x00000051 (OXFD69420, 0x00000005, OXFBF92317, 0x00000000)\n"
                text _("*** [bsodFile!u]  -  Адрес FBF92317, основа FBF102721, метка времени 3d6dd67c")

        elif os in [(6, 2), (6, 3)]: # Windows 8 и 8.1
            add Solid("#1273aa")

            vbox:
                style_prefix "bsod_win8"
                xalign 0.5
                yalign 0.4

                text ":(" style "bsod_win8_sad_text"
                text _("На вашем ПК возникла проблема, и его необходимо перезагрузить.")
                text _("Мы лишь собираем некоторые сведения об ошибке, а затем будет")
                add DynamicDisplayable(fakePercent, 8)
                text _("При желании вы можете найти в Интернете информацию по этому коду ошибки: [bsodCode!u]") style "bsod_win8_sub_text"

        elif os == (10, 0) and os < (10, 0, 26100): # Windows 10, 11 (младше 10.0.26100) и RSOD / Неизвестно
            if rsod:
                add Solid("#d40e0eff")
                python:
                    blackCol = "#f00"

            else:
                add Solid("#0078d7")
                python:
                    blackCol = "#0078d7"

            vbox:
                style_prefix "bsod_win10"
                xalign 0.2
                yalign 0.4

                text ":(" style "bsod_win10_sad_text"

                if os == "10":
                    python:
                        bsodQRSize = 100

                    text _("На вашем ПК возникла проблема, и его необходимо перезагрузить.")
                    text _("Мы лишь собираем некоторые сведения об ошибке, а затем будет")
                    text _("автоматически выполнена перезагрузка.")

                else:
                    python:
                        bsodQRSize = 150

                    text _("На вашем устройстве возникла проблема, и его необходимо перезагрузить.")
                    text _("Мы лишь собираем некоторые сведения об ошибке, а затем будет")
                    text _("автоматически выполнена перезагрузка.")

                add DynamicDisplayable(fakePercent, 10)

                hbox:
                    vbox:
                        text "" line_leading -3
                        add Transform("mod_assets/mod_extra_images/bsod_qr_code.png", matrixcolor=ColorizeMatrix(blackCol, "#fff")) at bsod_qrcode(bsodQRSize)
                    vbox:
                        xpos 0.04
                        vbox:
                            spacing 2
                            text _("Дополнительные сведения об этой проблеме и возможных способах её решения см. на странице") style "bsod_win10_info_text" line_leading 30
                            text "https://www.windows.com/stopcode\n" style "bsod_win10_info_text"
                        null height 3
                        vbox:
                            spacing 4
                            text _("При обращении в службу поддержки предоставьте следующие данные:") style "bsod_win10_sub_text"
                            text _("Код остановки: [bsodCode!u]") style "bsod_win10_sub_text"
                            text _("Что вызвало проблему: [bsodFile!l]") style "bsod_win10_sub_text"

        else: # Windows 11 (10.0.26100 и старше)
            add Solid("#000")

            vbox:
                style_prefix "bsod_win10"
                xalign 0.5
                yalign 0.5

                text _("На вашем устройстве возникла проблема, и его необходимо перезагрузить.")

                vbox:
                    xalign 0.5
                    add DynamicDisplayable(fakePercent, 10)

            vbox:
                style_prefix "bsod_win10"
                xalign 0.5
                yalign 0.95

                text _("Код остановки: [bsodCode!u] ([hexcodeError])") style "bsod_win10_info_text"


    elif renpy.macintosh:

        python:
            release = get_macos_version()

        if release <= (10, 10): # OS X Yosemite и младше
            add Solid("#222")

            add Transform("mod_assets/DDLCModTemplateLogo.png", matrixcolor=SaturationMatrix(0) * BrightnessMatrix(-0.36)) at bsod_qrcode(440) xalign 0.5 yalign 0.54
            vbox:

                style_prefix "bsod_osx"
                xalign 0.53
                yalign 0.51

                text _("Компьютер был перезагружен из-за возникшего сбоя. Нажмите любую клавишу\n")
                text _("или подождите пару секунд, чтобы продолжить запуск.") line_spacing 25
                text "Votre ordinateur a redémarré en raison d'un problème. Pour poursuivre\n"
                text "le démarrage, appuyez sur une touche ou patientez quelques secondes." line_spacing 25
                text "El ordenador se ha reiniciado debido a un problema. Para continuar con\n"
                text "el arranque, pulse cualquier tecla o espere unos segundos." line_spacing 25
                text "Ihr Computer wurde aufgrund eines Problems neu gestartet. Drücken\n"
                text "Sie zum Fortfahren eine Taste oder warten Sie einige Sekunden." line_spacing 25

                # Из-за ограничений шрифта японский и китайский языки не поддерживаются. Если вы используете шрифт,
                # который поддерживает данные языки, раскомментируйте нижеприведённые строки.
                # Мы же используем альтернативные языки (итальянский/нидерландский).

                #text "問題が起きたためコンピュータを再起動しました。このまま起動する場合は、\n"
                #text "いずれかのキーを押すか、数秒間そのままお待ちください。" line_spacing 25
                #text "电脑因出现问题而重新启动。请按一下按键,或等几秒钟以继续启动。"

                text "Il computer è stato riavviato a causa di un problema. Per continuare l'avvio,\n"
                text "premere un tasto o attendere qualche secondo." line_spacing 25
                text "De computer is opnieuw opgestart vanwege een probleem. Druk op een toets\n"
                text "om door te gaan met opstarten, of wacht een paar seconden." line_spacing 25

        elif release <= (10, 15): # OS X El Capitan, macOS Sierra -> macOS Catalina
            add Solid("#000")

            vbox:
                style_prefix "bsod_macos"
                xalign 0.0
                yalign 0.0

                text "**************************************************\n"
                text "This system was automatically rebooted after panic" line_spacing 5
                text "**************************************************" line_spacing 5 

        else: # macOS Big Sur и старше
            add DynamicDisplayable(fake_macos_bigsur_panic)

    else: # Linux и другие платформы

        add Solid("#000")

        vbox:
            style_prefix "bsod_linux"

            text "metaverse-pci.c:v[config.version] 5/22/2024 Metaverse Enterprise Solutions\n"
            text "  https://www.metaverse-enterprise.com/network/metaverse-pci.html"
            text "hd0: METAVERSE ENTERPRISE VIRTUAL HARDDISK, ATA DISK drive"
            text "sda0 at 0x1f0 - 0x1f7, 0x3f6 on irq 14"
            text "hdc: METAVERSE ENTERPRISE VIRTUAL CD-ROM, ATAPI CD/DVD-ROM drive"
            text "sr0 at 0x444 - 0x910, 0x211 on irq 15"
            text "fd0: METAVERSE ENTERPRISE VIRTUAL FLOPPY, ATA FLOPPY drive"
            text "ide2 at 0x7363-0x6e6565, 0x4569 on irq 16"
            text "ACPI: PCI Interrupt Link [[LNKC] ebabked at IRQ 10"
            text "ACPI: PCI Interrupt 0000:00:03:.0[[A] -> Link [[LNKC] -> GSI 10 (level, low) -> IRQ 10"
            text "eno1: Metaverse Enterprise LIB-0922 found at 0xc453, IRQ 10, 09:10:21:86:75:30"
            text "sda: max request size: 4MiB"
            text "sda: 2147483648 sectors (1 TB) w/256KiB Cache, CHS=178/255/63, (U)DMA"
            text "sda: sda1"
            text "sr0: ATAPI 16x CD-ROM drive, 2MB Cache, (U)DMA"
            text "Uniform CD-ROM driver Revision: [renpy.version_tuple]"
            text "Done."
            text "Begin: DDLC.so"
            text "Done."
            text "DDLC.so[[3352]: Faled to initialize steam: FileNotFoundError(\"Could not find module '/usr/app/ddlc/lib/py3-linux-x86_64/steam_api64.so') (or one of its dependencies). Try using the full path with constructor syntax.\")"
            text "DDLC.so[[3352]: nvdrs: Loaded, about to disable thread optimizations."
            text "DDLC.so[[3352]: nvdrs: Disabled thread optimizations."
            text "DDLC.so: SUCCESS."
            text "Done."
            text "Begin: DDLC.so -> linux-5.18"
            text "/init: /init: 151: [bsodCode!u]: 0xforce=panic"
            text "Kernel panic - not syncing: Attempted to kill init!"
            add DynamicDisplayable(constantCursor)

    if renpy.windows:
        add Solid("#000") at win_bsod_transition
    else:
        add Solid("#000") at general_bsod_transition

style bsod_win7_text is gui_text
style bsod_win7_text:
    font "C:/Windows/Fonts/lucon.ttf"
    antialias False
    size 13
    line_leading 15
    line_spacing -14
    xsize 1279
    outlines []

style bsod_win8_text is gui_text
style bsod_win8_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 25
    line_spacing 5
    xsize 600
    outlines []

style bsod_win8_sad_text is gui_text
style bsod_win8_sad_text is bsod_win8_text:
    size 128
    xpos -8

style bsod_win8_sub_text is gui_text
style bsod_win8_sub_text is bsod_win8_text:
    size 11

style bsod_win10_text is bsod_win8_text
style bsod_win10_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 28
    line_leading 2
    line_spacing -2
    xsize 800
    outlines []

style bsod_win10_info_text is bsod_win10_text
style bsod_win10_info_text:
    size 13

style bsod_win10_sad_text is bsod_win10_text
style bsod_win10_sad_text:
    size 140
    xpos -8

style bsod_win10_sub_text is bsod_win10_text
style bsod_win10_sub_text:
    size 11

style bsod_osx_text is gui_text
style bsod_osx_text:
    font gui.default_font
    size 28
    outlines []
    line_spacing -30

style bsod_macos_text is bsod_osx_text
style bsod_macos_text:
    size 21
    line_spacing -25

style bsod_linux_text is gui_text
style bsod_linux_text:
    font "gui/font/consola.ttf"
    size 15
    outlines []
    line_leading 5

transform win_bsod_transition:
    "black"
    0.05
    yoffset 250
    0.05
    yoffset 500
    0.05
    yoffset 750

transform general_bsod_transition:
    "black"
    pause 2.5
    yoffset 750

transform bsod_qrcode(x):
    xysize(x,x)