## effects.rpy

# Этот файл содержит определения всех эффектов в DDLC, используемых во Втором акте.

init python:
    # Эта функция делает снимок экрана игры для дальнейшего накладывания
    # на него разных эффектов.
    def screenshot_srf():
        if renpy.version_tuple > (7, 3, 5, 606):
            srf = renpy.display.draw.screenshot(None)
        else:
            srf = renpy.display.draw.screenshot(None, False)

        return srf

    # Эта функция инвертирует изображение для дальнейшего использования классом «Invert».
    def invert():
        srf = screenshot_srf()
        inv = renpy.Render(srf.get_width(), srf.get_height()).canvas().get_surface()
        inv.fill((255,255,255,255))
        inv.blit(srf, (0,0), None, 2) 
        return inv

    # Этот класс содержит код для инвертирования цветов и дальнейшего вывода экраном «invert».
    class Invert(renpy.Displayable):
        def __init__(self, delay=0.0, screenshot_delay=0.0):
            super(Invert, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            self.height = self.width * 9 / 16
            self.srf = invert()
            self.delay = delay

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            if st >= self.delay:
                render.blit(self.srf, (0, 0))
            return render

    # Эта функция скрывает все внутриигровые окна.
    def hide_windows_enabled(enabled=True):
        global _windows_hidden
        _windows_hidden = not enabled

## Invert(length, delay)
# Этот экран вызывается выражением `show screen invert()` для инвертирования цветов экрана.
# Синтаксис:
# length - Указывает, сколько будет длиться эффект.
# delay - Ждёт X секунд, прежде чем показать эффект.
screen invert(length, delay=0.0):
    add Invert(delay) size (1280, 720)
    timer delay action PauseAudio("music")
    timer delay action Play("sound", "sfx/glitch1.ogg")
    timer length + delay action Hide("invert")
    on "show" action Function(hide_windows_enabled, enabled=False)
    on "hide" action PauseAudio("music", False)
    on "hide" action Stop("sound")
    on "hide" action Function(hide_windows_enabled, enabled=True)

init python:
    # В этом классе содержится код для эффекта разрыва экрана.
    class TearPiece:
        def __init__(self, startY, endY, offtimeMult, ontimeMult, offsetMin, offsetMax):
            self.startY = startY
            self.endY = endY
            self.offTime = (random.random() * 0.2 + 0.2) * offtimeMult
            self.onTime = (random.random() * 0.2 + 0.2) * ontimeMult
            self.offset = 0
            self.offsetMin = offsetMin
            self.offsetMax = offsetMax
        
        def update(self, st):
            st = st % (self.offTime + self.onTime)
            if st > self.offTime and self.offset == 0:
                self.offset = random.randint(self.offsetMin, self.offsetMax)
            elif st <= self.offTime and self.offset != 0:
                self.offset = 0
    
    # В этом классе содержится код для вывода эффекта разрыва экраном «tear».
    class Tear(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf=None):
            super(Tear, self).__init__()
            self.width, self.height = renpy.get_physical_size()

            if float(self.width) / float(self.height) > 16.0/9.0:
                self.width = self.height * 16 / 9
            else:
                self.height = self.width * 9 / 16
            self.number = number
            if not srf: self.srf = screenshot_srf()
            else: self.srf = srf

            self.pieces = []
            tearpoints = [0, self.height]
            for i in range(number):
                tearpoints.append(random.randint(10, int(self.height) - 10))
            tearpoints.sort()
            for i in range(number+1):
                self.pieces.append(TearPiece(tearpoints[i], tearpoints[i+1], offtimeMult, ontimeMult, offsetMin, offsetMax))
        
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            render.blit(self.srf, (0,0))
            for piece in self.pieces:
                piece.update(st)
                subsrf = self.srf.subsurface((0, max(0, piece.startY - 1), self.width, max(0, piece.endY - piece.startY)))
                render.blit(subsrf, (piece.offset, piece.startY))
            renpy.redraw(self, 0)
            return render

## Tear
# Этот экран вызывается выражением `show screen tear()` для разрыва экрана.
# Синтаксис:
# number - Указывает, на сколько частей будет разрываться экран.
# offtimeMult - Определяет множитель времени действия эффекта.
# ontimeMult - Определяет множитель времени, в течение которого длится эффект.
# offsetMin - Определяет минимальное смещение времени по множителю.
# offsetMax - Определяет the максимальное смещение времени по множителю.
# srf - Определяет изображение экрана, полученное функцией «screenshot_srf», если оное было объявлено.
screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None):
    zorder 150
    add Tear(number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf) size (1280,720)
    on "show" action Function(hide_windows_enabled, enabled=False)
    on "hide" action Function(hide_windows_enabled, enabled=True)

