"""
╔══════════════════════════════════════════════════════════╗
║              🦊  Foxy Memory   🔥                        ║
║      Juego educativo de POO con el Foxy Memory           ║
║      Aprende Programación Orientada a Objetos            ║
╠══════════════════════════════════════════════════════════╣
║  © 2026 David Mutis, Sebastián Durán, Juan Pablo López   ║
║  Todos los derechos reservados.                          ║
║  Software educativo de uso libre con atribución.         ║
╠══════════════════════════════════════════════════════════╣
║  Requiere: Python 3.8+  (tkinter incluido)               ║
║  Ejecutar: Juego Poo Quest.py                            ║
╚══════════════════════════════════════════════════════════╝
"""

import tkinter as tk
from tkinter import font as tkfont
import math, random

# ─── PALETA DE COLORES ──────────────────────────────────────────
C = {
    "page":      "#1a1a2e",   # fondo oscuro azul noche
    "card":      "#16213e",   # card azul oscuro
    "card2":     "#0f3460",   # card acento
    "ink":       "#e0e0e0",
    "snow":      "#e8e8f0",
    "orange":    "#f77f00",   # naranja zorro
    "orange_dk": "#d45f00",
    "orange_lt": "#ffb347",
    "fire":      "#ff4500",
    "fire_lt":   "#ff6b35",
    "gold":      "#ffd700",
    "gold_dk":   "#c9a020",
    "danger":    "#e63946",
    "danger_l":  "#3d0c11",
    "success":   "#2dc653",
    "success_l": "#0a2e14",
    "hint":      "#1a1f4e",
    "hint_txt":  "#7eb8ff",
    "muted":     "#8888aa",
    "border":    "#2a2a4a",
    "white":     "#ffffff",
    "tail":      "#f77f00",
    "belly":     "#ffe0c0",
}

# ─── NIVELES Y PREGUNTAS ────────────────────────────────────────
NIVELES = [
    {
        "tema": "🦊 Clases y Objetos",
        "emoji": "🦊",
        "preguntas": [
            {
                "e": "¿Qué es una Clase en POO?",
                "ops": [
                    "Un objeto concreto que existe en memoria",
                    "Una plantilla o molde para crear objetos",
                    "Una función que retorna datos"
                ],
                "c": 1,
                "p": "Imagina que el Zorro Cody es un objeto. La 'clase Zorro' sería el plano que define cómo son todos los zorros.",
            },
            {
                "e": "¿Qué es una Instancia u Objeto?",
                "ops": [
                    "Un objeto real creado a partir de una clase",
                    "Un tipo especial de bucle",
                    "Un error en tiempo de ejecución"
                ],
                "c": 0,
                "p": "Cody es una instancia de la clase Zorro. Es concreto, vive en memoria y tiene sus propios valores.",
            },
            {
                "e": "¿Qué son los Atributos de una clase?",
                "ops": [
                    "Los métodos que puede ejecutar",
                    "Las variables que describen las características del objeto",
                    "Los archivos que importa el programa"
                ],
                "c": 1,
                "p": "Los atributos de Cody son: nombre='Cody', color='naranja', velocidad=10. Describen cómo ES el objeto.",
            },
            {
                "e": "¿Para qué sirve el método __init__?",
                "ops": [
                    "Para destruir un objeto cuando ya no se usa",
                    "Para inicializar los atributos cuando se crea un objeto",
                    "Para imprimir el objeto en pantalla"
                ],
                "c": 1,
                "p": "__init__ es el constructor: se ejecuta automáticamente al crear una instancia y define sus atributos iniciales.",
            },
        ]
    },
    {
        "tema": "🌿 Herencia y Polimorfismo",
        "emoji": "🌿",
        "preguntas": [
            {
                "e": "¿Qué permite la Herencia en POO?",
                "ops": [
                    "Duplicar exactamente el código de otra clase",
                    "Que una subclase reutilice atributos y métodos de una superclase",
                    "Eliminar clases que ya no se necesitan"
                ],
                "c": 1,
                "p": "Cody hereda de Animal: no necesita redefinir respirar() o moverse(), ya los tiene por herencia.",
            },
            {
                "e": "¿Cómo se llama la clase de la que se hereda?",
                "ops": [
                    "Subclase o clase hija",
                    "Superclase o clase padre",
                    "Clase abstracta siempre"
                ],
                "c": 1,
                "p": "Animal es la superclase (padre). Zorro es la subclase (hija) que hereda de Animal.",
            },
            {
                "e": "¿Qué describe mejor el Polimorfismo?",
                "ops": [
                    "Un mismo método actúa diferente según el objeto",
                    "Todos los objetos deben tener los mismos métodos",
                    "Solo puede existir una instancia de cada clase"
                ],
                "c": 0,
                "p": "hablar() en Zorro devuelve '¡Au!', en Perro '¡Guau!', en Gato '¡Miau!'. Mismo nombre, comportamiento distinto.",
            },
            {
                "e": "¿Qué es la sobreescritura (override) de métodos?",
                "ops": [
                    "Eliminar un método de la clase padre",
                    "Crear un método con el mismo nombre en la subclase para cambiar su comportamiento",
                    "Importar métodos desde otra biblioteca"
                ],
                "c": 1,
                "p": "Zorro redefine hablar() para que diga '¡Au!' en vez del comportamiento genérico de Animal.",
            },
        ]
    },
    {
        "tema": "🔒 Encapsulamiento y Abstracción",
        "emoji": "🔒",
        "preguntas": [
            {
                "e": "¿Para qué sirve el Encapsulamiento?",
                "ops": [
                    "Para hacer el código más lento pero seguro",
                    "Para proteger datos internos y controlar el acceso a ellos",
                    "Para compartir todos los atributos libremente"
                ],
                "c": 1,
                "p": "La salud de Cody es privada (__salud). Solo puede cambiarse con curar() o lastimar(), nunca directamente.",
            },
            {
                "e": "En Python, ¿cómo se marca un atributo como privado?",
                "ops": [
                    "Con el prefijo private_ antes del nombre",
                    "Con doble guión bajo __ antes del nombre",
                    "Escribiéndolo en MAYÚSCULAS"
                ],
                "c": 1,
                "p": "self.__salud es privado. Python lo transforma internamente para evitar acceso accidental desde fuera.",
            },
            {
                "e": "¿Qué es la Abstracción en POO?",
                "ops": [
                    "Mostrar todos los detalles internos al usuario",
                    "Representar solo las características esenciales, ocultando los detalles",
                    "Es exactamente lo mismo que encapsulamiento"
                ],
                "c": 1,
                "p": "No necesitas saber cómo funciona el motor del coche para conducirlo. La abstracción oculta la complejidad.",
            },
            {
                "e": "¿Qué son los métodos getter y setter?",
                "ops": [
                    "Métodos para leer y modificar atributos privados de forma controlada",
                    "Métodos para crear y destruir objetos",
                    "Funciones para conectarse a bases de datos"
                ],
                "c": 0,
                "p": "get_salud() permite leer __salud. set_salud(v) permite cambiarla, pero puede validar que sea un valor válido.",
            },
        ]
    },
]


# ─── DATOS MINIJUEGO MEMORY ─────────────────────────────────────
# Cada par comparte el mismo color de fondo al voltearse
COLORES_PAR = ["#7b2d8b", "#1a6b3c", "#b05a00", "#1a4a8a"]  # morado, verde, naranja, azul

MEMORY_RONDAS = [
    {
        "titulo": "Memory POO — Voltea y empareja",
        "pares": [
            ("Clase",     "Plantilla para\nconstruir objetos"),
            ("Objeto",    "Instancia real\nde una clase"),
            ("Atributo",  "Variable que describe\nal objeto"),
            ("Metodo",    "Funcion que define\nsu comportamiento"),
        ]
    },
    {
        "titulo": "Memory POO — Herencia",
        "pares": [
            ("Herencia",     "Reutiliza codigo\nde otra clase"),
            ("Superclase",   "La clase padre\nde la que se hereda"),
            ("Subclase",     "La clase hija\nque extiende al padre"),
            ("Polimorfismo", "Mismo metodo,\ndistinto comportamiento"),
        ]
    },
]

LETRAS = ["A", "B", "C"]


# ─── DIBUJADOR DEL ZORRO ─────────────────────────────────────────
class ZorroCanvas(tk.Canvas):
    """Canvas que dibuja un zorro animado con expresiones."""

    def __init__(self, parent, size=120, **kw):
        bg = kw.pop("bg", C["card"])
        super().__init__(parent, width=size, height=size,
                         bg=bg, highlightthickness=0, **kw)
        self.size = size
        self.smile = True
        self.wink = False
        self._anim_id = None
        self._bounce_step = 0
        self._shake_step = 0
        self._blink_on = True
        self.draw()

    def draw(self, offset_x=0, offset_y=0):
        self.delete("all")
        s = self.size
        cx, cy = s / 2 + offset_x, s * 0.58 + offset_y
        r = s * 0.32

        # ── Cola (detrás de todo) ──
        tail_pts = []
        for i in range(20):
            t = math.radians(i * 9)
            tx = cx + r * 1.3 * math.cos(t)
            ty = cy + r * 0.5 * math.sin(t) + r * 0.9
        self._oval(cx + r * 1.1, cy + r * 0.95, r * 0.55, r * 0.35, C["orange"])
        self._oval(cx + r * 1.35, cy + r * 0.85, r * 0.28, r * 0.22, C["white"])

        # ── Orejas puntiagudas (triángulos) ──
        ear_l = self._ear_pts(cx - r * 0.55, cy - r * 0.75, r * 0.28, r * 0.45, -10)
        ear_r = self._ear_pts(cx + r * 0.55, cy - r * 0.75, r * 0.28, r * 0.45, 10)
        self.create_polygon(ear_l, fill=C["orange"], outline="")
        self.create_polygon(ear_r, fill=C["orange"], outline="")
        # interior orejas
        ear_li = self._ear_pts(cx - r * 0.55, cy - r * 0.75, r * 0.16, r * 0.30, -10)
        ear_ri = self._ear_pts(cx + r * 0.55, cy - r * 0.75, r * 0.16, r * 0.30, 10)
        self.create_polygon(ear_li, fill=C["fire_lt"], outline="")
        self.create_polygon(ear_ri, fill=C["fire_lt"], outline="")

        # ── Cabeza (naranja) ──
        self._oval(cx, cy, r, r, C["orange"])

        # ── Máscara facial blanca ──
        self._oval(cx, cy + r * 0.12, r * 0.68, r * 0.60, C["belly"])

        # ── Manchas oscuras ojos (antifaz) ──
        self._oval(cx - r * 0.38, cy - r * 0.15, r * 0.27, r * 0.22, "#2a1a00")
        self._oval(cx + r * 0.38, cy - r * 0.15, r * 0.27, r * 0.22, "#2a1a00")

        # ── Ojos ──
        ew = r * 0.14
        if self._blink_on:
            self._oval(cx - r * 0.38, cy - r * 0.17, ew, ew * 1.1, C["white"])
            self._oval(cx + r * 0.38, cy - r * 0.17, ew, ew * 1.1, C["white"])
            # pupilas
            pw = r * 0.08
            self._oval(cx - r * 0.35, cy - r * 0.16, pw, pw, "#1a0a00")
            self._oval(cx + r * 0.35, cy - r * 0.16, pw, pw, "#1a0a00")
            # brillos
            bw = r * 0.04
            self._oval(cx - r * 0.33, cy - r * 0.19, bw, bw, "white")
            self._oval(cx + r * 0.33, cy - r * 0.19, bw, bw, "white")
        else:
            # ojos cerrados (línea curva)
            self.create_arc(cx - r*0.53, cy - r*0.25, cx - r*0.24, cy - r*0.08,
                            start=0, extent=180, style="arc",
                            outline=C["orange_dk"], width=max(2, int(s*0.022)))
            self.create_arc(cx + r*0.24, cy - r*0.25, cx + r*0.53, cy - r*0.08,
                            start=0, extent=180, style="arc",
                            outline=C["orange_dk"], width=max(2, int(s*0.022)))

        # ── Hocico ──
        self._oval(cx, cy + r * 0.30, r * 0.30, r * 0.22, C["belly"])
        # nariz triangular
        nose = [cx, cy + r * 0.12,
                cx - r * 0.10, cy + r * 0.22,
                cx + r * 0.10, cy + r * 0.22]
        self.create_polygon(nose, fill="#2a1a00", outline="")
        # línea nariz-boca
        self.create_line(cx, cy + r * 0.22, cx, cy + r * 0.32,
                         fill="#2a1a00", width=max(1, int(s * 0.018)))

        # ── Boca ──
        by = cy + r * 0.32
        if self.smile:
            self.create_arc(cx - r * 0.20, by - r * 0.12,
                            cx, by + r * 0.12,
                            start=200, extent=140, style="arc",
                            outline="#2a1a00", width=max(2, int(s * 0.022)))
            self.create_arc(cx, by - r * 0.12,
                            cx + r * 0.20, by + r * 0.12,
                            start=200, extent=140, style="arc",
                            outline="#2a1a00", width=max(2, int(s * 0.022)))
        else:
            self.create_arc(cx - r * 0.22, by,
                            cx + r * 0.22, by + r * 0.20,
                            start=20, extent=140, style="arc",
                            outline="#2a1a00", width=max(2, int(s * 0.022)))

        # ── Bigotes ──
        wh_color = C["white"] if self._blink_on else C["belly"]
        for i, wx in enumerate([-1, 1]):
            base_x = cx + wx * r * 0.15
            for j, wy in enumerate([-1, 0, 1]):
                x1 = base_x
                x2 = cx + wx * r * 0.70
                y1 = by - r * 0.04 + wy * r * 0.10
                y2 = y1 + wy * r * 0.06
                self.create_line(x1, y1, x2, y2,
                                 fill="#555", width=1)

    def _ear_pts(self, cx, cy, rx, ry, angle_deg):
        """Triángulo de oreja con ligera rotación."""
        a = math.radians(angle_deg)
        def rot(x, y):
            return (cx + x * math.cos(a) - y * math.sin(a),
                    cy + x * math.sin(a) + y * math.cos(a))
        pts = [rot(0, -ry), rot(-rx, ry * 0.5), rot(rx, ry * 0.5)]
        return [v for pt in pts for v in pt]

    def _oval(self, cx, cy, rx, ry, color):
        self.create_oval(cx - rx, cy - ry, cx + rx, cy + ry,
                         fill=color, outline="")

    def set_happy(self):
        self.smile = True
        self._blink_on = True
        self.draw()
        self._start_bounce()

    def set_sad(self):
        self.smile = False
        self._blink_on = True
        self.draw()
        self._start_shake()

    def set_neutral(self):
        self.smile = True
        self._blink_on = True
        self.draw()

    def _start_bounce(self):
        self._cancel_anim()
        self._bounce_step = 0
        self._animate_bounce()

    def _animate_bounce(self):
        steps = [0, -9, -15, -11, -5, -9, -5, -2, 0]
        if self._bounce_step < len(steps):
            oy = steps[self._bounce_step]
            self.draw(offset_y=oy)
            self._bounce_step += 1
            self._anim_id = self.after(40, self._animate_bounce)

    def _start_shake(self):
        self._cancel_anim()
        self._shake_step = 0
        self._animate_shake()

    def _animate_shake(self):
        steps = [0, -10, 10, -8, 8, -5, 5, 0]
        if self._shake_step < len(steps):
            ox = steps[self._shake_step]
            self.draw(offset_x=ox)
            self._shake_step += 1
            self._anim_id = self.after(50, self._animate_shake)

    def _cancel_anim(self):
        if self._anim_id:
            self.after_cancel(self._anim_id)
            self._anim_id = None