# RectStatic
# Эти изображения с преобразованиями показывают глючные прямоугольники в игре во время Третьего акта,
# когда Моника была удалена из игры.

# Это изображение с преобразованиями добавляет несколько чёрных квадратов на экран.
image m_rectstatic:
    RectStatic(Solid("#000"), 32, 32, 32).sm
    pos (0, 0)
    size (32, 32)

# Это изображение с преобразованиями добавляет несколько квадратов, вырезанных из логотипа DDLC.
image m_rectstatic2:
    RectStatic(im.FactorScale(im.Crop("gui/logo.png", (100, 100, 128, 128)), 0.25), 2, 32, 32).sm

# Это изображение с преобразованиями добавляет несколько квадратов спрайта Сайори из главного меню.
image m_rectstatic3:
    RectStatic(im.FactorScale(im.Crop("gui/menu_art_s.png", (100, 100, 64, 64)), 0.5), 2, 32, 32).sm

init python:
    # Этот класс определяет код, используемый для эффекта статичных прямоугольников (RectStatic).
    class RectStatic(object):
        def __init__(self, theDisplayable, numRects=12, rectWidth = 30, rectHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.timers = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.rectWidth = rectWidth
            self.rectHeight = rectHeight

            for i in range(self.numRects):
                self.add(self.displayable)
                self.timers.append(random.random() * 0.4 + 0.1)

        def add(self, d):
            s = self.sm.create(d)
            s.x = random.randint(0, 40) * 32
            s.y = random.randint(0, 23) * 32
            s.width = self.rectWidth
            s.height = self.rectHeight
            self.rects.append(s)

        def update(self, st):
            for i, s in enumerate(self.rects):
                if st >= self.timers[i]:
                    s.x = random.randint(0, 40) * 32
                    s.y = random.randint(0, 23) * 32
                    self.timers[i] = st + random.random() * 0.4 + 0.1
            return 0

    ## ParticleBurst
    # Этот класс определяет код, используемый для эффекта разрыва частиц (ParticleBurst).
    class ParticleBurst(object):
        def __init__(self, theDisplayable, explodeTime=0, numParticles=20, particleTime = 0.500, particleXSpeed = 3, particleYSpeed = 5):
            self.sm = SpriteManager(update=self.update)

            self.stars = [ ]
            self.displayable = theDisplayable
            self.explodeTime = explodeTime
            self.numParticles = numParticles
            self.particleTime = particleTime
            self.particleXSpeed = particleXSpeed
            self.particleYSpeed = particleYSpeed
            self.gravity = 240
            self.timePassed = 0

            for i in range(self.numParticles):
                self.add(self.displayable, 1)

        def add(self, d, speed):
            s = self.sm.create(d)
            speed = random.random()
            angle = random.random() * 3.14159 * 2
            xSpeed = speed * math.cos(angle) * self.particleXSpeed
            ySpeed = speed * math.sin(angle) * self.particleYSpeed - 1
            s.x = xSpeed * 24
            s.y = ySpeed * 24
            pTime = self.particleTime
            self.stars.append((s, ySpeed, xSpeed, pTime))

        def update(self, st):
            sindex=0
            for s, ySpeed, xSpeed, particleTime in self.stars:
                if (st < particleTime):
                    s.x = xSpeed * 120 * (st + .20)
                    s.y = (ySpeed * 120 * (st + .20) + (self.gravity * st * st))
                else:
                    s.destroy()
                    self.stars.pop(sindex)
                sindex += 1
            return 0

    ## Blood
    # Этот класс определяет код, используемый для эффекта крови (Blood) для Юри во Втором акте.
    class Blood(object):
        def __init__(self, theDisplayable, density=120.0, particleTime=1.0, dripChance=0.05, dripSpeedX=0.0, dripSpeedY=120.0, dripTime=180.0, burstSize=100, burstSpeedX=200.0, burstSpeedY=400.0, numSquirts=4, squirtPower=400, squirtTime=0.25):
            self.sm = SpriteManager(update=self.update)
            self.drops = []
            self.squirts = []
            self.displayable = theDisplayable
            self.density = density
            self.particleTime = particleTime
            self.dripChance = dripChance
            self.dripSpeedX = dripSpeedX
            self.dripSpeedY = dripSpeedY
            self.gravity = 800.0
            self.dripTime = dripTime
            self.burstSize = burstSize
            self.burstSpeedX = burstSpeedX
            self.burstSpeedY = burstSpeedY
            self.lastUpdate = 0
            self.delta = 0.0

            for i in range(burstSize): self.add_burst(theDisplayable, 0)
            for i in range(numSquirts): self.add_squirt(squirtPower, squirtTime)

        # Эта функция создаёт одну струйку крови по дуге.
        def add_squirt(self, squirtPower, squirtTime):
            angle = random.random() * 6.283
            xSpeed = squirtPower * math.cos(angle)
            ySpeed = squirtPower * math.sin(angle)
            self.squirts.append([xSpeed, ySpeed, squirtTime])

        # Эта функция создаёт всплеск крови, возникающий из конкретного участка.
        def add_burst(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.burstSpeedX + 20
            ySpeed = (random.random() - 0.75) * self.burstSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])

        # Эта функция создаёт текущий поток крови.
        def add_drip(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.dripSpeedX + 20
            ySpeed = random.random() * self.dripSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])

        def update(self, st):
            delta = st - self.lastUpdate
            self.delta += st - self.lastUpdate
            self.lastUpdate = st

            sindex = 0
            for xSpeed, ySpeed, squirtTime in self.squirts:
                if st > squirtTime: self.squirts.pop(sindex)
                sindex += 1

            pindex = 0
            if st < self.dripTime:
                while self.delta * self.density >= 1.0:
                    self.delta -= (1.0 / self.density)
                    if random.random() >= 1 - self.dripChance: self.add_drip(self.displayable, st)
                    for xSpeed, ySpeed, squirtTime in self.squirts:
                        s = self.sm.create(self.displayable)
                        s.x += (random.random() - 0.5) * 5
                        s.y += (random.random() - 0.5) * 5
                        self.drops.append([s, xSpeed + (random.random() - 0.5) * 20, ySpeed + (random.random() - 0.5) * 20, self.particleTime, st])
            for s, xSpeed, ySpeed, particleTime, startTime in self.drops:
                if (st - startTime < particleTime):
                    s.x += xSpeed * delta
                    s.y += ySpeed * delta
                    self.drops[pindex][2] += self.gravity * delta
                else:
                    s.destroy()
                    self.drops.pop(pindex)
                pindex += 1
            return 0