# ─── UTILIDADES DE DIBUJO ────────────────────────────────────────
def rounded_rect(canvas, x1, y1, x2, y2, radius, color,
                 outline="", outline_width=0):
    r = radius
    pts = [
        x1+r, y1,   x2-r, y1,
        x2,   y1,   x2,   y1+r,
        x2,   y2-r, x2,   y2,
        x2-r, y2,   x1+r, y2,
        x1,   y2,   x1,   y2-r,
        x1,   y1+r, x1,   y1,
    ]
    if outline and outline_width:
        canvas.create_polygon(pts, smooth=True, fill=color,
                              outline=outline, width=outline_width)
    else:
        canvas.create_polygon(pts, smooth=True, fill=color, outline=color)


# ─── BOTÓN REDONDEADO ────────────────────────────────────────────
class RoundButton(tk.Canvas):
    def __init__(self, parent, text, command, width=200, height=44,
                 radius=14, bg=C["orange"], fg="white",
                 hover_bg=C["fire"], font_obj=None, canvas_bg=None, **kw):
        safe_bg = canvas_bg if canvas_bg else C["page"]
        super().__init__(parent, width=width, height=height,
                         highlightthickness=0, bg=safe_bg,
                         cursor="hand2", **kw)
        self._text  = text
        self._cmd   = command
        self._cmd_actual = command
        self._btn_w = width
        self._btn_h = height
        self._r     = radius
        self._bg    = bg
        self._hbg   = hover_bg
        self._fg    = fg
        self._font  = font_obj or tkfont.Font(family="Helvetica", size=11, weight="bold")
        self._cur_bg = bg
        self.after(10, self._draw)
        self.bind("<Enter>",          lambda e: self._hover(True))
        self.bind("<Leave>",          lambda e: self._hover(False))
        self.bind("<Button-1>",       lambda e: self._click())
        self.bind("<ButtonRelease-1>",lambda e: self._release())

    def _draw(self, scale=1.0):
        self.delete("all")
        m = int((1 - scale) * 4)
        rounded_rect(self, m, m, self._btn_w - m, self._btn_h - m,
                     self._r, self._cur_bg)
        self.create_text(self._btn_w // 2, self._btn_h // 2,
                         text=self._text, fill=self._fg, font=self._font)

    def _hover(self, on):
        self._cur_bg = self._hbg if on else self._bg
        self._draw()

    def _click(self):  self._draw(scale=0.96)

    def _release(self):
        self._draw()
        if self._cmd: self._cmd()

    def set_state(self, enabled=True):
        if not enabled:
            self._cur_bg = C["border"]
            self._cmd = None
        else:
            self._cur_bg = self._bg
            self._cmd = self._cmd_actual
        self._draw()


# ─── BOTÓN DE OPCIÓN ─────────────────────────────────────────────
class OpcionBtn(tk.Canvas):
    def __init__(self, parent, letra, texto, command, width=460):
        h = 54
        super().__init__(parent, width=width, height=h,
                         highlightthickness=0, bg=C["card"], cursor="hand2")
        self._btn_w  = width
        self._btn_h  = h
        self._letra  = letra
        self._texto  = texto
        self._cmd    = command
        self._state  = "normal"
        self._hover  = False
        self._bold   = tkfont.Font(family="Helvetica", size=10, weight="bold")
        self._body   = tkfont.Font(family="Helvetica", size=11)
        self.after(10, self._draw)
        self.bind("<Enter>",    lambda e: self._on_enter())
        self.bind("<Leave>",    lambda e: self._on_leave())
        self.bind("<Button-1>", lambda e: self._on_click())

    def _draw(self):
        self.delete("all")
        if self._state == "ok":
            bg, bdr, lb, lf, tc = C["success_l"], C["success"], C["success"], C["white"], C["success"]
        elif self._state == "mal":
            bg, bdr, lb, lf, tc = C["danger_l"], C["danger"], C["danger"], C["white"], C["danger"]
        elif self._hover:
            bg, bdr, lb, lf, tc = "#1e2a50", C["orange"], C["orange"], C["white"], C["orange_lt"]
        else:
            bg, bdr, lb, lf, tc = C["card2"], C["border"], C["card2"], C["ink"], C["ink"]

        rounded_rect(self, 1, 1, self._btn_w - 1, self._btn_h - 1, 14, bg, bdr, 2)

        lx, ly, lr = 32, self._btn_h // 2, 14
        self.create_oval(lx-lr, ly-lr, lx+lr, ly+lr, fill=lb, outline="")
        lbl = "✓" if self._state=="ok" else ("✗" if self._state=="mal" else self._letra)
        self.create_text(lx, ly, text=lbl, fill=lf, font=self._bold)

        max_chars = int((self._btn_w - 85) / 7)
        txt = self._texto if len(self._texto) <= max_chars else self._texto[:max_chars-1] + "…"
        self.create_text(62, self._btn_h // 2, text=txt, fill=tc,
                         font=self._body, anchor="w")

    def _on_enter(self):
        if self._state == "normal":
            self._hover = True;  self._draw()

    def _on_leave(self):
        self._hover = False;  self._draw()

    def _on_click(self):
        if self._state == "normal" and self._cmd:
            self._cmd()

    def set_state(self, state):
        self._state = state;  self._hover = False;  self._draw()

    def disable(self):
        self._cmd = None
        if self._state == "normal":
            self.config(cursor="arrow")