# Это изображение с преобразованиями добавляет каплю крови, которая со
# временем становится длиннее и тоньше.
image blood_particle_drip:
    "gui/blood_drop.png"
    yzoom 0 yanchor 0.2 subpixel True
    linear 10 yzoom 8

# Это изображение с преобразованиями добавляет каплю крови, которая со
# временем случайным образом становится тоньше.
image blood_particle:
    subpixel True
    "gui/blood_drop.png"
    zoom 0.75
    alpha 0.75
    choice:
        linear 0.25 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.55 zoom 0

# Это изображение с преобразованиями добавляет каплю крови, которая
# создаёт всплеск и капает в течение трёх минут.
image blood:
    size (1, 1)
    truecenter
    Blood("blood_particle").sm

# Это изображение с преобразованиями добавляет каплю крови, которая
# не создаёт всплеск, а вероятность капания увеличивается.
image blood_eye:
    size (1, 1)
    truecenter
    Blood("blood_particle", dripChance=0.5, numSquirts=0).sm

# Это изображение с преобразованиями добавляет каплю крови, которая
# имеет очень низкий шанс капания.
image blood_eye2:
    size (1, 1)
    truecenter
    Blood("blood_particle", dripChance=0.005, numSquirts=0, burstSize=0).sm

init python:
    ## AnimatedMask
    # Этот класс определяет код, используемый для эффекта анимированной маски (AnimatedMask) в Третьем акте.
    class AnimatedMask(renpy.Displayable):
        
        def __init__(self, child, mask, maskb, oc, op, moving=True, speed=1.0, frequency=1.0, amount=0.5, **properties):
            super(AnimatedMask, self).__init__(**properties)
            
            self.child = renpy.displayable(child)
            self.mask = renpy.displayable(mask)
            self.maskb = renpy.displayable(maskb)
            self.oc = oc
            self.op = op
            self.null = None
            self.size = None
            self.moving = moving
            self.speed = speed
            self.amount = amount
            self.frequency = frequency
        
        def render(self, width, height, st, at):
            
            cr = renpy.render(self.child, width, height, st, at)
            mr = renpy.render(self.mask, width, height, st, at)
            mb = renpy.Render(width, height)
            
            
            if self.moving:
                mb.place(self.mask, ((-st * 50) % (width * 2)) - (width * 2), 0)
                mb.place(self.maskb, -width / 2, 0)
            else:
                mb.place(self.mask, 0, 0)
                mb.place(self.maskb, 0, 0)
            
            
            
            cw, ch = cr.get_size()
            mw, mh = mr.get_size()
            
            w = min(cw, mw)
            h = min(ch, mh)
            size = (w, h)
            
            if self.size != size:
                self.null = Null(w, h)
            
            nr = renpy.render(self.null, width, height, st, at)
            
            rv = renpy.Render(w, h)
            
            complete = self.oc + math.pow(math.sin(st * self.speed / 8), 64 * self.frequency) * self.amount

            rv.operation = renpy.display.render.IMAGEDISSOLVE
            rv.operation_alpha = 1.0
            rv.operation_complete = complete
            rv.operation_parameter = self.op
            
            if renpy.display.render.models:

                target = rv.get_size()

                op = self.op

                # Prevent a DBZ if the user gives us a 0 ramp.
                if op < 1:
                    op = 1

                # Compute the offset to apply to the alpha.
                start = -1.0
                end = op / 256.0
                offset = start + (end - start) * complete

                rv.mesh = True

                rv.add_shader("renpy.imagedissolve",)
                rv.add_uniform("u_renpy_dissolve_offset", offset)
                rv.add_uniform("u_renpy_dissolve_multiplier", 256.0 / op)
                rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)
            
            rv.blit(mb, (0, 0), focus=False, main=False)
            rv.blit(nr, (0, 0), focus=False, main=False)
            rv.blit(cr, (0, 0))
            
            renpy.redraw(self, 0)
            return rv

    # Эта функция делает изображение прозрачным на короткое мгновение, а затем 
    # проявляет и растворяет его в Третьем акте.
    def monika_alpha(trans, st, at):
        trans.alpha = math.pow(math.sin(st / 8), 64) * 1.4
        return 0