# ─── APLICACIÓN PRINCIPAL ────────────────────────────────────────
class ZorroPOO(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🦊 Foxy Memory — Aprende Programación Orientada a Objetos")
        self.configure(bg=C["page"])
        self.resizable(False, False)
        self.geometry("580x800")

        # Estado
        self.nombre = ""
        self.puntos = 0
        self.vidas  = 3
        self.nivel  = 0
        self.pregunta_idx = 0
        self.respondido   = False
        self.racha        = 0   # respuestas correctas consecutivas
        self.mejor_racha  = 0

        # Fuentes
        self.f_title = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self.f_sub   = tkfont.Font(family="Helvetica", size=11)
        self.f_h2    = tkfont.Font(family="Helvetica", size=14, weight="bold")
        self.f_body  = tkfont.Font(family="Helvetica", size=12)
        self.f_sm    = tkfont.Font(family="Helvetica", size=10)
        self.f_bold  = tkfont.Font(family="Helvetica", size=11, weight="bold")
        self.f_huge  = tkfont.Font(family="Helvetica", size=34, weight="bold")
        self.f_badge = tkfont.Font(family="Helvetica", size=9,  weight="bold")

        # Scroll
        outer = tk.Frame(self, bg=C["page"])
        outer.pack(fill="both", expand=True)
        canvas_scroll = tk.Canvas(outer, bg=C["page"], highlightthickness=0)
        sb = tk.Scrollbar(outer, orient="vertical", command=canvas_scroll.yview)
        canvas_scroll.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        canvas_scroll.pack(side="left", fill="both", expand=True)
        self.container = tk.Frame(canvas_scroll, bg=C["page"])
        self._scroll_win = canvas_scroll.create_window((0, 0), window=self.container, anchor="nw")
        self.container.bind("<Configure>", lambda e: canvas_scroll.configure(
            scrollregion=canvas_scroll.bbox("all")))
        canvas_scroll.bind("<Configure>", lambda e: canvas_scroll.itemconfig(
            self._scroll_win, width=e.width))
        self.bind_all("<MouseWheel>", lambda e: canvas_scroll.yview_scroll(
            -1*(e.delta//120), "units"))

        self._build_inicio()

    # ──────── PANTALLA INICIO ────────────────────────────────────
    def _build_inicio(self):
        self._clear()

        # Título con efecto
        title_frame = tk.Frame(self.container, bg=C["page"])
        title_frame.pack(pady=(10, 2))
        tk.Label(title_frame, text="🦊 ", font=self.f_title,
                 bg=C["page"], fg=C["orange"]).pack(side="left")
        tk.Label(title_frame, text="Foxy Memory", font=self.f_title,
                 bg=C["page"], fg=C["orange_lt"]).pack(side="left")
        tk.Label(title_frame, text=" 🔥", font=self.f_title,
                 bg=C["page"], fg=C["fire"]).pack(side="left")

        tk.Label(self.container,
                 text="Domina la Programación Orientada a Objetos",
                 font=self.f_sm, bg=C["page"], fg=C["muted"]).pack()

        # Zorro animado
        zorro = ZorroCanvas(self.container, size=170, bg=C["page"])
        zorro.pack(pady=(14, 0))
        zorro.set_happy()

        # Descripción
        tk.Label(self.container,
                 text="¡Cody el Zorro te guiará en el camino del POO!\n"
                      "3 niveles · 12 preguntas · gana puntos de fuego 🔥",
                 font=self.f_body, bg=C["page"], fg=C["snow"],
                 justify="center").pack(pady=(10, 14))

        # Badges de niveles
        badges = tk.Frame(self.container, bg=C["page"])
        badges.pack(pady=(0, 18))
        for txt, col in [
            ("🦊 Clases y Objetos", C["orange"]),
            ("🌿 Herencia",         C["success"]),
            ("🔒 Encapsulamiento",  C["hint_txt"]),
        ]:
            lbl = tk.Label(badges, text=txt, font=self.f_badge,
                           bg=C["card2"], fg=col,
                           padx=12, pady=6,
                           highlightbackground=col,
                           highlightthickness=1)
            lbl.pack(side="left", padx=5)

        # Separador
        self._fire_separator()

        # Bonus info
        bonus_frame = tk.Frame(self.container, bg=C["card"],
                               highlightbackground=C["orange"],
                               highlightthickness=1)
        bonus_frame.pack(fill="x", pady=(0, 14), padx=4)
        tk.Label(bonus_frame,
                 text="⚡ Consejo: ¡Las rachas de respuestas correctas dan puntos extra!",
                 font=self.f_sm, bg=C["card"], fg=C["gold"],
                 padx=14, pady=8).pack()

        # Input nombre
        tk.Label(self.container, text="¿Cuál es tu nombre, estudiante?",
                 font=self.f_bold, bg=C["page"], fg=C["snow"]).pack(anchor="w", padx=4)
        self._nombre_var = tk.StringVar()
        entry_frame = tk.Frame(self.container,
                               bg=C["orange"], highlightthickness=0)
        entry_frame.pack(fill="x", pady=(6, 16), padx=4)
        entry = tk.Entry(entry_frame, textvariable=self._nombre_var,
                         font=self.f_body, bg=C["card2"], fg=C["snow"],
                         relief="flat", bd=0,
                         insertbackground=C["orange_lt"],
                         highlightthickness=0)
        entry.pack(fill="x", padx=2, pady=2, ipady=9, ipadx=12)
        entry.focus()
        entry.bind("<Return>", lambda e: self._empezar())

        RoundButton(self.container, "¡Comenzar aventura! 🦊",
                    self._empezar, width=480, height=52,
                    radius=16, bg=C["orange"], hover_bg=C["fire"],
                    fg=C["white"], font_obj=self.f_h2, canvas_bg=C["page"]).pack(pady=6, padx=4)

        # ── Botones inferiores ──
        botones_row = tk.Frame(self.container, bg=C["page"])
        botones_row.pack(pady=(8, 4))
        RoundButton(botones_row, "📖 Acerca de",
                    self._build_acerca, width=200, height=38,
                    radius=12, bg=C["card2"], hover_bg=C["border"],
                    fg=C["hint_txt"], font_obj=self.f_sm,
                    canvas_bg=C["page"]).pack(side="left", padx=6)
        RoundButton(botones_row, "📋 Bitácora",
                    self._build_bitacora, width=200, height=38,
                    radius=12, bg=C["card2"], hover_bg=C["border"],
                    fg=C["hint_txt"], font_obj=self.f_sm,
                    canvas_bg=C["page"]).pack(side="left", padx=6)

        # ── Créditos en pantalla de inicio ──
        cr_frame = tk.Frame(self.container, bg=C["page"])
        cr_frame.pack(pady=(6, 4))
        tk.Frame(cr_frame, bg=C["border"], height=1).pack(fill="x", pady=(0, 6))
        tk.Label(cr_frame,
                 text="© 2026  David Mutis · Sebastián Durán · Juan Pablo López",
                 font=self.f_sm, bg=C["page"], fg=C["muted"]).pack()
        tk.Label(cr_frame,
                 text="Todos los derechos reservados — Software educativo",
                 font=self.f_sm, bg=C["page"], fg=C["border"]).pack()

    # ──────── PANTALLA JUEGO ─────────────────────────────────────
    def _build_juego(self):
        self._clear()

        # Stats bar
        sf = tk.Frame(self.container, bg=C["page"])
        sf.pack(fill="x", pady=(0, 8))

        nombre_text = self.nombre[:14] + "…" if len(self.nombre) > 14 else self.nombre
        self._lbl_nombre = tk.Label(sf, text=f"🦊 {nombre_text}",
                                    font=self.f_badge, bg=C["orange_dk"],
                                    fg=C["white"], padx=10, pady=5)
        self._lbl_nombre.pack(side="left", padx=(0, 5))

        self._lbl_pts = tk.Label(sf, text=f"🔥 {self.puntos} pts",
                                 font=self.f_badge, bg=C["card2"],
                                 fg=C["gold"], padx=10, pady=5)
        self._lbl_pts.pack(side="left", padx=(0, 5))

        self._lbl_vidas = tk.Label(sf, text=f"♥ {self.vidas}",
                                   font=self.f_badge, bg=C["danger"],
                                   fg=C["white"], padx=10, pady=5)
        self._lbl_vidas.pack(side="left", padx=(0, 5))

        self._lbl_racha = tk.Label(sf, text=f"⚡ ×{self.racha}",
                                   font=self.f_badge, bg=C["card2"],
                                   fg=C["orange_lt"], padx=10, pady=5)
        self._lbl_racha.pack(side="left")

        # Dots de nivel
        dots_f = tk.Frame(self.container, bg=C["page"])
        dots_f.pack(fill="x", pady=(0, 5))
        self._dots = []
        for i in range(len(NIVELES)):
            dot = tk.Frame(dots_f, height=7, bg=C["border"])
            dot.pack(side="left", fill="x", expand=True, padx=2)
            self._dots.append(dot)
        self._update_dots()

        # Barra de progreso
        prog_out = tk.Frame(self.container, bg=C["border"], height=8)
        prog_out.pack(fill="x", pady=(0, 12))
        prog_out.pack_propagate(False)
        self._prog_inner = tk.Frame(prog_out, bg=C["orange"], height=8)
        self._prog_inner.place(x=0, y=0, relheight=1, relwidth=0)
        self._update_progreso()

        # Card principal
        card = tk.Frame(self.container, bg=C["card"],
                        highlightbackground=C["orange"],
                        highlightthickness=1)
        card.pack(fill="x", padx=2)
        inner = tk.Frame(card, bg=C["card"])
        inner.pack(fill="both", padx=20, pady=18)

        # Zorro + tema
        top = tk.Frame(inner, bg=C["card"])
        top.pack(fill="x", pady=(0, 12))

        self._zorro_game = ZorroCanvas(top, size=76, bg=C["card"])
        self._zorro_game.pack(side="left", padx=(0, 14))

        right = tk.Frame(top, bg=C["card"])
        right.pack(side="left", fill="both", expand=True)

        self._lbl_tema = tk.Label(right, text="", font=self.f_badge,
                                  bg=C["orange_dk"], fg=C["white"],
                                  padx=10, pady=4)
        self._lbl_tema.pack(anchor="w", pady=(4, 6))

        self._lbl_pregunta = tk.Label(right, text="", font=self.f_bold,
                                      bg=C["card"], fg=C["snow"],
                                      wraplength=310, justify="left")
        self._lbl_pregunta.pack(anchor="w")

        tk.Frame(inner, bg=C["border"], height=1).pack(fill="x", pady=10)

        # Opciones
        self._opts_frame = tk.Frame(inner, bg=C["card"])
        self._opts_frame.pack(fill="x")
        self._opcion_btns = []

        # Feedback
        self._fb_var = tk.StringVar()
        self._fb_label = tk.Label(inner, textvariable=self._fb_var,
                                  font=self.f_sm, bg=C["hint"],
                                  fg=C["hint_txt"],
                                  wraplength=430, justify="left",
                                  padx=14, pady=10)

        # Botones acción
        btn_row = tk.Frame(inner, bg=C["card"])
        btn_row.pack(fill="x", pady=(12, 0))

        self._btn_pista = RoundButton(btn_row, "🔥 Pista (−15 pts)",
                                      self._usar_pista,
                                      width=165, height=40, radius=12,
                                      bg=C["card2"], hover_bg=C["border"],
                                      fg=C["muted"], font_obj=self.f_sm, canvas_bg=C["card"])
        self._btn_pista.pack(side="left")

        self._btn_sig = RoundButton(btn_row, "Siguiente →",
                                    self._siguiente,
                                    width=270, height=40, radius=12,
                                    bg=C["orange"], hover_bg=C["fire"],
                                    fg=C["white"], font_obj=self.f_bold, canvas_bg=C["card"])
        self._btn_sig.pack(side="right")
        self._btn_sig.set_state(False)

        self._card_inner = inner
        self._cargar_pregunta()

    # ──────── PANTALLA FIN ───────────────────────────────────────
    def _build_fin(self, gano):
        self._clear()

        zorro = ZorroCanvas(self.container, size=160, bg=C["page"])
        zorro.pack(pady=(10, 0))
        zorro.set_happy() if gano else zorro.set_sad()

        card = tk.Frame(self.container, bg=C["card"],
                        highlightbackground=C["orange"] if gano else C["danger"],
                        highlightthickness=2)
        card.pack(fill="x", pady=14, padx=4)
        inner = tk.Frame(card, bg=C["card"])
        inner.pack(fill="both", padx=26, pady=22)

        titulo = "¡Victoria! 🏆" if gano else "Game Over 💀"
        color_t = C["orange_lt"] if gano else C["danger"]
        tk.Label(inner, text=titulo, font=self.f_title,
                 bg=C["card"], fg=color_t).pack()

        msg = (
            f"¡Completaste todos los niveles, {self.nombre}!\n"
            f"Cody el Zorro está muy orgulloso de ti. 🦊🔥"
            if gano else
            f"Sin vidas, {self.nombre}.\n"
            f"Cody confía en que lo intentarás de nuevo."
        )
        tk.Label(inner, text=msg, font=self.f_body,
                 bg=C["card"], fg=C["snow"], justify="center",
                 wraplength=400).pack(pady=10)

        # Puntos
        tk.Label(inner, text=str(self.puntos),
                 font=self.f_huge, bg=C["card"],
                 fg=C["orange_lt"]).pack()
        tk.Label(inner, text="puntos de fuego 🔥",
                 font=self.f_sm, bg=C["card"], fg=C["muted"]).pack(pady=(0, 6))

        # Mejor racha
        if self.mejor_racha >= 2:
            tk.Label(inner,
                     text=f"⚡ Mejor racha: {self.mejor_racha} respuestas seguidas",
                     font=self.f_sm, bg=C["card"], fg=C["gold"]).pack(pady=(0, 14))

        self._fire_separator()

        RoundButton(self.container, "Jugar de nuevo 🦊",
                    self._reiniciar, width=320, height=50,
                    radius=16, bg=C["orange"], hover_bg=C["fire"],
                    fg=C["white"], font_obj=self.f_h2, canvas_bg=C["page"]).pack(pady=(0, 10))

        # ── Pantalla de créditos ──
        self._fire_separator()
        cr_card = tk.Frame(self.container, bg=C["card"],
                           highlightbackground=C["border"],
                           highlightthickness=1)
        cr_card.pack(fill="x", padx=4, pady=(0, 12))
        cr_inner = tk.Frame(cr_card, bg=C["card"])
        cr_inner.pack(fill="both", padx=20, pady=14)

        tk.Label(cr_inner, text="🎬  Créditos",
                 font=self.f_h2, bg=C["card"], fg=C["orange_lt"]).pack()

        tk.Frame(cr_inner, bg=C["border"], height=1).pack(fill="x", pady=8)

        autores = [
            ("👨‍💻", "David Mutis"),
            ("👨‍💻", "Sebastián Durán"),
            ("👨‍💻", "Juan Pablo López"),
        ]
        for emoji, nombre in autores:
            fila = tk.Frame(cr_inner, bg=C["card"])
            fila.pack(fill="x", pady=2)
            tk.Label(fila, text=emoji + "  " + nombre,
                     font=self.f_body, bg=C["card"], fg=C["snow"]).pack(side="left")

        tk.Frame(cr_inner, bg=C["border"], height=1).pack(fill="x", pady=8)

        tk.Label(cr_inner,
                 text="© 2026 — Todos los derechos reservados",
                 font=self.f_sm, bg=C["card"], fg=C["muted"]).pack()
        tk.Label(cr_inner,
                 text="Software educativo desarrollado para la asignatura de POO",
                 font=self.f_sm, bg=C["card"], fg=C["muted"]).pack(pady=(2, 0))
        tk.Label(cr_inner,
                 text="Zorro Cody dibujado con tkinter Canvas — Python 3.8+",
                 font=self.f_sm, bg=C["card"], fg=C["border"]).pack(pady=(2, 0))

    # ──────── LÓGICA DEL JUEGO ───────────────────────────────────
    def _empezar(self):
        n = self._nombre_var.get().strip()
        self.nombre = n if n else "Estudiante"
        self.puntos = 0
        self.vidas  = 3
        self.nivel  = 0
        self.pregunta_idx = 0
        self.respondido   = False
        self.racha        = 0
        self.mejor_racha  = 0
        self._build_juego()

    def _reiniciar(self):
        self._build_inicio()

    def _cargar_pregunta(self):
        self.respondido = False
        nv = NIVELES[self.nivel]
        p  = nv["preguntas"][self.pregunta_idx]

        self._lbl_tema.config(text=f"  {nv['tema']}  ")
        self._lbl_pregunta.config(text=p["e"])
        self._fb_label.pack_forget()
        self._btn_sig.set_state(False)
        self._zorro_game.set_neutral()

        for w in self._opcion_btns:
            w.destroy()
        self._opcion_btns.clear()

        for i, op in enumerate(p["ops"]):
            btn = OpcionBtn(self._opts_frame, LETRAS[i], op,
                            lambda idx=i: self._responder(idx),
                            width=480)
            btn.pack(pady=4)
            self._opcion_btns.append(btn)

        self._update_dots()
        self._update_progreso()

    def _responder(self, idx):
        if self.respondido:
            return
        self.respondido = True
        p = NIVELES[self.nivel]["preguntas"][self.pregunta_idx]

        for b in self._opcion_btns:
            b.disable()
        self._opcion_btns[p["c"]].set_state("ok")

        if idx == p["c"]:
            self.racha += 1
            bonus = 20 if self.racha >= 3 else (10 if self.racha == 2 else 0)
            base  = 50
            self.puntos += base + bonus
            if self.racha > self.mejor_racha:
                self.mejor_racha = self.racha
            msg = f"¡Correcto! +{base} pts 🔥"
            if bonus:
                msg += f"  ⚡ ¡RACHA ×{self.racha}! +{bonus} pts extra!"
            self._fb_var.set(msg)
            self._fb_label.config(bg=C["success_l"], fg=C["success"])
            self._zorro_game.set_happy()
        else:
            self.racha = 0
            self._opcion_btns[idx].set_state("mal")
            self.vidas -= 1
            self._fb_var.set(
                f"Incorrecto 💀  Respuesta correcta: \"{p['ops'][p['c']]}\"\n"
                f"Perdiste una vida. Racha reiniciada."
            )
            self._fb_label.config(bg=C["danger_l"], fg=C["danger"])
            self._zorro_game.set_sad()

        self._fb_label.pack(fill="x", pady=(10, 0))
        self._update_stats()

        es_ult_p = self.pregunta_idx >= len(NIVELES[self.nivel]["preguntas"]) - 1
        es_ult_n = self.nivel >= len(NIVELES) - 1

        if self.vidas <= 0:
            self._btn_sig._text = "Ver resultado"
            self._btn_sig._cmd_actual = lambda: self._build_fin(False)
        elif es_ult_p and es_ult_n:
            self._btn_sig._text = "¡Ver resultado final! 🏆"
            self._btn_sig._cmd_actual = lambda: self._build_fin(True)
        elif es_ult_p:
            self._btn_sig._text = f"Nivel {self.nivel + 2} →"
            self._btn_sig._cmd_actual = self._avanzar_nivel
        else:
            self._btn_sig._text = "Siguiente pregunta →"
            self._btn_sig._cmd_actual = self._avanzar_pregunta

        self._btn_sig._bg  = C["orange"]
        self._btn_sig._cmd = self._btn_sig._cmd_actual
        self._btn_sig.set_state(True)

    def _siguiente(self): pass

    def _avanzar_pregunta(self):
        self.pregunta_idx += 1
        self._cargar_pregunta()

    def _avanzar_nivel(self):
        self.nivel += 1
        self.pregunta_idx = 0
        # Mostrar minijuego entre niveles (hay 2 transiciones para 3 niveles)
        ronda_idx = self.nivel - 1
        if ronda_idx < len(MEMORY_RONDAS):
            self._build_minijuego(ronda_idx)
        else:
            self._cargar_pregunta()

    def _usar_pista(self):
        if self.respondido:
            return
        p = NIVELES[self.nivel]["preguntas"][self.pregunta_idx]
        if self.puntos >= 15:
            self.puntos -= 15
            self._update_stats()
            self._fb_var.set(f"💡 Pista de Cody: {p['p']}")
            self._fb_label.config(bg=C["hint"], fg=C["hint_txt"])
            self._fb_label.pack(fill="x", pady=(10, 0))
        else:
            self._fb_var.set("No tienes suficientes puntos para una pista (cuesta 15 pts 🔥).")
            self._fb_label.config(bg=C["danger_l"], fg=C["danger"])
            self._fb_label.pack(fill="x", pady=(10, 0))


    # ──────── MINIJUEGO MEMORY ───────────────────────────────────
    def _build_minijuego(self, ronda_idx):
        """Memory: 8 cartas boca abajo, voltea de 2 en 2.
           Cada par comparte color de fondo. Concepto + Definicion."""
        self._clear()
        ronda = MEMORY_RONDAS[ronda_idx]

        # ── Header ──
        tk.Label(self.container, text="🃏  MINIJUEGO  🃏",
                 font=self.f_badge, bg=C["page"], fg=C["gold"]).pack(pady=(8, 0))
        tk.Label(self.container, text=ronda["titulo"],
                 font=self.f_h2, bg=C["page"], fg=C["orange_lt"]).pack(pady=(2, 0))
        tk.Label(self.container,
                 text="Voltea 2 cartas: si son del mismo concepto forman pareja",
                 font=self.f_sm, bg=C["page"], fg=C["muted"]).pack(pady=(2, 6))

        # ── Stats del minijuego ──
        sf = tk.Frame(self.container, bg=C["page"])
        sf.pack()
        self._mg_lbl_intentos = tk.Label(sf, text="Intentos: 0",
                                          font=self.f_badge, bg=C["card2"],
                                          fg=C["snow"], padx=10, pady=4)
        self._mg_lbl_intentos.pack(side="left", padx=4)
        self._mg_lbl_pares = tk.Label(sf, text="Parejas: 0/4",
                                       font=self.f_badge, bg=C["card2"],
                                       fg=C["gold"], padx=10, pady=4)
        self._mg_lbl_pares.pack(side="left", padx=4)

        # ── Zorro ──
        self._zorro_mini = ZorroCanvas(self.container, size=60, bg=C["page"])
        self._zorro_mini.pack(pady=(4, 0))
        self._zorro_mini.set_neutral()

        # ── Feedback ──
        self._mg_fb = tk.Label(self.container, text="¡Haz clic en dos cartas!",
                               font=self.f_sm, bg=C["page"], fg=C["hint_txt"])
        self._mg_fb.pack(pady=(4, 8))

        # ── Estado del juego ──
        pares = list(ronda["pares"])          # [(concepto, definicion), ...]
        # Construir lista de 8 cartas: para cada par, carta A=concepto, carta B=definicion
        # Ambas cartas del mismo par tienen el mismo color de fondo
        cartas_data = []
        for i, (concepto, definicion) in enumerate(pares):
            color = COLORES_PAR[i % len(COLORES_PAR)]
            cartas_data.append({"texto": concepto,    "par_id": i, "color": color, "tipo": "C"})
            cartas_data.append({"texto": definicion,  "par_id": i, "color": color, "tipo": "D"})
        random.shuffle(cartas_data)

        self._mg_cartas_data   = cartas_data   # info de cada carta
        self._mg_volteadas     = []            # índices de cartas volteadas actualmente
        self._mg_encontradas   = set()         # par_ids ya emparejados
        self._mg_bloqueado     = False         # bloqueo durante animacion
        self._mg_intentos      = 0
        self._mg_errores       = 0
        self._mg_canvas_cartas = []            # widgets Canvas de cada carta

        # ── Tablero 4×2 de cartas ──
        tablero = tk.Frame(self.container, bg=C["page"])
        tablero.pack(padx=10, pady=4)

        CW, CH = 118, 90   # ancho y alto de cada carta

        for i, carta in enumerate(cartas_data):
            fila = i // 4
            col  = i %  4
            cv = tk.Canvas(tablero, width=CW, height=CH,
                           bg=C["page"], highlightthickness=0, cursor="hand2")
            cv.grid(row=fila, column=col, padx=5, pady=5)
            self._mg_canvas_cartas.append(cv)
            self._mg_dibujar_dorso(cv, CW, CH)
            cv.bind("<Button-1>", lambda e, idx=i: self._mg_click_carta(idx))

        # ── Botón saltar ──
        tk.Button(self.container, text="Saltar →",
                  font=self.f_sm, bg=C["border"], fg=C["muted"],
                  relief="flat", cursor="hand2", bd=0,
                  command=self._mg_terminar).pack(pady=(8, 4))

    def _mg_dibujar_dorso(self, cv, w=118, h=90):
        """Carta boca abajo: fondo oscuro con patron y simbolo ?"""
        cv.delete("all")
        # Fondo
        cv.create_rectangle(2, 2, w-2, h-2, fill=C["card2"],
                            outline=C["orange"], width=2)
        # Patron de rombos decorativo
        for x in range(10, w-5, 18):
            for y in range(10, h-5, 18):
                cv.create_text(x, y, text="◆", fill=C["border"],
                               font=("Helvetica", 8))
        # Simbolo central
        cv.create_text(w//2, h//2 - 6, text="🦊",
                       font=("Helvetica", 18))
        cv.create_text(w//2, h//2 + 16, text="?",
                       fill=C["orange"], font=("Helvetica", 14, "bold"))

    def _mg_dibujar_frente(self, cv, carta, w=118, h=90):
        """Carta boca arriba: color del par + texto."""
        cv.delete("all")
        color = carta["color"]
        # Fondo coloreado
        cv.create_rectangle(2, 2, w-2, h-2, fill=color,
                            outline=C["white"], width=2)
        # Etiqueta tipo
        tipo_txt = "CONCEPTO" if carta["tipo"] == "C" else "DEFINICION"
        tipo_col = C["white"] if carta["tipo"] == "C" else "#ffe0a0"
        cv.create_rectangle(2, 2, w-2, 18, fill=color, outline="")
        cv.create_text(w//2, 11, text=tipo_txt, fill=tipo_col,
                       font=("Helvetica", 7, "bold"))
        # Texto principal
        cv.create_text(w//2, h//2 + 8, text=carta["texto"],
                       fill=C["white"], font=("Helvetica", 9, "bold"),
                       width=w-14, justify="center")

    def _mg_dibujar_encontrada(self, cv, carta, w=118, h=90):
        """Carta emparejada: verde con check."""
        cv.delete("all")
        cv.create_rectangle(2, 2, w-2, h-2, fill=C["success_l"],
                            outline=C["success"], width=2)
        cv.create_text(w//2, h//2 - 10, text="✓",
                       fill=C["success"], font=("Helvetica", 22, "bold"))
        cv.create_text(w//2, h//2 + 16, text=carta["texto"],
                       fill=C["success"], font=("Helvetica", 8),
                       width=w-14, justify="center")

    def _mg_click_carta(self, idx):
        """Maneja el clic sobre una carta."""
        if self._mg_bloqueado:
            return
        carta = self._mg_cartas_data[idx]
        # Ignorar si ya emparejada o ya volteada
        if carta["par_id"] in self._mg_encontradas:
            return
        if idx in self._mg_volteadas:
            return
        # Voltear carta
        cv = self._mg_canvas_cartas[idx]
        self._mg_dibujar_frente(cv, carta)
        self._mg_volteadas.append(idx)

        if len(self._mg_volteadas) == 2:
            self._mg_intentos += 1
            self._mg_lbl_intentos.config(text="Intentos: " + str(self._mg_intentos))
            self._mg_bloqueado = True
            self.container.after(900, self._mg_evaluar_par)

    def _mg_evaluar_par(self):
        """Comprueba si las 2 cartas volteadas forman pareja."""
        i1, i2 = self._mg_volteadas
        c1 = self._mg_cartas_data[i1]
        c2 = self._mg_cartas_data[i2]

        if c1["par_id"] == c2["par_id"]:
            # ✅ Pareja correcta
            self._mg_encontradas.add(c1["par_id"])
            self._mg_dibujar_encontrada(self._mg_canvas_cartas[i1], c1)
            self._mg_dibujar_encontrada(self._mg_canvas_cartas[i2], c2)
            self._mg_fb.config(text="✅ ¡Pareja encontrada! Buen trabajo",
                               fg=C["success"])
            self._zorro_mini.set_happy()
            n = len(self._mg_encontradas)
            total = len(self._mg_cartas_data) // 2
            self._mg_lbl_pares.config(text="Parejas: " + str(n) + "/" + str(total))
            if n == total:
                bonus = max(0, 100 - self._mg_errores * 12)
                self.puntos += bonus
                self._mg_fb.config(
                    text="🎉 ¡Completado! +" + str(bonus) + " pts de bonus 🔥",
                    fg=C["gold"])
                self.container.after(1800, self._mg_terminar)
        else:
            # ❌ No son pareja
            self._mg_errores += 1
            self._mg_fb.config(text="❌ No son pareja, sigue intentando",
                               fg=C["danger"])
            self._zorro_mini.set_sad()
            # Tapar las cartas de nuevo
            self.container.after(200, lambda: (
                self._mg_dibujar_dorso(self._mg_canvas_cartas[i1]),
                self._mg_dibujar_dorso(self._mg_canvas_cartas[i2])
            ))

        self._mg_volteadas = []
        self._mg_bloqueado = False

    def _mg_terminar(self):
        """Terminar el minijuego y continuar al siguiente nivel."""
        self._build_juego()
        self.container.after(100, self._cargar_pregunta)


    # ──────── PANTALLA ACERCA DE ─────────────────────────────────
    def _build_acerca(self):
        self._clear()

        tk.Label(self.container, text="📖  Acerca de Foxy Memory",
                 font=self.f_title, bg=C["page"], fg=C["orange_lt"]).pack(pady=(14, 6))

        self._fire_separator()

        card = tk.Frame(self.container, bg=C["card"],
                        highlightbackground=C["orange"], highlightthickness=1)
        card.pack(fill="x", padx=4, pady=6)
        inner = tk.Frame(card, bg=C["card"])
        inner.pack(fill="both", padx=22, pady=18)

        secciones = [
            ("🎯 Propósito",
             "Foxy Memory es un juego educativo desarrollado en Python con tkinter,\n"
             "cuyo objetivo es enseñar los conceptos fundamentales de la\n"
             "Programación Orientada a Objetos (POO) de forma interactiva y divertida."),

            ("🧠 ¿Qué aprenderás?",
             "• Clases y Objetos: qué son y cómo se relacionan\n"
             "• Herencia y Polimorfismo: reutilización y flexibilidad del código\n"
             "• Encapsulamiento y Abstracción: protección y simplificación"),

            ("🎮 ¿Cómo se juega?",
             "El juego tiene 3 niveles de preguntas de opción múltiple.\n"
             "Entre niveles aparece un minijuego de Memory donde emparejas\n"
             "conceptos POO con sus definiciones. Gana puntos respondiendo\n"
             "correctamente y construyendo rachas de respuestas seguidas."),

            ("🛠️ Tecnología",
             "Lenguaje: Python 3.8+\n"
             "Interfaz gráfica: tkinter (incluido en Python)\n"
             "Gráficos: dibujados con Canvas (sin imágenes externas)\n"
             "Sin dependencias adicionales — funciona directo en Thonny"),
        ]

        for titulo, texto in secciones:
            tk.Label(inner, text=titulo, font=self.f_h2,
                     bg=C["card"], fg=C["orange_lt"], anchor="w").pack(fill="x", pady=(10, 2))
            tk.Label(inner, text=texto, font=self.f_sm,
                     bg=C["card"], fg=C["snow"], justify="left",
                     wraplength=460, anchor="w").pack(fill="x", padx=8)
            tk.Frame(inner, bg=C["border"], height=1).pack(fill="x", pady=(8, 0))

        self._fire_separator()

        RoundButton(self.container, "← Volver al inicio",
                    self._build_inicio, width=280, height=44,
                    radius=14, bg=C["card2"], hover_bg=C["orange"],
                    fg=C["snow"], font_obj=self.f_bold,
                    canvas_bg=C["page"]).pack(pady=8)

    # ──────── PANTALLA BITÁCORA ───────────────────────────────────
    def _build_bitacora(self):
        self._clear()

        tk.Label(self.container, text="📋  Bitácora de Desarrollo",
                 font=self.f_title, bg=C["page"], fg=C["orange_lt"]).pack(pady=(14, 6))

        self._fire_separator()

        entradas = [
            ("v1.0", "Diseño inicial",
             "Estructura base del juego: pantallas de inicio, juego y fin.\n"
             "Sistema de preguntas de opción múltiple con 3 niveles POO.\n"
             "Paleta de colores oscura (modo noche) con tema naranja/fuego."),

            ("v1.1", "Corrección de errores en Windows/Thonny",
             "Bug crítico: self._w sobreescribía el atributo interno de\n"
             "tk.Canvas causando TclError 'invalid command name 480'.\n"
             "Solución: renombrar a self._btn_w y usar after(10, self._draw)\n"
             "para diferir el primer dibujo hasta que el widget esté listo."),

            ("v1.2", "Sistema de rachas y puntuación mejorada",
             "Se agregó contador de rachas consecutivas con bonus de puntos:\n"
             "+10 pts en racha ×2, +20 pts en racha ×3 o más.\n"
             "La mejor racha se muestra en la pantalla de resultados.\n"
             "Preguntas ampliadas: 4 por nivel (12 en total)."),

            ("v1.3", "Minijuego Memory entre niveles",
             "Se diseñó e integró un minijuego de cartas estilo Memory\n"
             "que aparece en las transiciones entre niveles.\n"
             "8 cartas boca abajo (4 pares): cada par comparte el mismo\n"
             "color de fondo. El jugador voltea 2 cartas por turno.\n"
             "Bonus de hasta +100 pts según errores cometidos."),

            ("v1.4", "Derechos de autor y créditos",
             "Se añadieron créditos oficiales en docstring, pantalla de\n"
             "inicio y pantalla final. Autores: David Mutis,\n"
             "Sebastián Durán y Juan Pablo López. © 2026."),

            ("v1.5", "Propósito y Bitácora (versión actual)",
             "Pantalla 'Acerca de' con propósito educativo, mecánicas\n"
             "y tecnología. Bitácora de desarrollo integrada en el juego.\n"
             "Botones de navegación en pantalla de inicio."),
        ]

        for version, titulo, desc in entradas:
            fila = tk.Frame(self.container, bg=C["card"],
                            highlightbackground=C["border"], highlightthickness=1)
            fila.pack(fill="x", padx=4, pady=4)
            inner = tk.Frame(fila, bg=C["card"])
            inner.pack(fill="both", padx=16, pady=10)

            header = tk.Frame(inner, bg=C["card"])
            header.pack(fill="x")
            tk.Label(header, text=version,
                     font=self.f_badge, bg=C["orange_dk"],
                     fg=C["white"], padx=8, pady=3).pack(side="left")
            tk.Label(header, text="  " + titulo,
                     font=self.f_bold, bg=C["card"],
                     fg=C["orange_lt"]).pack(side="left", padx=8)

            tk.Label(inner, text=desc, font=self.f_sm,
                     bg=C["card"], fg=C["snow"], justify="left",
                     wraplength=460, anchor="w").pack(fill="x", pady=(6, 0))

        self._fire_separator()

        RoundButton(self.container, "← Volver al inicio",
                    self._build_inicio, width=280, height=44,
                    radius=14, bg=C["card2"], hover_bg=C["orange"],
                    fg=C["snow"], font_obj=self.f_bold,
                    canvas_bg=C["page"]).pack(pady=8)

    # ──────── HELPERS ────────────────────────────────────────────
    def _clear(self):
        for w in self.container.winfo_children():
            w.destroy()

    def _update_stats(self):
        if hasattr(self, "_lbl_pts"):
            self._lbl_pts.config(text=f"🔥 {self.puntos} pts")
        if hasattr(self, "_lbl_vidas"):
            self._lbl_vidas.config(text=f"♥ {self.vidas}")
        if hasattr(self, "_lbl_racha"):
            self._lbl_racha.config(text=f"⚡ ×{self.racha}")

    def _update_dots(self):
        if not hasattr(self, "_dots"):
            return
        for i, dot in enumerate(self._dots):
            if i < self.nivel:
                dot.config(bg=C["orange_dk"])
            elif i == self.nivel:
                dot.config(bg=C["orange"])
            else:
                dot.config(bg=C["border"])

    def _update_progreso(self):
        if not hasattr(self, "_prog_inner"):
            return
        total = sum(len(nv["preguntas"]) for nv in NIVELES)
        hecho = sum(len(NIVELES[i]["preguntas"]) for i in range(self.nivel)) + self.pregunta_idx
        self._prog_inner.place(x=0, y=0, relheight=1, relwidth=hecho/total)

    def _fire_separator(self):
        sf = tk.Frame(self.container, bg=C["page"])
        sf.pack(fill="x", pady=8)
        tk.Frame(sf, bg=C["orange"], height=2).pack(
            fill="x", side="left", expand=True, pady=8)
        tk.Label(sf, text=" 🦊 ", font=self.f_sm,
                 bg=C["page"], fg=C["orange"]).pack(side="left")
        tk.Frame(sf, bg=C["orange"], height=2).pack(
            fill="x", side="left", expand=True, pady=8)


# ─── ENTRY POINT ─────────────────────────────────────────────────
if __name__ == "__main__":
    app = ZorroPOO()
    app.mainloop()