## Старый Синий экран смерти
# Эти изображения заставляют игрока думать, что его система крашнулась.
# Данная функция была упразднена в угоду более лучшей реализации СЭС, но 
# оставлена здесь для совместимости.

image bsod_1:
    "images/bg/bsod.png"
    size (1280,720)
image bsod_2:
    "black"
    0.1
    yoffset 250
    0.1
    yoffset 500
    0.1
    yoffset 750

image bsod = Composite((1280, 720), (0, 0), "bsod_1", (0, 0), "bsod_2")

## Вены
# Это изображение с преобразованиями создаёт ореол из вен вокруг экрана, которые трясутся и пульсируют
# случайным образом во Втором акте.
image veins:
    AnimatedMask("images/bg/veinmask.png", "images/bg/veinmask.png", "images/bg/veinmaskb.png", 0.15, 16, moving=False, speed=10.0, frequency=0.25, amount=0.1)
    xanchor 0.05 zoom 1.10
    xpos -5
    subpixel True
    parallel:
        ease 2.0 xpos 5
        ease 1.0 xpos 0
        ease 1.0 xpos 5
        ease 2.0 xpos -5
        ease 1.0 xpos 0
        ease 1.0 xpos -5
        repeat
    parallel:
        choice:
            0.6
        choice:
            0.2
        choice:
            0.3
        choice:
            0.4
        choice:
            0.5
        pass
        choice:
            xoffset 0
        choice:
            xoffset 1
        choice:
            xoffset 2
        choice:
            xoffset -1
        choice:
            xoffset -2
        repeat
