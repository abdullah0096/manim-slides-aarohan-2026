import numpy as np

from manim import *
from manim_slides import Slide

from cryptologySlide import *
from utils import *
from piryamid import *

# ═══════════════════════════════════════════════════════════════
#  UNIFIED PALETTE  — gold / dark theme used across all slides
# ═══════════════════════════════════════════════════════════════
SLIDE_BG       = "#000000"          # default background

# Primary accent (gold family — matches pyramid & QuantumThreat)
C_GOLD         = "#D4AA50"
C_GOLD_BRIGHT  = "#F5D87A"
C_GOLD_DIM     = "#8A6015"

# Neutral text
C_WHITE        = "#E8E8E8"
C_GREY         = "#888888"
C_DARK_PANEL   = "#111111"

# Semantic accents (used sparingly for contrast)
# C_BLUE         = "#5599E0"
C_BLUE         = YELLOW_D
C_RED          = "#E05555"
C_GREEN        = "#55C477"
C_ORANGE       = "#F7931A"
C_TEAL         = "#56D4B0"

# ── Standard font sizes ──────────────────────────────────────
FS_TITLE       = 48      # slide titles
FS_SUBTITLE    = 32      # sub-headings
FS_BODY        = 28      # main body text
FS_LABEL       = 24      # labels, captions
FS_SMALL       = 20      # small annotations
FS_TINY        = 16      # footnotes, axis labels

DOTCOLOR = WHITE
def plotDotTL(s):
    dot = Dot(color=DOTCOLOR).to_corner(UL).scale(0.1)
    s.play(FadeIn(dot), run_time=0.1)
    s.play(FadeOut(dot), run_time=0.1)

class Title(Slide):
    def construct(self):
        self.camera.background_color = SLIDE_BG
        # Create banner with gold accent
        banner = RoundedRectangle(
            width=13,
            height=2,
            corner_radius=0.2,
            fill_color=C_DARK_PANEL,
            fill_opacity=1,
            stroke_color=C_GOLD,
            stroke_width=2
        )
        banner.shift(UP * 2)
        
        self.next_slide(loop=True)
        # Main title
        main_title = Tex("Modern Cryptography, ECDLP \& Quantum Computers", font_size=FS_TITLE, color=C_GOLD_BRIGHT)
        main_title.move_to(banner.get_center() + UP * 0.2)
        # self.play(FadeIn(banner))
        self.play(FadeIn(banner), Write(main_title), run_time=3)
        # self.next_slide()
        
        # Lecture subtitle
        subTitle = Tex("Present and future", font_size=FS_LABEL, color=WHITE_T)
        subTitle.next_to(main_title, DOWN, buff=0.3)
        self.play(FadeIn(subTitle))
        
        # Author name
        author = Text("Dr. Abdullah Ansari", font_size=FS_SUBTITLE+4, color=C_WHITE)
        author.next_to(banner, DOWN, buff=0.7)
        self.play(Write(author))

        # Department info
        dept1 = Tex(
            "Aarohan 2026 - DES PU",
            font_size=FS_SMALL+26,
            color=C_GOLD
        )
        dept1.next_to(author, DOWN, buff=0.5)
        self.play(Write(dept1), run_time = 5)
        self.wait(2)
        self.next_slide()
        
        university = Tex(
            "Department of Scientific Computing, Modeling and Simulation - SPPU",
            font_size=FS_TINY+2,
            color=C_GOLD_BRIGHT
        )
        university.to_edge(DOWN)
        
        dept2 = Tex(
            "23rd February 2026",
            font_size=FS_SMALL,
            color=C_GOLD
        )
        dept2.next_to(university, UP, buff=0.2)
        
        issc = Tex(r'Formerly - Interdisciplinary School of Scientific Computing', font_size=18)
        issc.next_to(university, DOWN, buff=0.2)
        self.play(FadeIn(university), Write(dept2), Write(issc), run_time=2.3)
        plotDotTL(self)

        self.next_slide()

# Aim : Setup the context of the talk by starting from a point already known the the audiance
#       i.e. using examples that are popular and relatable to the audiance. 
class Introduction(Slide):
    def construct(self):
        self.camera.background_color = SLIDE_BG
        txt1 = Tex(r"\textbf{6,000,000,000+} \\ \textbf{Internet user}", color=C_BLUE).scale(1.6)
        txt2 = Tex(r"\textbf{20,000,000,000+} \\ \textbf{Connected devices}", color=ORANGE).scale(1.8)

        self.play(Write(txt1), run_time=2)
        self.next_slide()

        # scale down txt1 and translate it up
        self.play(txt1.animate.scale(0.5).shift(UP*2), run_time=2)
        self.play(FadeOut(txt1), Write(txt2), run_time=2)
        self.next_slide()

        self.play(txt2.animate.scale(0.8).shift(UP*2), FadeOut(txt2))
        img_yt = SVGMobject("images/yt_icon.svg").scale_to_fit_width(2.5)
        self.play(FadeIn(img_yt))
        yt_text = Tex(r"2.7+ Billion", font_size=FS_LABEL, color=C_WHITE).next_to(img_yt, DOWN)
        self.play(Write(yt_text))

        ytGrp = VGroup()
        ytGrp.add(img_yt, yt_text)
        self.play(ytGrp.animate.shift(LEFT*5))
        c
        img_fb = ImageMobject("images/facebook.png").scale_to_fit_width(1.6)
        img_whatsApp = SVGMobject("images/WhatsApp.svg").scale_to_fit_width(1.6).next_to(img_fb, RIGHT)
        img_insta = ImageMobject("images/Instagram_.webp").scale_to_fit_width(1.6).next_to(img_whatsApp, RIGHT)

        metaGrp = Group()
        metaGrp.add(img_whatsApp, img_insta, img_fb)
        self.play(FadeIn(metaGrp))

        #make a box around the metaGrp
        box = SurroundingRectangle(metaGrp, color=C_BLUE, buff=0.2)
        self.play(Create(box))
        meta_txt = Tex(r"3.9+ Billion", font_size=FS_LABEL, color=C_WHITE).next_to(metaGrp, DOWN, buff=0.3)
        self.play(Write(meta_txt))
        self.play(FadeOut(box))

        self.next_slide()
        
        self.play(metaGrp.animate.shift(LEFT*2.4), meta_txt.animate.shift(LEFT*2))

        img_upi = ImageMobject("images/upi2.png").scale_to_fit_width(3.2)
        upi_text = Tex(r"500+ Million", font_size=FS_LABEL, color=C_WHITE).next_to(img_upi, DOWN, buff=0.3)
        upiGrp = Group()
        upiGrp.add(img_upi, upi_text).next_to(metaGrp, RIGHT, buff=1).shift(DOWN*0.4)

        self.play(FadeIn(upiGrp))

        self.next_slide()

        # fade out everything except img_whatsapp
        self.play(
            FadeOut(img_yt),
            FadeOut(yt_text),
            FadeOut(img_fb),
            FadeOut(img_insta),
            FadeOut(img_upi),
            FadeOut(upi_text),
            FadeOut(meta_txt)
        )

        # move whats app to the center and print End to end encryption below it
        self.play(img_whatsApp.animate.scale(2.5).move_to(ORIGIN))
        e2e_text = Tex(r"End to End Encryption", font_size=FS_TITLE+8, color=C_GREEN).next_to(img_whatsApp, DOWN, buff=0.3)
        self.play(Write(e2e_text))
      
        self.next_slide()

        # fade out e2e_text and img_whatsAPP
        self.play(FadeOut(e2e_text), FadeOut(img_whatsApp))

        # why 
        why = Tex(r"WHY ?", font_size=72, color=RED)
        self.play(Write(why))        
        
        self.next_slide()

# Aim : Show message sharing over insecure communication channel
class InsecureChannel(Slide):
    def construct(self):
        self.camera.background_color = SLIDE_BG
        # make Alice appear on the top left corner
        img_alice = ImageMobject("images/d2.png").scale_to_fit_width(1).to_corner(UL).shift(LEFT * 0.3 + UP * 0.3)
        txt_alice = Tex(r"Alice", font_size=FS_LABEL+12, color=C_BLUE).next_to(img_alice, DOWN, buff=0.1)
        self.play(FadeIn(img_alice), FadeIn(txt_alice))   
        self.next_slide()

        # make Bob appear on the bottom right corner
        img_bob = ImageMobject("images/d2.png").scale_to_fit_width(1).to_corner(DR).shift(RIGHT * 0.3)
        txt_bob = Tex(r"Bob", font_size=FS_LABEL+12, color=C_BLUE).next_to(img_bob, DOWN, buff=0.1)
        self.play(FadeIn(img_bob), FadeIn(txt_bob))  
        self.next_slide()

        # make whatsApp appear in the center of the screen called whatsapp_server with a bounding box around it
        img_whatsApp = SVGMobject("images/WhatsApp.svg").scale_to_fit_width(1)
        txt_whatsApp = Tex(r"Server", font_size=FS_LABEL).next_to(img_whatsApp, DOWN, buff=0.1)
        whatsApp_grp = VGroup()
        whatsApp_grp.add(img_whatsApp, txt_whatsApp)
        box = SurroundingRectangle(whatsApp_grp, color=C_GREEN, buff=0.15)
        self.play(FadeIn(img_whatsApp), FadeIn(txt_whatsApp))
        self.play(Create(box))
        self.next_slide()

        # connect Alice to a cell tower called alice_tower
        img_aliceTower = ImageMobject("images/cell_tower.png").scale_to_fit_width(1)
        img_aliceTower.to_edge(UP).shift(UP * 0.3)
        self.play(FadeIn(img_aliceTower)) 
        self.next_slide()

        # connect whatapp_server to a ISP called bob_isp
        img_bobISP = ImageMobject("images/server.png").scale_to_fit_width(1).to_edge(DOWN)
        self.play(FadeIn(img_bobISP))
        self.next_slide()

        # connect all of them
        line1 = Line(img_alice.get_right(), img_aliceTower.get_left()+0.1, color=C_GOLD_DIM)
        line2 = Line(img_aliceTower.get_bottom(), box.get_top(), color=C_GOLD_DIM)
        line3 = Line(img_bobISP.get_top(), box.get_bottom(), color=C_GOLD_DIM)
        line4 = Line(img_bob.get_left()-0.2, img_bobISP.get_right(), color=C_GOLD_DIM)

        # Create them normally
        self.play(Create(line1))
        self.play(Create(line2))
        self.next_slide()
        self.play(Create(line4))
        self.play(Create(line3))

        self.next_slide()

        # Then make them all thin
        self.play(
            line1.animate.set_stroke(width=1),
            line2.animate.set_stroke(width=1),
            line3.animate.set_stroke(width=1),
            line4.animate.set_stroke(width=1),
        )
        
        msg_List = ['Hello', ' Hi', 'Bye !']
        images_list = [img_alice, img_aliceTower, img_whatsApp, img_bobISP, img_bob]
        
        waypoints = [
            (img_alice.get_right(), img_aliceTower.get_left()),   # right of A to left of B
            (img_aliceTower.get_left(), img_whatsApp.get_left()-0.5),    # left of B to left of C
            (img_whatsApp.get_left(), img_bobISP.get_left()),    # left of C to left of D
            (img_bobISP.get_left(), img_bob.get_left()),    # left of D to left of E
        ]

        for msg in msg_List:
            label = Tex(msg, font_size=24)
            label.move_to(waypoints[0][0] + UP * 0.3)
            self.play(FadeIn(label))

            for start, end in waypoints:
                self.play(
                    label.animate.move_to(end + UP * 0.3),
                    run_time=2,
                    rate_func=smooth
                )

            self.remove(label)

        self.next_slide()

        img_eve = ImageMobject(
            "images/hacker_2.png").scale(0.4)
        img_eve.move_to([img_bob.get_top()[0], line2.get_y(), 0])
        txt_eve = Tex(r"Eve", font_size=FS_LABEL, color=C_RED).next_to(img_eve, DOWN, buff=0.1)
        self.play(FadeIn(img_eve), FadeIn(txt_eve))
        self.next_slide()

        # making line compromised
        line5 = Line(img_eve.get_left(), line2.get_center(), color=C_RED)
        self.play(Create(line5), run_time=1.5)
        
        mid = (img_aliceTower.get_bottom() + box.get_top())/2
        line6 = Line(mid, mid, color=C_RED)
        self.play(line6.animate.put_start_and_end_on(img_aliceTower.get_bottom(), box.get_top()), run_time=1)
        
        self.next_slide()

        waypoints2 = [
            (img_alice.get_right(), img_aliceTower.get_left()),
            (img_aliceTower.get_left(), line2.get_center()-0.5),
            (line2.get_center(), img_bobISP.get_left()),
            # (img_whatsApp.get_left(), img_bobISP.get_left()),
            (img_bobISP.get_left(), img_bob.get_left()),
        ]

        for msg in msg_List:
            label = Tex(msg, font_size=24)
            label.move_to(waypoints2[0][0] + UP * 0.3)
            self.play(FadeIn(label))

            i = 0
            for start, end, in waypoints2:
                if  i == 2:
                    msg2 = label.copy()
                    self.play(
                        label.animate.move_to(end + UP * 0.3), msg2.animate.move_to(img_eve.get_left()),
                        run_time=2,
                        rate_func=smooth
                    )
                    self.remove(msg2)
                else:
                    self.play(
                        label.animate.move_to(end + UP * 0.3),
                        run_time=2.5,
                        rate_func=smooth
                    )

                i += 1

            self.remove(label)
        self.next_slide()

        # change whatsapp to upi server and send pin from Alice to Bob
        img_upi = ImageMobject("images/upi2.png").scale_to_fit_width(1.2)
        # txt_upi = Tex(r"UPI Server", font_size=32).next_to(img_upi, DOWN, buff=0.1)
        self.play(FadeOut(img_whatsApp), FadeIn(img_upi))
        # self.play(FadeIn(txt_upi))

        # send pin 1234 from Alice to Bob
        pin = Tex(r"Pin : 1234", font_size=24)
        upi_msgList = ["Pin : 1234", "Pay Bob 20"]
        for msg in upi_msgList:
            label = Tex(msg, font_size=24)
            label.move_to(waypoints2[0][0] + UP * 0.3)
            self.play(FadeIn(label))

            i = 0
            for start, end, in waypoints2:
                if  i == 2:
                    msg2 = label.copy()
                    self.play(
                        label.animate.move_to(end + UP * 0.3), msg2.animate.move_to(img_eve.get_left()),
                        run_time=2,
                        rate_func=smooth
                    )
                    self.remove(msg2)
                else:
                    self.play(
                        label.animate.move_to(end + UP * 0.3),
                        run_time=2.5,
                        rate_func=smooth
                    )

                i += 1

            self.remove(label)
        self.next_slide()

        self.play(FadeOut(img_upi), FadeIn(img_whatsApp))
        txt_hello = Tex("HELLO", font_size=FS_BODY).next_to(img_alice, RIGHT, buff=0.2).shift(UP*0.3)
        self.play(FadeIn(txt_hello))
        self.next_slide()

        # Give and example of encryption using cesar cipher
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet_text = VGroup(*[Tex(l, font_size=FS_BODY+5) for l in letters])
        alphabet_text.arrange(RIGHT, buff=0.2)  # Control spacing with buff
        alphabet_text.shift(DOWN * 2)
        self.play(Create(alphabet_text))
        plotDotTL(self)
        self.next_slide()

        # A=0, B=1, C=2 ... Z=25
        pairs = [
            (7, 10),   # H -> K
            (4, 7),    # E -> H
            (11, 14),  # L -> O
            (11, 14),  # L -> O            
            (14, 17),  # O -> R
        ]

        copied_letters = []
        offset = 14
        result_group = VGroup()
        # result_group.next_to(img_alice, RIGHT, buff=0.2).shift(DOWN*0.3)
        for src, dst in pairs:
            h_rect = SurroundingRectangle(alphabet_text[src], buff=0.1, color=C_GOLD_BRIGHT, stroke_width=2)
            self.play(Create(h_rect))
            # self.play(FadeIn(label))

            r_rect = SurroundingRectangle(alphabet_text[dst], buff=0.1, color=C_RED, stroke_width=2)
            self.play(TransformFromCopy(h_rect, r_rect))
            self.next_slide()
            
            letter_copy = alphabet_text[dst].copy()
            self.play(letter_copy.animate.next_to(img_whatsApp, LEFT*offset), run_time=1.5)
            offset -= 1
            self.play(FadeOut(h_rect), FadeOut(r_rect))
            copied_letters.append(letter_copy)

        self.next_slide()
        txt_khoor = Tex("KHOOR", font_size=FS_BODY).next_to(img_alice, RIGHT, buff=0.2).shift(DOWN*0.3)
        self.play(TransformFromCopy(txt_hello, txt_khoor), *[FadeOut(l) for l in copied_letters], FadeOut(alphabet_text))

        self.next_slide()

        waypoints3 = [
            (img_alice.get_right(), img_aliceTower.get_left()),
            (img_aliceTower.get_left(), line2.get_center()-0.5),
            (line2.get_center(), img_bobISP.get_left()),
            (img_bobISP.get_left(), img_bob.get_left()+ LEFT * 0.8 )
        ]

        i = 0
        for start, end, in waypoints3:
            if  i == 2:
                msg2 = txt_khoor.copy()
                self.play(
                    txt_khoor.animate.move_to(end + UP * 0.3), msg2.animate.move_to(img_eve.get_left()),
                    run_time=2,
                    rate_func=smooth
                )
            else:
                self.play(
                    txt_khoor.animate.move_to(end + UP * 0.3),
                    run_time=2.5,
                    rate_func=smooth
                )

            i += 1

        txt_helloBob = Tex("HELLO", font_size=FS_BODY).next_to(img_bob, LEFT, buff=0.2).shift(DOWN*0.4)
        self.play(TransformFromCopy(txt_khoor, txt_helloBob))
        self.remove(msg2)

        self.next_slide()
        # upi ping encryption demo
        self.play(FadeOut(img_whatsApp), FadeIn(img_upi), FadeOut(txt_khoor), FadeOut(txt_helloBob), FadeOut(txt_hello))
        pin.next_to(img_alice, RIGHT, buff=0.2).shift(UP*0.3)
        self.play(FadeIn(pin))
        self.next_slide()

        enc_pin = Tex(r"Qpg : 9628", font_size=24).next_to(img_alice, RIGHT*0.8, buff=0.2).shift(DOWN*0.3)  
        self.play(TransformFromCopy(pin, enc_pin))
        
        i = 0
        for start, end, in waypoints3:
            if  i == 2:
                msg2 = enc_pin.copy()
                self.play(
                    enc_pin.animate.move_to(end + UP * 0.3), msg2.animate.move_to(img_eve.get_left()),
                    run_time=2,
                    rate_func=smooth
                )
                # self.remove(msg2)
            else:
                self.play(
                    enc_pin.animate.move_to(end + UP * 0.3),
                    run_time=2.5,
                    rate_func=smooth
                )

            i += 1
        
        txt_pinBob = Tex("Pin : 1234", font_size=FS_BODY).next_to(img_bob, LEFT, buff=0.2).shift(DOWN*0.4)
        self.play(TransformFromCopy(enc_pin, txt_pinBob))

# Aim : Defination of cryptography and old vs modern cryptography
class EncDec(Slide):
    def construct(self):
        self.camera.background_color = SLIDE_BG
        txt1 = Tex(r'HELLO').shift(UP*3)
        self.play(FadeIn(txt1))
        self.next_slide()

        rectangle = Rectangle(width=3, height=1, color=C_BLUE).next_to(
            txt1, DOWN, buff=1)
        self.play(Create(rectangle))

        hello_text = Tex("Scramble", font_size=FS_TINY+20, color=C_WHITE)
        hello_text.move_to(rectangle)

        self.play(Write(hello_text))
        self.next_slide()

        txt2 = Tex(r'KHOOR').next_to(rectangle, DOWN, buff=0.6)
        self.play(FadeIn(txt2, shift=DOWN*1.5), run_time=1)
        self.next_slide()

        rectangle2 = Rectangle(width=3, height=1, color=C_RED).next_to(
            txt2, DOWN, buff=1)
        self.play(Create(rectangle2))

        unscramble_text = Tex("Un-scramble", font_size=FS_TINY+18, color=C_WHITE)
        unscramble_text.move_to(rectangle2)
        self.play(Write(unscramble_text))
        self.next_slide()

        txt3 = Tex(r'HELLO').next_to(rectangle2, DOWN, buff=0.6)
        self.play(FadeIn(txt3, shift=DOWN*1.5), run_time=1)
        self.next_slide()

        transform1 = Transform(hello_text, Tex(
            r'Encryption').move_to(rectangle))
        self.play(transform1)
        self.next_slide()

        txtDec = Tex(
            r'Decryption'). move_to(rectangle2)
        transform2 = Transform(unscramble_text, txtDec)
        self.play(transform2)
        self.next_slide()

        # Define Cryptography -> Hidden writing
        grp1 = VGroup()
        grp1.add(rectangle, rectangle2, txt1, txt2, txt3,
                 hello_text, unscramble_text, txtDec)
        self.play(grp1.animate.shift(LEFT*4))
        self.next_slide()

        txt_defination1 = Tex(r'Hidden writting').next_to(
            txt2, RIGHT*14).align_to(DOWN)
        txt_defination1[0].set_color(C_BLUE)

        txt_defination = Tex(r'Crypto', r'graphy', font_size=56).next_to(txt_defination1, UP, buff=0.7)

        self.play(FadeIn(txt_defination1, shift=RIGHT), run_time=1)
        self.next_slide()

        self.play(FadeIn(txt_defination, shift=UP), run_time=1)
        self.next_slide()

        self.play(txt_defination[1].animate.shift(RIGHT * 0.2), txt_defination[0].animate.shift(LEFT * 0.2))
        self.next_slide()

        self.play(txt_defination[0].animate.set_color(C_RED), txt_defination[1].animate.set_color(C_GOLD_BRIGHT))

        self.next_slide()

        txt_why = Tex(r'Why ?').scale(
            0.7).next_to(txt_defination1, DOWN, buff=0.8)
        self.next_slide()
        self.play(FadeIn(txt_why))

        self.next_slide()

        txt_1_9 = Tex(r'Secure Communication \\ Over Insecure Channel').next_to(
            txt_why, DOWN, buff=0.5).scale(0.9)
        self.play(FadeIn(txt_1_9))
        self.next_slide()

        # continue here
        self.play(FadeOut(txt_defination), FadeOut(
            txt_defination1), FadeOut(txt_why), FadeOut(txt_1_9))
        self.play(FadeOut(txt2), FadeOut(txt1), FadeOut(txt3))
        # self.next_slide()

        self.play(FadeOut(rectangle), FadeOut(
            rectangle2), FadeOut(unscramble_text))
        grp = VGroup()
        grp.add(hello_text, txtDec)
        txt4 = Tex(r'Old Vs Modern Cryptography').shift(UP*3)
        transform3 = Transform(grp, txt4)
        self.play(transform3)
        self.next_slide()

        line = Line(start=2*UP, end=2.2*DOWN)
        line.set_stroke(width=2)  # Set th

        txt_3_1 = Text("Old Cryptography", color=C_RED, font_size=FS_BODY)
        txt_4_1 = Text("Modern Cryptography", color=C_BLUE, font_size=FS_BODY)

        txt_3_1.next_to(txt4, 2.3*DOWN)
        txt_3_1.shift(2.8*LEFT)

        txt_4_1.next_to(txt4, 2.3*DOWN)
        txt_4_1.shift(2.7*RIGHT)

        self.play(GrowFromCenter(line))
        self.play(Write(txt_3_1), Write(txt_4_1))

        self.next_slide()

        items_1 = [
            "Cesar/Shift Cipher",
            "Hill Cipher",
            "OTP / Scytale",
            "Vigenère / Playfair Cipher",
            "Bombe + Enigma ",
            "Colossus + Lorenz ciphers",
            "etc..."
        ]

        items_2 = [
            "AES / DSA / RSA / ECC",
            "Digital signatures / Hashing",
            "Homomorphic encryption",
            "ZKP / Paring based",
            "Cryptanalysis / Attacks ",
            "Post-Quantum cryptography",
            "etc..."
        ]

        bullet = "• "
        bullet_color = C_RED

        generic_algos = [
            Tex(f"{bullet}{item}", color=bullet_color, font_size=FS_LABEL) for item in items_1]
        genericAlgo_list = VGroup(*generic_algos)
        genericAlgo_list.arrange(DOWN, aligned_edge=LEFT*2)
        genericAlgo_list.next_to(txt_3_1, DOWN*1.5)

        bullet_color_special = C_BLUE
        special_algos = [
            Tex(f"{bullet}{item}", color=bullet_color_special, font_size=FS_LABEL) for item in items_2]
        specialAlgo_list = VGroup(*special_algos)
        specialAlgo_list.arrange(DOWN, aligned_edge=LEFT*2)
        specialAlgo_list.next_to(txt_4_1, DOWN*1.5)
        # specialAlgo_list.shift(LEFT) #### 0.7*hhhhh

        self.play(Write(genericAlgo_list), run_time=2)
        self.play(Write(specialAlgo_list), run_time=1)

        self.next_slide()
        self.play(FadeOut(genericAlgo_list), run_time=1)

        genComplexity = Tex(r'Obsolete', font_size=96, color=C_RED)
        genComplexity.next_to(txt_3_1, 6*DOWN)
        genComplexity.shift(LEFT*0.1)

        self.play(FadeIn(genComplexity), FadeOut(txt_3_1), run_time=1)
        self.next_slide()

# Aim : Cryptology = Cryptography + Cryptanalysis
class Cryptology(Slide, MovingCameraScene):
    """
    Vertical (top-down) cryptology tree with camera zoom choreography:
      1. Title card
      2. Root → two branches (Cryptography & Cryptanalysis)
      3. Zoom into Cryptography subtree
      4. Zoom back to root
      5. Zoom into Cryptanalysis subtree
      6. Zoom out — full tree overview + closing caption
      7. Functions for this class in cryptologySlide.py
    """
    def construct(self):
        self.camera.background_color = BG

        # ══════════════════════════════════════════════════════
        #  LAYOUT CONSTANTS  (vertical / top-down tree)
        # ══════════════════════════════════════════════════════
        ROOT_Y = 6.0          # top of canvas

        # Level 1: Cryptography & Cryptanalysis
        LVL1_Y = 3.5
        CRYPTO_X = -10.0
        ANAL_X   =  10.0

        # Level 2: Children of Crypto / Cryptanalysis
        LVL2_Y = 0.0

        # Level 3: Leaf nodes
        LVL3_Y = -4.0

        # Horizontal gaps
        CRYPTO_CHILD_GAP = 3.8
        ANAL_CHILD_GAP   = 4.0

        # ══════════════════════════════════════════════════════
        #  BUILD ALL NODES
        # ══════════════════════════════════════════════════════

        # ── ROOT ──────────────────────────────────────────────
        root = make_node(
            "Cryptology", 4.2, 1.1,
            ROOT_FILL, ROOT_STROKE, ROOT_TEXT,
            font_size=42, radius=0.22, stroke_w=2.5,
        )
        root.move_to([0, ROOT_Y, 0])

        # ── CRYPTOGRAPHY (level 1) ───────────────────────────
        crypto_root = make_node(
            "Cryptography", 3.8, 1.0,
            CRYPTO_FILL, CRYPTO_STROKE, CRYPTO_TEXT,
            font_size=32,
        )
        crypto_root.move_to([CRYPTO_X, LVL1_Y, 0])

        conn_root_crypto = elbow_down(root, crypto_root, CONN_ROOT, 1.8)

        # ── CRYPTANALYSIS (level 1) ──────────────────────────
        anal_root = make_node(
            "Cryptanalysis", 3.8, 1.0,
            ANAL_FILL, ANAL_STROKE, ANAL_TEXT,
            font_size=32,
        )
        anal_root.move_to([ANAL_X, LVL1_Y, 0])

        conn_root_anal = elbow_down(root, anal_root, CONN_ROOT, 1.8)

        # ── CRYPTOGRAPHY CHILDREN (level 2) ──────────────────
        c_labels = [
            (["Public Key", "(Asymmetric)"],  CRYPTO_C1),
            (["Private Key", "(Symmetric)"],  CRYPTO_C2),
            (["Digital", "Signatures"],       CRYPTO_C3),
            (["Hashing"],                     CRYPTO_C4),
            (["Advanced", "Topics"],          CRYPTO_C5),
        ]
        n_c = len(c_labels)
        c_start_x = CRYPTO_X - (n_c - 1) * CRYPTO_CHILD_GAP / 2

        crypto_children = VGroup()
        for i, (label, col) in enumerate(c_labels):
            n = make_node(label, 3.0, 0.85, col, CRYPTO_STROKE, CRYPTO_TEXT,
                          font_size=18)
            n.move_to([c_start_x + i * CRYPTO_CHILD_GAP, LVL2_Y, 0])
            crypto_children.add(n)

        crypto_child_conns = VGroup(
            *[elbow_down(crypto_root, ch, CONN_CRYPTO, 1.3) for ch in crypto_children]
        )

        # ── CRYPTOGRAPHY LEAVES (level 3) ────────────────────
        leaf_defs_c = [
            (0, ["Diffie-Hellman Key Exch.", "El-Gamal enc/dec",
                 "RSA", "EC Key Exchange", "EC enc./dec.", "ECIES"],
             3.6, 2.5),
            (1, ["AES"],
             2.6, 0.65),
            (2, ["El-Gamal", "RSA", "EC DSA"],
             2.8, 1.1),
            (3, ["SHA-2 / SHA-3"],
             2.8, 0.65),
            (4, ["ZKP", "Homomorphic Enc.", "MPC",
                 "Post-Quantum", r"Blockchain \& DLT"],
             3.6, 1.9),
        ]

        crypto_leaves     = VGroup()
        crypto_leaf_conns = VGroup()
        for (pidx, lines, lw, lh) in leaf_defs_c:
            parent = crypto_children[pidx]
            leaf = make_leaf_node(lines, lw, lh, LEAF_FILL, LEAF_STROKE, LEAF_TEXT,
                                 font_size=24)
            leaf.move_to([parent.get_center()[0], LVL3_Y, 0])
            crypto_leaves.add(leaf)
            crypto_leaf_conns.add(elbow_down(parent, leaf, CONN_CRYPTO, 1.2))

        # ── CRYPTANALYSIS CHILDREN (level 2) ──────────────────
        a_labels = [
            (["Classical", "Cryptanalysis"],       ANAL_C1),
            (["Symmetric Cipher", "Attacks"],      ANAL_C2),
            (["Asymmetric", "Cryptanalysis"],      ANAL_C3),
            (["Side-Channel &", "Implementation"], ANAL_C4),
        ]
        n_a = len(a_labels)
        a_start_x = ANAL_X - (n_a - 1) * ANAL_CHILD_GAP / 2

        anal_children = VGroup()
        for i, (label, col) in enumerate(a_labels):
            n = make_node(label, 3.0, 0.85, col, ANAL_STROKE, ANAL_TEXT,
                          font_size=18)
            n.move_to([a_start_x + i * ANAL_CHILD_GAP, LVL2_Y, 0])
            anal_children.add(n)

        anal_child_conns = VGroup(
            *[elbow_down(anal_root, ch, CONN_ANAL, 1.3) for ch in anal_children]
        )

        # ── CRYPTANALYSIS LEAVES (level 3) ────────────────────
        leaf_defs_a = [
            (0, ["Brute-force Search", "Frequency Analysis",
                 "Known-plaintext Attack", "Chosen-plaintext Attack",
                 "Chosen-ciphertext Attack", "Ciphertext-only Attack"],
             3.8, 2.5),
            (1, ["Linear Cryptanalysis",
                 "Differential Cryptanalysis",
                 "Integral Cryptanalysis"],
             3.6, 1.1),
            (2, ["Attack on DLP", "Attack on IFP", "Attack on ECDLP"],
             3.4, 1.1),
            (3, ["Timing Attacks", "Power Analysis",
                 "Cache Timing Attacks", "Fault Injection",
                 "Rowhammer Key Extraction"],
             3.8, 1.9),
        ]

        anal_leaves     = VGroup()
        anal_leaf_conns = VGroup()
        for (pidx, lines, lw, lh) in leaf_defs_a:
            parent = anal_children[pidx]
            leaf = make_leaf_node(lines, lw, lh, ANAL_LEAF_FILL, ANAL_LEAF_STROKE,
                                 ANAL_LEAF_TEXT, font_size=20)
            leaf.move_to([parent.get_center()[0], LVL3_Y, 0])
            anal_leaves.add(leaf)
            anal_leaf_conns.add(elbow_down(parent, leaf, CONN_ANAL, 1.2))

        # ══════════════════════════════════════════════════════
        #  Convenience groups
        # ══════════════════════════════════════════════════════
        crypto_subtree = VGroup(
            crypto_root, crypto_child_conns, crypto_children,
            crypto_leaf_conns, crypto_leaves,
        )
        anal_subtree = VGroup(
            anal_root, anal_child_conns, anal_children,
            anal_leaf_conns, anal_leaves,
        )
        everything = VGroup(
            root, conn_root_crypto, conn_root_anal,
            crypto_subtree, anal_subtree,
        )

        # ══════════════════════════════════════════════════════
        #  ACT 1 — ROOT NODE APPEARS
        # ══════════════════════════════════════════════════════
        self.camera.frame.move_to([0, ROOT_Y, 0]).set(width=12)

        self.play(FadeIn(root, scale=0.85), run_time=1.0)
        self.wait(0.8)
        self.next_slide()

        # ══════════════════════════════════════════════════════
        #  ACT 2 — TWO BRANCH STUBS
        # ══════════════════════════════════════════════════════
        # Widen camera to see both level-1 nodes
        self.play(
            self.camera.frame.animate
                .move_to([0, (ROOT_Y + LVL1_Y) / 2, 0])
                .set(width=28),
            run_time=1.0,
        )

        self.play(Create(conn_root_crypto), Create(conn_root_anal), run_time=1.0)
        self.play(
            FadeIn(crypto_root, shift=DOWN * 0.3),
            FadeIn(anal_root,   shift=DOWN * 0.3),
            run_time=0.8,
        )
        self.wait(0.5)
        self.next_slide()

        # ══════════════════════════════════════════════════════
        #  ACT 3 — ZOOM INTO CRYPTOGRAPHY BRANCH
        # ══════════════════════════════════════════════════════
        # Compute bounding box for crypto subtree area
        crypto_center_x = CRYPTO_X
        crypto_center_y = (LVL1_Y + LVL3_Y) / 2
        crypto_area_w   = n_c * CRYPTO_CHILD_GAP + 6.0
        crypto_area_h   = abs(LVL1_Y - LVL3_Y) + 5.0
        crypto_frame_w  = max(crypto_area_w, crypto_area_h * 16 / 9)

        self.play(
            self.camera.frame.animate
                .move_to([crypto_center_x, crypto_center_y, 0])
                .set(width=crypto_frame_w),
            run_time=1.6, rate_func=smooth,
        )

        # Section label
        sec_c = Text("Cryptography", font_size=34, color=CRYPTO_STROKE,
                      weight=BOLD)
        sec_c.move_to([crypto_center_x, LVL1_Y + 1.2, 0])
        self.play(FadeIn(sec_c, shift=DOWN * 0.2), run_time=0.6)
        self.wait(0.3)
        self.play(FadeOut(sec_c), run_time=0.4)

        # Reveal children
        self.play(Create(crypto_child_conns), run_time=0.8)
        for ch in crypto_children:
            self.play(FadeIn(ch, shift=DOWN * 0.2, scale=0.9), run_time=0.35)
        self.wait(0.3)
        self.next_slide()

        # Reveal leaves
        self.play(Create(crypto_leaf_conns), run_time=0.7)
        for leaf in crypto_leaves:
            self.play(FadeIn(leaf, shift=DOWN * 0.15), run_time=0.30)
        self.wait(0.6)
        self.next_slide()

        # ══════════════════════════════════════════════════════
        #  ACT 4 — ZOOM BACK TO ROOT
        # ══════════════════════════════════════════════════════
        self.play(
            self.camera.frame.animate
                .move_to([0, (ROOT_Y + LVL1_Y) / 2, 0])
                .set(width=28),
            run_time=1.6, rate_func=smooth,
        )
        self.wait(0.5)
        self.next_slide()

        # ══════════════════════════════════════════════════════
        #  ACT 5 — ZOOM INTO CRYPTANALYSIS BRANCH
        # ══════════════════════════════════════════════════════
        anal_center_x = ANAL_X
        anal_center_y = (LVL1_Y + LVL3_Y) / 2
        anal_area_w   = n_a * ANAL_CHILD_GAP + 6.0
        anal_area_h   = abs(LVL1_Y - LVL3_Y) + 5.0
        anal_frame_w  = max(anal_area_w, anal_area_h * 16 / 9)

        self.play(
            self.camera.frame.animate
                .move_to([anal_center_x, anal_center_y, 0])
                .set(width=anal_frame_w),
            run_time=1.6, rate_func=smooth,
        )

        sec_a = Text("Cryptanalysis", font_size=34, color=ANAL_STROKE,
                      weight=BOLD)
        sec_a.move_to([anal_center_x, LVL1_Y + 1.2, 0])
        self.play(FadeIn(sec_a, shift=DOWN * 0.2), run_time=0.6)
        self.wait(0.3)
        self.play(FadeOut(sec_a), run_time=0.4)

        # Reveal children
        self.play(Create(anal_child_conns), run_time=0.8)
        for ch in anal_children:
            self.play(FadeIn(ch, shift=DOWN * 0.2, scale=0.9), run_time=0.35)
        self.wait(0.3)
        self.next_slide()

        # Reveal leaves
        self.play(Create(anal_leaf_conns), run_time=0.7)
        for leaf in anal_leaves:
            self.play(FadeIn(leaf, shift=DOWN * 0.15), run_time=0.30)
        self.wait(0.6)
        self.next_slide()

        # ══════════════════════════════════════════════════════
        #  ACT 6 — FULL TREE OVERVIEW
        # ══════════════════════════════════════════════════════
        all_center = everything.get_center()
        all_w      = everything.width
        all_h      = everything.height
        aspect     = 16 / 9
        frame_w    = max(all_w + 3.0, (all_h + 2.5) * aspect)

        self.play(
            self.camera.frame.animate
                .move_to(all_center)
                .set(width=frame_w),
            run_time=2.2, rate_func=smooth,
        )
        self.wait(0.6)

        # Final caption
        caption = Tex(
            r"\textbf{Cryptology  =  Cryptography  +  Cryptanalysis}",
            font_size=96, color=ROOT_TEXT,
        )
        caption.move_to(all_center + DOWN * (all_h / 2 + 1.5))

        self.play(Write(caption), run_time=1.3)
        self.wait(2.0)
        self.next_slide()

        # ══════════════════════════════════════════════════════
        #  ACT 7 — HIGHLIGHT PUBLIC KEY & TRANSITION
        # ══════════════════════════════════════════════════════
        # Fade caption first
        self.play(FadeOut(caption), run_time=0.6)

        # Zoom camera to see the Public Key node area
        pk_node = crypto_children[0]  # "Public Key (Asymmetric)"

        # Highlight with yellow box
        highlight = SurroundingRectangle(pk_node, color=C_GOLD_BRIGHT,
                                         buff=0.15, stroke_width=3.0,
                                         corner_radius=0.18)
        self.play(Create(highlight), run_time=0.8)
        self.wait(0.5)
        self.next_slide()

        # Fade out everything except the Public Key node
        others = Group(
            *[m for m in self.mobjects if m is not pk_node and m is not highlight]
        )
        self.play(FadeOut(others), FadeOut(highlight), run_time=1.0)

        # Move PK node to center of screen and scale 2x
        self.play(
            pk_node.animate.move_to(ORIGIN).scale(2),
            self.camera.frame.animate.move_to(ORIGIN).set(width=14),
            run_time=1.2, rate_func=smooth,
        )
        self.wait(1.0)
        self.next_slide()

# Aim : One way function in PKC
class OneWayFunction(Slide, MovingCameraScene):
    """
    Starts with the Public Key (Asymmetric) box centered and scaled 2x.
    This continues from CryptologySlides where the PK box was already highlighted,
    isolated, and scaled.
    """

    def construct(self):
        self.camera.background_color = BG

        # ══════════════════════════════════════════════════════
        #  START WITH PUBLIC KEY NODE AT CENTER (scaled 2x)
        # ══════════════════════════════════════════════════════
        pk_node = make_node(
            ["Public Key", "(Asymmetric)"],
            3.0, 0.85,
            CRYPTO_C1, CRYPTO_STROKE, CRYPTO_TEXT,
            font_size=18
        )
        pk_node.scale(2).move_to(ORIGIN)

        # Camera matches end framing from CryptologySlides
        self.camera.frame.move_to(ORIGIN).set(width=14)

        # Keep node already present (no entrance animation)
        self.add(pk_node)
        self.wait(1.0)
        self.next_slide()

        # ══════════════════════════════════════════════════════
        #  THREE LEAF NODES: DLP, IFP, ECC
        # ══════════════════════════════════════════════════════
        PK_LEAF_Y = -3.2
        PK_LEAF_GAP = 4.2

        dlp = make_node("DLP", 2.2, 0.80, "#4C1D95", CRYPTO_STROKE, CRYPTO_TEXT, font_size=26)
        ifp = make_node("IFP", 2.2, 0.80, "#6D28D9", CRYPTO_STROKE, CRYPTO_TEXT, font_size=26)
        ecc = make_node("ECC", 2.2, 0.80, "#7C3AED", CRYPTO_STROKE, CRYPTO_TEXT, font_size=26)

        dlp.move_to([-PK_LEAF_GAP, PK_LEAF_Y, 0])
        ifp.move_to([0, PK_LEAF_Y, 0])
        ecc.move_to([PK_LEAF_GAP, PK_LEAF_Y, 0])

        leaves = VGroup(dlp, ifp, ecc)
        conns = VGroup(
            elbow_down(pk_node, dlp, CONN_CRYPTO, 2.0),
            elbow_down(pk_node, ifp, CONN_CRYPTO, 2.0),
            elbow_down(pk_node, ecc, CONN_CRYPTO, 2.0),
        )

        self.play(
            self.camera.frame.animate
                .move_to([0, -2.1, 0])
                .set(width=20),
            run_time=1.0,
        )
        self.play(Create(conns), run_time=0.8)
        self.play(FadeIn(leaves, shift=DOWN * 0.2), run_time=0.8)
        self.wait(1.0)
        self.next_slide()

        oneWayFun = Tex(r"One Way Functions", font_size=72, color=WHITE).next_to(leaves, DOWN*1.7, buff = 0.8)
        self.play(Write(oneWayFun), run_time=2)

        self.next_slide()

        self.play(FadeOut(leaves), FadeOut(conns), FadeOut(pk_node), Unwrite(oneWayFun), run_time=1.0)
        # reset camera position
        self.play(
            self.camera.frame.animate
                .move_to(ORIGIN)
                .set(width=14),  # Default manim width
            run_time=1.0,
        )

        oneWayFun2 = Tex(r"One Way Functions", font_size=52, color=WHITE).to_edge(UP)
        self.play(Write(oneWayFun2), run_time=0.5)

        ellipse1 = Ellipse(width=3, height=5, stroke_width=2, color=C_BLUE).scale(
            0.5).next_to(oneWayFun2, DOWN, buff=1).shift(LEFT*2)
        ellipse2 = Ellipse(width=3, height=5, stroke_width=2, color=C_RED).scale(
            0.5).next_to(ellipse1, RIGHT, buff=3)

        center_coords = ellipse1.get_center()
        dot = Dot(color=WHITE).move_to(center_coords)
        x = Tex(r'$x$').next_to(dot, LEFT)

        self.play(Create(ellipse1), Create(ellipse2), Create(dot), FadeIn(x))

        self.next_slide()

        dot2 = Dot(color=WHITE).move_to(ellipse2.get_center())
        fx = Tex(r'$f(x)$').next_to(dot2, DOWN).scale(0.7)
        curved_arrow = CurvedArrow(
            start_point=ellipse1.get_center(), end_point=ellipse2.get_center(), color=WHITE, stroke_width=2)
        self.play(Create(dot2), FadeIn(fx), Create(curved_arrow))

        easy = Tex(r'Easy', font_size=28).next_to(
            curved_arrow, DOWN)
        easy2 = Tex(r'Easy : Given $x$ easy to compute $f(x)$',
                    font_size=24).next_to(ellipse1, DOWN, buff=0.8).shift(RIGHT*1.5)
        self.play(FadeIn(easy), FadeIn(easy2))

        self.next_slide()
        # Create a curved arrow between the two points
        curved_arrow2 = CurvedArrow(
            start_point=ellipse2.get_center(), end_point=ellipse1.get_center(), color=C_GOLD_BRIGHT, stroke_width=2)
        curved_arrow2.tip_length = 4
        self.play(Create(curved_arrow2))
        hard = Tex(r'Hard', font_size=28, color=C_RED).next_to(curved_arrow2, UP)
        hard2 = Tex(r'Hard : Practically impossible to compute $f^{-1}(x)$',
                    font_size=24).next_to(easy2, DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(FadeIn(hard), FadeIn(hard2))

        self.next_slide()

        grp = VGroup()
        grp.add(ellipse1, ellipse2, dot, dot2, x, fx, curved_arrow,
                curved_arrow2, easy, hard, easy2, hard2)

        self.play(grp.animate.shift(LEFT*3.1))

        p = Tex(r'\textbf{$ p = 9343$}', font_size=30).next_to(
            oneWayFun2, DOWN, buff=1, aligned_edge=RIGHT)
        q = Tex(r'\textbf{ $q = 313$}', font_size=30).next_to(
            p, DOWN, aligned_edge=LEFT)
        n = Tex(r'\textbf{$ n = p \times q = 2924359$}', font_size=30).next_to(
            q, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(p), FadeIn(q))
        self.next_slide()

        self.play(FadeIn(n))
        n_easy = Tex(r'\textbf{Easy}', font_size=25,
                     color=C_GREEN).next_to(n, RIGHT)
        self.play(ScaleInPlace(n_easy, 1.4), run_time=3)
        self.wait(0.5)
        self.play(ShrinkToCenter(n_easy), run_time=2)
        self.next_slide()

        inv = Tex(r'\textbf{Given $n$, Find $p,q$ ?}', font_size=30).next_to(
            n, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(inv))
        inv_hard = Tex(r'\textbf{Hard}', font_size=25,
                       color=C_RED).next_to(inv, RIGHT)
        self.play(ScaleInPlace(inv_hard, 1.4), run_time=3)
        self.wait(0.5)
        self.play(ShrinkToCenter(inv_hard), run_time=2)
        self.next_slide()

        ifp = Tex(r'\textbf{Integer Factorization Problem}', font_size=32).next_to(
            inv, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(ifp))

        self.next_slide()
        self.play(FadeOut(grp), FadeOut(p), FadeOut(q), FadeOut(n),
                  FadeOut(inv), FadeOut(inv_hard))

        ifp2 = Tex(r'Integer Factorization problem',
                   font_size=38).next_to(oneWayFun2, DOWN, buff=0.2).to_edge(LEFT)

        # trf1 = 
        self.play(Transform(ifp, ifp2))

        txt_p = Tex(r'$p = $').next_to(ifp2, DOWN, buff=0.5).to_edge(LEFT)
        txt_q = Tex(r'$q = $').next_to(
            txt_p, DOWN, buff=0.2).align_to(txt_p, LEFT)

        txt_n1 = Tex(r'$n = $').next_to(
            txt_q, DOWN, buff=0.4).align_to(txt_q, LEFT)

        txt_p_val = Tex(r' 9343').next_to(txt_p, RIGHT).align_to(txt_p, DOWN)
        txt_q_val = Tex(r' 313').next_to(txt_q, RIGHT).align_to(txt_q, DOWN)
        txt_n1_val = Tex(r' 2924359').next_to(
            txt_n1, RIGHT).align_to(txt_n1, DOWN)

        self.play(FadeIn(txt_p), FadeIn(txt_p_val), run_time=1)
        self.play(FadeIn(txt_q), FadeIn(txt_q_val), run_time=0.5)
        self.play(FadeIn(txt_n1), FadeIn(txt_n1_val), run_time=0.5)

        self.next_slide()

        txt_bin = Tex(r'$\Longrightarrow$ 1011001001111101000111',
                      color=C_BLUE).next_to(txt_n1_val, RIGHT)
        txt_binBits = Tex(r'$\implies$ 22 bits').next_to(txt_bin)

        self.play(Write(txt_bin), run_time=1.3)
        self.play(Write(txt_binBits))

        self.next_slide()

        self.play(Unwrite(txt_p_val), Unwrite(txt_q_val), Unwrite(
            txt_n1_val), Unwrite(txt_bin), Unwrite(txt_binBits))

        # 300 digits prime
        txt_pBig = Tex(
            '''20395687835640197740576586692903457728019399331434826309477264645328306272\\
               27012776329366160631440881733123728826771238795387094001583065673383282791\\
               54499698366071906766440037074217117805690872792848149112022286332144876183\\
               376326512083574821647933992961249917319836219304274280243803104015000563790123
                ''').scale(0.6)

        txt_pBig.next_to(txt_p, RIGHT).align_to(txt_p, UP)

        self.play(txt_q.animate.shift(DOWN*1),
                  txt_n1.animate.shift(DOWN*0.8))
        self.play(Write(txt_pBig), run_time=2)

        self.next_slide()

        # 300 digits prime        
        txt_qBig = Tex(
            '''53187228905420418418508473437513339940830361398213085664529946493095217860\\
               60458488771291478203879964281755642282047858461412075324629363398341394124\\
               01975338705794646595487324365194792822189473092273993580587964571659678084\\
               484152603881094176995594813302284232006001752128168901293560051833646881436219
               ''').scale(0.6)
        txt_qBig.next_to(txt_q, RIGHT).align_to(txt_q, UP)
        self.play(txt_n1.animate.shift(DOWN))
        self.play(Write(txt_qBig), run_time=2)

        self.next_slide()

        # 600 digits
        txt_n1Big = Tex(
            '''1084790117597693937271763084574570511858682020282296481906670181023891548155144212725117888186309079413830042779189\\
            2172435969832681110079821228777715637385402516046241697020771301040268433037790024927292082119641899443468954219544400\\
            8546643909734553918562196237000260811736016995830450094506601223180883688118367193617732939585810720318219660211710733\\
            8082151740484847947310115784597211618760522571466879919783157250437448135206914678195218254097254219242827406407157677\\
            1892385103643850980406911054141524800072060690705610312275180837688240523596676859736979681916191592932997560462347010\\
            8492326664937
        ''').scale(0.4)
        txt_n1Big.next_to(txt_n1, RIGHT).align_to(txt_n1, UP)

        self.play(Write(txt_n1Big), run_time=3)

        self.next_slide()
        txt_3 = Tex(r'$n$ = ', '250 decimal or 829', ' bits  and used ', '2700 CPU', ' core-years').next_to(
        txt_n1Big, DOWN, buff=0.5).align_to(txt_n1Big, LEFT).scale(0.7)
        txt_3[1].set_color(C_BLUE)
        txt_3[3].set_color(C_GOLD_BRIGHT)

        txt_4 = Text(r'https:\\en.wikipedia.org\wiki\RSA_numbers').next_to(txt_3, DOWN, buff=0.1).scale(0.3)

        self.play(FadeIn(txt_3), FadeIn(txt_4))

        self.next_slide()
        self.play(FadeOut(oneWayFun2), FadeOut(ifp2), FadeOut(txt_3), FadeOut(txt_4), FadeOut(txt_n1Big), FadeOut(txt_qBig), FadeOut(txt_pBig), FadeOut(txt_p), FadeOut(txt_q), FadeOut(txt_n1))

        txt_1 = Tex(r'Https \\ Gmail, LinkedIn \\ etc...').shift(
            UP*1.7).scale(0.55)
        txt_2 = Tex(r'TLS').next_to(txt_1, DOWN, buff=0.8)
        txt_3 = Tex(r'RSA').next_to(txt_2, DOWN, buff=0.9)
        # txt_4 = Tex(r'Integer Factorization Problem', color=YELLOW).next_to(
        #     txt_3, DOWN, buff=0.8)

        self.play(ifp.animate.next_to(txt_3, DOWN, buff=0.8).set_color(C_GOLD_BRIGHT))
    
        self.next_slide()
        self.play(Write(txt_3))

        self.next_slide()
        self.play(Write(txt_2))

        self.next_slide()
        self.play(Write(txt_1))
        plotDotTL(self)

        self.next_slide()
        dot1 = Dot([0, 3.3, 1], color=WHITE)
        dot2 = Dot([-4.1, -2.9, 1], color=WHITE)
        dot3 = Dot([4.1, -2.9, 1], color=WHITE)

        l1 = Line(dot2, dot3, color=WHITE)
        l2 = Line(dot1, dot2, color=WHITE)
        l3 = Line(dot1, dot3, color=WHITE)

        self.play(Create(dot1), Create(dot2), Create(
            dot3), Create(l1), Create(l2), Create(l3))
        plotDotTL(self)

        dot4 = Dot([1.65, 0.9, 0])
        dot41 = Dot([-1.65, 0.9, 0])

        dot5 = Dot([-3.3, -1.6, 0])
        dot51 = Dot([3.3, -1.6, 0])

        l4 = Line(dot4, dot41, color=C_BLUE)
        l5 = Line(dot5, dot51, color=C_BLUE)
        self.play(FadeIn(l4), FadeIn(l5))

# Aim : Show ECDLP, Point addition, scalar multiplication
class ECDLP(Slide):
    def construct(self):
        self.camera.background_color = SLIDE_BG
        ecdlp = Tex('Elliptic Curve Discrete Logarithm Problem')
        self.play(Write(ecdlp))
        plotDotTL(self)
        self.next_slide()

        self.play(FadeOut(ecdlp))

        ec = Tex(r'Elliptic curves ')

        self.play(Write(ec))
        self.next_slide()  # Waits user to press continue to go to the next slide

        self.play(ec.animate.shift(UP*2))
        equation = Tex(r'$\mathcal{E} : y^2 = x^3 + ax + b$').scale(1.4)
        self.play(Write(equation))
        self.next_slide()

        self.play(Unwrite(ec))
        self.play(equation.animate.shift(UP*2))
        EC_coefficients = Tex(r'$a = -3, b = 3$').scale(1.4)
        self.play(Write(EC_coefficients))
        equation2 = Tex(r'$\mathcal{E} : y^2 = x^3 -3x + 3$').scale(1.4)
        self.next_slide()

        self.play(Unwrite(EC_coefficients))
        self.play(TransformMatchingTex(equation, equation2))
        self.next_slide()

        # self.play(equation2.animate.scale(0.5))
        self.play(equation2.animate.to_edge(UR).scale(0.7), run_time=1)
        plane = NumberPlane(x_range=[-12, 12, 1], x_length=12,
                            y_range=[-13, 13, 1], y_length=13,
                            background_line_style={
            "stroke_color": BLUE,
            "stroke_width": 2,
            "stroke_opacity": 0.3
        }
        ).add_coordinates().to_edge(LEFT)

        self.play(DrawBorderThenFill(plane))
        ellipticCurvePoints = getEC_points()

        graph = VMobject(color=C_RED)
        graph.set_points_smoothly(plane.coords_to_point(
            ellipticCurvePoints))

        self.play(Create(graph), run_time=2.5)
        self.next_slide()

        grp = VGroup()
        grp.add(plane, graph)
        myRect = SurroundingRectangle(grp, color=C_BLUE)
        grp.add(myRect)
        self.play(grp.animate.scale(0.6).to_edge(LEFT))
        # self.play(equation2.animate.shift(LEFT))
        self.next_slide()

        Text_pointAdd = Tex("Point addition", color=C_BLUE).next_to(equation2, DOWN, buff=0.5).shift(LEFT).scale(0.9)

        P = Dot(color=WHITE)
        P.move_to(graph.point_from_proportion(0.50))
        P_label = Tex("P", font_size=FS_SMALL).next_to(P, DL)

        Q = Dot(color=WHITE)
        Q.move_to(graph.point_from_proportion(0.45))
        Q_label = Tex("Q", font_size=FS_TINY+2).next_to(Q, LEFT)

        self.play(Create(P), Write(P_label), Create(Q), Write(Q_label))
        self.next_slide()

        self.play(Write(Text_pointAdd))
        self.next_slide()

        points_P_Q = Tex(
            r'$P = (x_p, y_p),    Q = (x_q, y_q$)', color=C_GREEN).next_to(Text_pointAdd, DOWN).scale(0.7)

        Text_R = Tex(r'$R = P + Q$').next_to(points_P_Q, DOWN).scale(0.7)

        point_AdditionFormula_Slope = Tex(
            r'$ \lambda = \frac{y_q - y_p}{x_q - x_p}  $').next_to(Text_R, DOWN).scale(0.9)

        # grp_rt = VGroup()
        # point_AdditionFormula = Tex(
        #     r'$ R = (\lambda^2 -x_p -x_q, \lambda(x_p - x_r)-y_p)$').next_to(point_AdditionFormula_Slope, DOWN).scale(0.7)

        # grp_rt.add(points_P_Q.shift(RIGHT*0.3), point_AdditionFormula_Slope,
        #            point_AdditionFormula.shift(RIGHT), Text_R)

        # self.play(FadeIn(grp_rt))

        # self.next_slide()

        l = Line(P, Q, color=C_GREEN, stroke_width=3)
        self.play(Create(l))
        self.next_slide()

        R = Dot(color=WHITE)
        R.move_to(graph.point_from_proportion(0.25))
        R_label = Text("R'", font_size=FS_TINY+2).next_to(R, LEFT)

        l2 = Line(Q, R, color=C_GREEN, stroke_width=3)
        self.play(Create(R), Create(R_label), Create(l2))
        self.next_slide()

        Q2 = Dot(color=WHITE)
        Q2.move_to(graph.point_from_proportion(0.75))

        l3 = Line(R, Q2, color=C_GREEN, stroke_width=3)

        self.play(Create(Q2), Create(l3))
        R2 = Text(f"({Q.get_center()[0]:.1f}, {Q.get_center()[1]:.1f})", font_size=FS_TINY+2).next_to(
            Q2, LEFT)
        R2 = Text("R = P+Q", font_size=FS_TINY+2).next_to(
            Q2, RIGHT)
        self.play(Create(R2))
        self.next_slide()

        # self.play(Unwrite(grp_rt))
        # self.play(Unwrite(Text_pointAdd))
        self.play(Unwrite(l3), Unwrite(R2), Unwrite(Q2),
                  Unwrite(R), Unwrite(l2), Unwrite(l), Unwrite(R_label))

        # @TODO :: merge P and Q to a single point using animation
        self.play(Unwrite(P), Unwrite(P_label),
                  Unwrite(Q), Unwrite(Q_label))

        Text_pointDouble = Tex("Point doubling", color=C_BLUE).next_to(Text_pointAdd, DOWN).scale(0.9)

        self.play(Write(Text_pointDouble))
        self.next_slide()

        P = Dot(color=WHITE)
        P.move_to(graph.point_from_proportion(0.47))
        P_label = Text("P", font_size=FS_TINY+2).next_to(P, UL)

        self.play(Create(P), Create(P_label))
        self.next_slide()

        tangentToCurve = TangentLine(graph, alpha=0.47, length=8, color=C_BLUE)

        self.play(Create(tangentToCurve))
        self.next_slide()

        Q = Dot(color=WHITE)
        Q.move_to(graph.point_from_proportion(0.29))
        Q_label = Text("Q", font_size=FS_TINY+2).next_to(Q, UL)

        self.play(Create(Q), Create(Q_label))
        self.next_slide()

        R = Dot(color=WHITE)
        R.move_to(graph.point_from_proportion(0.71))
        R_label = Tex(r"$2P = P+P$").next_to(R,
                                             RIGHT).scale(.6).shift(LEFT*0.7)
        l3 = Line(Q, R, color=C_BLUE, stroke_width=3)

        self.play(Create(l3))
        self.play(Create(R), Write(R_label))
        self.next_slide()

        points_2P = Tex(
            r'$2P = P+P$').next_to(Text_pointDouble, DOWN, aligned_edge=DOWN).scale(0.8).shift(LEFT*0.4)

        self.play(Write(points_2P))
        self.next_slide()

        self.play(Unwrite(Q), Unwrite(Q_label), Unwrite(
            tangentToCurve, reverse=True), Unwrite(l3))

        l4 = Line(R, P, color=C_BLUE, stroke_width=3)
        self.play(Create(l4))
        self.next_slide()

        d1 = Dot(color=WHITE)
        d1.move_to(graph.point_from_proportion(0.567))
        self.play(Create(d1))
        self.next_slide()

        d2 = Dot(color=WHITE)
        d2.move_to(graph.point_from_proportion(0.4316))
        l5 = Line(d1, d2, color=C_BLUE, stroke_width=3)
        self.play(Uncreate(l4))
        self.play(Create(d2), Create(l5))
        self.next_slide()

        self.play(Uncreate(l5), Uncreate(d1))

        P3_lable = Tex(r"$3P = P+P+P$").next_to(d2,
                                                RIGHT).scale(0.6).shift(LEFT*0.5)
        P3 = Tex(r"$3P = P+P+P$").next_to(points_2P,
                                          DOWN, aligned_edge=DL, buff=0.5).scale(0.78).shift(LEFT*0.2)

        self.play(Write(P3_lable), Write(P3))
        self.next_slide()

        dot_dotDot_1 = Text('.').next_to(P3, DOWN)
        dot_dotDot_2 = Text('.').next_to(dot_dotDot_1, DOWN)
        dot_dotDot_3 = Text('.').next_to(
            dot_dotDot_2, DOWN)
        mP = Tex(r'$mP = P+P+P+...+P = Q$').next_to(dot_dotDot_3,
                                                    DOWN, aligned_edge=LEFT).scale(0.8).shift(LEFT*2)

        self.play(Create(dot_dotDot_1), Create(dot_dotDot_2), Create(dot_dotDot_3))
        self.play(Write(mP))
        plotDotTL(self)
        self.next_slide()

        question = Tex(r'Given $m$ and $P$ \\ Compute $Q = mP$ $\in$ $\mathcal{E}$', color=C_GREEN).next_to(
            mP, DOWN, buff=0.8).scale(0.8)
        self.play(Write(question))
        plotDotTL(self)

        self.next_slide()
        self.play(FadeOut(dot_dotDot_1), FadeOut(dot_dotDot_2), FadeOut(
            dot_dotDot_3), FadeOut(P3_lable), FadeOut(P3), FadeOut(points_2P))

        self.play(mP.animate.next_to(
            Text_pointDouble, DOWN, aligned_edge=LEFT), run_time=0.4)
        self.play(question.animate.next_to(mP, DOWN), run_time=0.3)

        txt_da = Tex(r'DOUBLE and ADD \\ Algorithm', font_size=43, color=C_BLUE).next_to(
            question, DOWN, buff=0.6)

        self.play(FadeIn(txt_da))

# Aim : Double and add algorithm for scalar multiplication, complexity of ECDLP
class DoubleAndAdd(Slide):
    def construct(self):
        self.camera.background_color = SLIDE_BG

        mP = Tex(r'$mP = P+P+P+...+P$').scale(1.5)
        m = Tex(r'$mP$').scale(1.5)

        titleText = MarkupText(
            f'<span fgcolor="{C_BLUE}">DOUBLE</span> and <span fgcolor="{C_RED}">ADD</span> algorithm', color=WHITE)
        self.play(FadeIn(titleText))
        self.next_slide()

        self.play(titleText.animate.to_edge(UL).shift(LEFT*1.3).scale(0.7))
        mP.next_to(titleText, DOWN).scale(0.6)
        self.play(Write(mP))
        m.next_to(titleText, DOWN).scale(0.6).shift(LEFT*2.28)
        self.play(FadeIn(m))
        self.next_slide()

        # self.start_loop()  # Start loop
        my_rect = Rectangle(height=m.get_height()+0.3,
                            width=(m.get_width()+0.3), color=C_GOLD_BRIGHT)
        my_rect.surround(m)
        self.play(Create(my_rect), run_time=1.5)
        self.wait(0.3)
        self.play(FadeOut(my_rect))
        # self.end_loop()  # This will loop until user inputs a key

        m_bin = Tex(
            r'$ m$', color=C_GREEN).next_to(mP, DOWN, buff=0.6).scale(1).shift(LEFT*3.2)

        transformTo_m = Transform(m, m_bin)
        self.play(transformTo_m, run_time=1.3)
        m_bin2 = Tex(
            r'$= m_0 + 2m_1 + 2^2m_2 + ... +2^sm_s$', color=C_GREEN).next_to(m_bin, RIGHT).scale(0.8).shift(LEFT*0.8)
        self.play(FadeIn(m_bin2, shift=RIGHT), run_time=1.3)
        self.next_slide()

        example1 = Tex(r'e.g: $m = (9)_{10} = $').next_to(
            m_bin, DOWN, buff=0.4).shift(RIGHT*1.5)
        example2 = Tex(r'$(1001)_2$').next_to(example1, RIGHT)

        self.play(FadeIn(example1), FadeIn(example2))
        example2Copy = example2.copy()
        self.play(FadeIn(example2Copy))
        self.next_slide()

        first_One = Tex(r'$1$').next_to(example1, DOWN).shift(LEFT*1.5)
        first_Zero = Tex(r'$0$').next_to(first_One, DOWN)
        seond_Zero = Tex(r'$0$').next_to(first_Zero, DOWN)
        second_One = Tex(r'$1$').next_to(seond_Zero, DOWN)

        grp = VGroup()
        grp.add(first_Zero, first_One, seond_Zero, second_One)

        trans = Transform(example2, grp)
        self.play(trans)
        self.next_slide()

        txt_firstOne = Tex(
            r'$\blacktriangleright$ DOUBLE and ADD', color=C_BLUE).next_to(first_One, RIGHT).scale(0.7).shift(LEFT*0.8)
        txt_secondOne = Tex(
            r'$\blacktriangleright$ DOUBLE and ADD', color=C_BLUE).next_to(second_One, RIGHT).scale(0.7).shift(LEFT*0.8)

        txt_firstZero = Tex(
            r'$\blacktriangleright$ DOUBLE', color=C_RED).next_to(first_Zero, RIGHT).scale(0.7).shift(LEFT*0.32)
        txt_secondZero = Tex(
            r'$\blacktriangleright$ DOUBLE', color=C_RED).next_to(seond_Zero, RIGHT).scale(0.7).shift(LEFT*0.35)

        self.play(FadeIn(txt_firstOne, shift=RIGHT), run_time=1)
        self.wait(1)
        self.play(FadeIn(txt_firstZero, shift=RIGHT), run_time=1)
        self.play(FadeIn(txt_secondZero, shift=RIGHT), run_time=1)
        self.play(FadeIn(txt_secondOne, shift=RIGHT), run_time=1)

        self.next_slide()

        complexity = Tex(r"Complexity",
                         font_size=40, color=C_BLUE).shift(RIGHT*3).shift(UP)
        complexity2 = Tex(r"$O(log_2(m))$", font_size=66).next_to(
            complexity, DOWN, buff=0.3)

        self.play(FadeIn(complexity), FadeIn(complexity2))

        grp2 = VGroup()
        grp2.add(complexity2, complexity)
        myRect = SurroundingRectangle(grp2, color=C_GOLD_BRIGHT)
        grp2.add(myRect)

        self.play(Create(myRect), run_time=2)
        self.wait(0.3)
        self.play(FadeOut(myRect))

        # nextScenePause(self)

# Aim : Show ECDLP, inverse problem is hard
class ECDLP2(Slide):
    def construct(self):
        self.camera.background_color = SLIDE_BG

        txt_1 = Tex(r'$mP = Q$')
        txt_2 = Tex(r'EASY !!!', color=C_GREEN).next_to(
            txt_1, RIGHT).shift(RIGHT*0.5)
        self.play(Write(txt_1), run_time=2)
        self.play(ScaleInPlace(txt_2, 1.4), run_time=3)
        self.wait(0.5)
        self.play(ShrinkToCenter(txt_2), run_time=2)

        self.next_slide()

        self.play(txt_1.animate.shift(UP*3))
        self.next_slide()

        txt_3 = Tex(r'The inverse problem...').shift(UP*1.5)
        self.play(Write(txt_3), run_time=2)
        self.next_slide()

        txt_4 = Tex(r'Given $P$ and $Q \in \mathcal{E}$, Find $m$.').next_to(
            txt_3, DOWN, buff=0.5)
        self.play(FadeIn(txt_4), run_time=2)
        self.next_slide()

        txt_51 = Tex(r'Elliptic Curve Discrete Logarithm Problem',
                     color=C_BLUE).next_to(txt_4, DOWN, buff=1)
        txt_5 = Tex(r'$Elliptic\: Curve\: Discrete\: Logarithm\: Problem$').next_to(
            txt_4, DOWN*1.2, buff=1).scale(1.2)
        self.play(FadeIn(txt_51))
        self.wait(1)
        self.play(Unwrite(txt_3),  run_time=1)

        self.play(txt_4.animate.shift(UP),
                  txt_51.animate.shift(UP), run_time=3)

        # nextScenePause(self)

# Aim : Triangle stack w.r.t. ECDLP
class ECDLP3(Slide):
    def construct(self):
        self.camera.background_color = SLIDE_BG
        txt_21 = Tex(r'Elliptic curve cryptography').shift(UL*3.5)
        self.play(FadeIn(txt_21), run_time=0.1)

        img_whatsApp = SVGMobject("images/WhatsApp.svg").scale(0.7).shift(UP)
        txt_app1 = Tex(r'WhatsAPP \\ End to End \\ encryption',
                       color=C_GREEN).next_to(img_whatsApp, DOWN)

        self.play(FadeIn(img_whatsApp), FadeIn(txt_app1))
        # self.next_slide()

        self.play(txt_app1.animate.shift(LEFT*5),
                  img_whatsApp.animate.shift(LEFT*5))

        img_UPI = ImageMobject(
            "images/upi2.png").scale(0.7).shift(UP)
        txt_app2 = Tex(r'UPI \\ Google Pay \\ PhonePe',
                       color=C_BLUE).next_to(txt_app1, RIGHT, buff=1).next_to(img_UPI, DOWN)
        self.play(FadeIn(txt_app2), FadeIn(img_UPI))

        # self.next_slide()
        self.play(txt_app2.animate.shift(LEFT*1.7),
                  img_UPI.animate.shift(LEFT*1.7))

        img_bitEth = ImageMobject(
            "images/bitEth.png").scale(0.2).next_to(img_UPI, RIGHT, buff=0.8)
        txt_app3 = Tex(r'Crypto \\ Curriencies',
                       color=C_GOLD_BRIGHT).next_to(img_bitEth, DOWN)
        self.play(FadeIn(txt_app3), FadeIn(img_bitEth))

        # self.next_slide()

        txt_TLS = Tex(r"SSL/TLS").scale(1.3).next_to(img_bitEth,
                                                     RIGHT, buff=1)
        txt_Https = Tex(r'HTTPS \\ Email \\ etc...',
                        color=C_BLUE).next_to(txt_TLS, DOWN)
        self.play(FadeIn(txt_Https), FadeIn(txt_TLS))
        # self.next_slide()

        grp = Group()
        grp.add(img_whatsApp, txt_app1, img_UPI, txt_app2,
                img_bitEth, txt_app3, txt_TLS, txt_Https)
        self.play(grp.animate.shift(UP).scale(0.8))

        txt_ecdlp = Tex(
            r'Elliptic Curve Discrete Logarithm Problem').next_to(grp, DOWN, buff=1).scale(1.2)
        self.play(FadeIn(txt_ecdlp))

        self.next_slide()
        self.play(FadeOut(img_whatsApp), FadeOut(txt_app1), FadeOut(img_UPI), FadeOut(txt_app2), FadeOut(img_bitEth), 
                    FadeOut(txt_app3), FadeOut(txt_TLS), FadeOut(txt_Https))
        
        self.play(txt_ecdlp.animate.to_edge(DOWN))
        self.next_slide()
        self.play(txt_21.animate.next_to(txt_ecdlp, UP, buff=0.5))
        self.next_slide()

        left_base = np.array([-4.0, -3.1, 0])
        right_base = np.array([4.0, -3.1, 0])
        apex_point = np.array([0, 3.3, 0])
        tri_outline = Polygon(left_base, right_base, apex_point, color=C_GOLD, stroke_width=4)

        base_y = left_base[1]
        apex_y = apex_point[1]
        half_base = right_base[0]

        def half_width_at(y):
            return half_base * (apex_y - y) / (apex_y - base_y)

        y_top_div = 1.0
        y_mid_div = -1.3
        top_half = half_width_at(y_top_div)
        mid_half = half_width_at(y_mid_div)

        top_divider = Line(
            np.array([-top_half, y_top_div, 0]),
            np.array([top_half, y_top_div, 0]),
            color=C_GOLD_DIM,
            stroke_width=3,
        )
        mid_divider = Line(
            np.array([-mid_half, y_mid_div, 0]),
            np.array([mid_half, y_mid_div, 0]),
            color=C_GOLD_DIM,
            stroke_width=3,
        )

        wa_apex = SVGMobject("images/WhatsApp.svg").scale(0.55)
        upi_apex = ImageMobject("images/upi2.png").scale(0.18)
        biteth_apex = ImageMobject("images/bitEth.png").scale(0.085)

        # Center icons within the top tier (between y_top_div and apex)
        top_tier_mid = (y_top_div + apex_y) / 2  # midpoint of top tier
        apps_top_row = Group(wa_apex).move_to(np.array([0, top_tier_mid + 0.3, 0]))
        apps_bottom_row = Group(upi_apex, biteth_apex).arrange(RIGHT, buff=0.25).move_to(np.array([0, top_tier_mid - 0.4, 0]))
        apps_icons = Group(apps_top_row, apps_bottom_row)

        # Center text in middle and bottom tiers
        mid_tier_mid = (y_mid_div + y_top_div) / 2  # midpoint of middle tier
        bot_tier_mid = (base_y + y_mid_div) / 2  # midpoint of bottom tier
        txt_ecdlp_target = Tex(r'Elliptic curve discrete \\ logarithm problem').scale(0.86).move_to(np.array([0, bot_tier_mid, 0]))
        txt_21_target = Tex(r'Elliptic curve \\ cryptography').scale(1.0).move_to(np.array([0, mid_tier_mid, 0]))

        self.play(
            Transform(txt_ecdlp, txt_ecdlp_target),
            Transform(txt_21, txt_21_target),
        )
        self.next_slide()
        self.play(Create(tri_outline))
        self.play(Create(top_divider), Create(mid_divider))
        self.play(FadeIn(apps_icons))

# Aim : The big picture - pyrimid with everything
class CryptoPyramid(Slide, MovingCameraScene):

    def construct(self):
        self.camera.background_color = BG
        self.camera.frame.save_state()

        # ── outer triangle shell ──
        shell = Polygon(
            APEX, BL, BR,
            color=GOLD, stroke_width=3.0,
            fill_color=BG, fill_opacity=1,
        )
        self.play(Create(shell), run_time=1.2)
        self.next_slide()

        self._tier_math()
        self.next_slide()

        self._tier_hardness()
        self.next_slide()

        self._tier_algorithms()
        self.next_slide()

        self._tier_protocols()
        self.next_slide()

        self._tier_applications()
        self.next_slide()

        # ── Final zoom out ──
        self.play(Restore(self.camera.frame), run_time=1.4)
        self.next_slide()

    # ═══════════════════════════════════════════════════════
    #  TIER 1 — MATHEMATICS   (Y0 → Y1)
    #  Width at content ≈ 9.8 — lots of room
    # ═══════════════════════════════════════════════════════
    def _tier_math(self):
        banner_y  = Y0 + 0.30
        content_y = (Y0 + Y1) / 2 + 0.18  # −2.92

        # Subtle warm tint for entire math zone (Y0→Y2)
        math_bg = trapezoid(Y0, Y2, GOLD, opacity=0.05)

        div = tier_div(Y1, sw=1.5, col=GOLD_DIM)  # dashed feel — sub-layer

        lbl = t_gold("M A T H E M A T I C S", fs=38, w=BOLD) \
                .move_to([0, banner_y, 0])

        col_x = hw(content_y) * 2 * 0.28

        sep_l = dash_vline(-col_x / 1.6, Y0 + 0.50, Y1 - 0.06)
        sep_r = dash_vline( col_x / 1.6, Y0 + 0.50, Y1 - 0.06)

        alg = vstack(
            t_white("Abstract Algebra", 22),
            t_small("Groups · Rings · Fields", 13), buf=0.09,
        ).move_to([-col_x-0.3, content_y, 0])

        num = vstack(
            t_white("Number Theory", 22),
            t_small("Primes · Modular Arith., Factor.", 13), buf=0.09,
        ).move_to([0, content_y, 0])

        ell = vstack(
            t_white("Elliptic Curves", 22),
            t_small("Finite Fields", 13), buf=0.09,
        ).move_to([col_x+0.3, content_y, 0])

        self.play(FadeIn(math_bg), run_time=0.4)
        self.play(Create(div), run_time=0.6)
        self.play(Write(lbl), run_time=0.8)
        self.play(Create(sep_l), Create(sep_r), run_time=0.4)
        self.play(
            LaggedStart(FadeIn(alg), FadeIn(num), FadeIn(ell), lag_ratio=0.25),
            run_time=0.9,
        )

    # ═══════════════════════════════════════════════════════
    #  TIER 2 — HARDNESS (sub-layer of Mathematics) (Y1 → Y2)
    #  Compact — abbreviations. Visual cue: same tint, dashed divider.
    #  Width at content ≈ 8.3
    # ═══════════════════════════════════════════════════════
    def _tier_hardness(self):
        tier_mid = (Y1 + Y2) / 2           # −1.90
        self.play(
            self.camera.frame.animate
                .set_width(9.0)
                .move_to([0, tier_mid, 0]),
            run_time=0.9,
        )

        # Solid gold divider at Y2 — this is the real boundary
        div = tier_div(Y2, sw=2.5)

        # Bracket label connecting to math
        bracket_l = Line(lp(Y1) + RIGHT*0.15, lp(Y1) + RIGHT*0.15 + UP*0.20,
                         color=GOLD_DIM, stroke_width=1.5)
        bracket_r = Line(rp(Y1) + LEFT*0.15, rp(Y1) + LEFT*0.15 + UP*0.20,
                         color=GOLD_DIM, stroke_width=1.5)

        title = t_small("Hardness Assumptions",
                         fs=12, col=GOLD_DIM) \
                    .move_to([0, Y1 + 0.14, 0])

        content_y = tier_mid
        avail = hw(content_y) * 2          # ≈ 8.3
        col_x = avail * 0.25

        sep_l = dash_vline(-col_x * 0.65, Y1 + 0.26, Y2 - 0.06)
        sep_r = dash_vline( col_x * 0.65, Y1 + 0.26, Y2 - 0.06)

        # Compact: abbreviations + emoji lock icons
        ifp = vstack(
            t_gold("IFP", fs=26, col=GOLD, w=BOLD),
            t_small("RSA", fs=12), buf=0.08,
        ).move_to([-col_x, content_y, 0])

        lock1 = Text(LOCK_EMOJI, font_size=18).next_to(ifp, LEFT, buff=0.12)

        ecdlp = vstack(
            t_gold("ECDLP", fs=26, col=GOLD, w=BOLD),
            t_small("ECC", fs=12), buf=0.08,
        ).move_to([0, content_y, 0])

        lock2 = Text(LOCK_EMOJI, font_size=18).next_to(ecdlp, LEFT, buff=0.12)

        dlp = vstack(
            t_gold("DLP", fs=26, col=GOLD, w=BOLD),
            t_small("Diffie Hellman", fs=12), buf=0.08,
        ).move_to([col_x, content_y, 0])

        lock3 = Text(LOCK_EMOJI, font_size=18).next_to(dlp, LEFT, buff=0.12)

        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(title), FadeIn(bracket_l), FadeIn(bracket_r), run_time=0.5)
        self.play(Create(sep_l), Create(sep_r), run_time=0.4)
        self.play(
            LaggedStart(
                AnimationGroup(FadeIn(ifp), FadeIn(lock1)),
                AnimationGroup(FadeIn(ecdlp), FadeIn(lock2)),
                AnimationGroup(FadeIn(dlp), FadeIn(lock3)),
                lag_ratio=0.3,
            ),
            run_time=1.2,
        )

    # ═══════════════════════════════════════════════════════
    #  TIER 3 — ALGORITHMS   (Y2 → Y5)
    #  Banner at Y3→Y4.  Content below (Y2→Y3) and above (Y4→Y5).
    #  Width at Y2 ≈ 7.6, at Y5 ≈ 4.9
    # ═══════════════════════════════════════════════════════
    def _tier_algorithms(self):
        tier_mid = (Y2 + Y5) / 2           # −0.45
        self.play(
            self.camera.frame.animate
                .set_width(8.5)
                .move_to([0, tier_mid, 0]),
            run_time=0.9,
        )

        # ── ALGORITHMS banner (Y3→Y4) — clipped to pyramid ──
        ban_mid = (Y3 + Y4) / 2           # −0.50
        # Use a polygon that exactly follows the pyramid edges
        ban_bg = trapezoid(Y3, Y4, GOLD_DIM, opacity=0.15)
        b_top = tier_div(Y4, sw=2.0)
        b_bot = tier_div(Y3, sw=2.0)
        lbl   = t_gold("A L G O R I T H M S", fs=28, w=BOLD) \
                    .move_to([0, ban_mid, 0])

        # Top divider at Y5
        div_top = tier_div(Y5, sw=2.5)

        # ── Content BELOW banner (Y2 → Y3): 3 sub-rows ──
        below_h = Y3 - Y2                 # 0.60
        rh      = below_h / 3.0           # 0.20 each
        ry      = [Y2 + rh * (i + 0.5) for i in range(3)]

        c_div_below = dash_vline(0, Y2 + 0.03, Y3 - 0.03)
        sub1 = dim_line(lp(Y2 + rh),     rp(Y2 + rh), sw=0.7)
        sub2 = dim_line(lp(Y2 + rh * 2), rp(Y2 + rh * 2), sw=0.7)

        # Row 0 (bottom): wider area — use more width
        rx0 = hw(ry[0]) * 0.45
        key_l = t_white("Public Key", fs=11).move_to([-rx0, ry[0], 0])
        key_r = t_white("Private Key", fs=11).move_to([rx0, ry[0], 0])

        # Row 1 (middle)
        rx1 = hw(ry[1]) * 0.45
        sig   = t_white("Digital Sig.", fs=11).move_to([-rx1, ry[1], 0])
        crypt = t_white("Cryptanalysis", fs=11).move_to([rx1, ry[1], 0])

        # Row 2 (top)
        rx2 = hw(ry[2]) * 0.42
        zkp = t_white("ZKP", fs=11).move_to([-rx2, ry[2], 0])
        pqc = t_white("PQC", fs=11).move_to([rx2, ry[2], 0])

        # ── Content ABOVE banner (Y4 → Y5): 2-column ──
        above_mid = (Y4 + Y5) / 2         # 0.15
        c_div_above = dash_vline(0, Y4 + 0.04, Y5 - 0.04)

        rxa = hw(above_mid) * 0.40
        enc = vstack(
            t_white("Encryption", fs=16),
            t_small("AES · RSA · ECC", fs=12), buf=0.06,
        ).move_to([-rxa, above_mid, 0])

        key_icon = Text(KEY_EMOJI, font_size=14).next_to(enc, LEFT, buff=0.08)

        hash_fn = vstack(
            t_white("Hashing", fs=16),
            t_small("SHA · Blake · MD5", fs=12), buf=0.06,
        ).move_to([rxa, above_mid, 0])

        shield = Text(SHIELD_EMJ, font_size=14).next_to(hash_fn, LEFT, buff=0.08)

        # ── Animate ──
        self.play(FadeIn(ban_bg), Create(b_bot), Create(b_top), run_time=0.5)
        self.play(Write(lbl), Create(div_top), run_time=0.7)

        # Below banner
        self.play(Create(c_div_below), run_time=0.3)
        self.play(Create(sub1), FadeIn(key_l), FadeIn(key_r), run_time=0.5)
        self.play(Create(sub2), FadeIn(sig), FadeIn(crypt), run_time=0.5)
        self.play(FadeIn(zkp), FadeIn(pqc), run_time=0.5)

        # Above banner
        self.play(Create(c_div_above), run_time=0.3)
        self.play(
            FadeIn(enc), FadeIn(key_icon),
            FadeIn(hash_fn), FadeIn(shield),
            run_time=0.7,
        )

    # ═══════════════════════════════════════════════════════
    #  TIER 4 — PROTOCOLS   (Y5 → Y6)
    #  Width at content ≈ 4.2 — three tight columns
    # ═══════════════════════════════════════════════════════
    def _tier_protocols(self):
        tier_mid = (Y5 + Y6) / 2           # 1.05
        self.play(
            self.camera.frame.animate
                .set_width(5.5)
                .move_to([0, tier_mid, 0]),
            run_time=0.9,
        )

        div = tier_div(Y6, sw=2.0)

        title = t_small("P R O T O C O L S", fs=13, col=GOLD_DIM) \
                    .move_to([0, Y5 + 0.10, 0])

        content_y = tier_mid + 0.05
        avail = hw(content_y) * 2          # ≈ 4.16
        col_x = avail * 0.28

        sep_l = dash_vline(-col_x * 0.55, Y5 + 0.22, Y6 - 0.06)
        sep_r = dash_vline( col_x * 0.55, Y5 + 0.22, Y6 - 0.06)

        tls = vstack(
            t_white("TLS 1.3", fs=16),
            t_small("HTTPS", fs=12), buf=0.07,
        ).move_to([-col_x, content_y, 0])

        signal = vstack(
            t_white("Signal", fs=16),
            t_small("E2E", fs=11), buf=0.07,
        ).move_to([0, content_y, 0])

        ssh = vstack(
            t_white("SSH", fs=16),
            t_small("PGP", fs=11), buf=0.07,
        ).move_to([col_x, content_y, 0])

        self.play(Create(div), run_time=0.5)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(sep_l), Create(sep_r), run_time=0.4)
        self.play(
            LaggedStart(FadeIn(tls), FadeIn(signal), FadeIn(ssh), lag_ratio=0.25),
            run_time=0.9,
        )

    # ═══════════════════════════════════════════════════════
    #  TIER 5 — APPLICATIONS   (Y6 → Y7 apex)
    #  Narrow — heavy zoom. Stacked vertically, 3 rows.
    #  Width: 2.9 at bottom, 1.7 at mid, 0.7 near apex
    # ═══════════════════════════════════════════════════════
    def _tier_applications(self):
        apex_mid = (Y6 + Y7) / 2           # 2.80
        self.play(
            self.camera.frame.animate
                .set_width(3.5)
                .move_to([0, apex_mid, 0]),
            run_time=0.9,
        )

        apps_lbl = t_small("A P P L I C A T I O N S", fs=10, col=GOLD_DIM) \
                       .move_to([0, Y6 + 0.10, 0])

        # ── Bottom row (y ≈ 2.0, width ≈ 2.8) ──
        row_bot_y = Y6 + 0.38
        w_bot     = hw(row_bot_y) * 2      # ≈ 2.82

        https_t = t_white("HTTPS", fs=13).move_to([-w_bot * 0.28, row_bot_y, 0])
        upi_t   = t_gold("UPI", fs=13, col=GOLD_BRIGHT) \
                      .move_to([0, row_bot_y, 0])
        more_t  = t_small("& more...", fs=10) \
                      .move_to([w_bot * 0.28, row_bot_y, 0])

        d_bot = dim_line(lp(row_bot_y + 0.22), rp(row_bot_y + 0.22), sw=0.8)

        # ── Middle row (y ≈ 2.55, width ≈ 2.0) ──
        row_mid_y = 2.55
        w_mid     = hw(row_mid_y) * 2      # ≈ 2.04

        wa_t = t_gold("WhatsApp", fs=12, col=GOLD_BRIGHT) \
                   .move_to([-w_mid * 0.25, row_mid_y, 0])
        eth_gem = self._eth_gem().scale(0.16) \
                      .move_to([w_mid * 0.25, row_mid_y + 0.04, 0])
        eth_lbl = t_small("ETH", fs=9) \
                      .next_to(eth_gem, DOWN, buff=0.03)

        d_mid = dim_line(lp(row_mid_y + 0.28), rp(row_mid_y + 0.28), sw=0.8)

        # ── Top: Bitcoin near apex (y ≈ 3.30, width ≈ 1.0) ──
        btc_y  = 3.25
        circle = Circle(
            radius=0.14, stroke_width=1.5,
            color=BITCOIN_ORG, fill_color=BITCOIN_ORG, fill_opacity=1,
        ).move_to([0, btc_y + 0.16, 0])
        sym = Text("₿", font="GFS Complutum", font_size=11, color=WHITE) \
                .move_to(circle.get_center())
        btc_lbl = t_white("Crypto. Curr.", fs=10) \
                      .next_to(circle, DOWN, buff=0.04)

        # ── Animate bottom → top for fun reveal ──
        self.play(FadeIn(apps_lbl), run_time=0.3)
        self.play(
            LaggedStart(FadeIn(https_t), FadeIn(upi_t), FadeIn(more_t), lag_ratio=0.15),
            run_time=0.6,
        )
        self.play(Create(d_bot), run_time=0.25)
        self.play(FadeIn(wa_t), FadeIn(eth_gem), FadeIn(eth_lbl), run_time=0.6)
        self.play(Create(d_mid), run_time=0.25)

        # Fun: Bitcoin drops from above and bounces
        circle.shift(UP * 1.5)
        sym.shift(UP * 1.5)
        self.play(
            circle.animate.shift(DOWN * 1.5),
            sym.animate.shift(DOWN * 1.5),
            rate_func=rate_functions.ease_out_bounce,
            run_time=1.0,
        )
        self.play(Write(btc_lbl), run_time=0.4)

    # ─────────────────────────────────────────────────────────
    #  Utility — Ethereum diamond gem
    # ─────────────────────────────────────────────────────────
    def _eth_gem(self):
        O = np.array
        top = Polygon(
            O([0,  0.48, 0]), O([ 0.38, 0, 0]), O([-0.38, 0, 0]),
            fill_color=ETH_SILVER, fill_opacity=1, stroke_width=0,
        )
        bot = Polygon(
            O([0, -0.48, 0]), O([ 0.38, 0, 0]), O([-0.38, 0, 0]),
            fill_color="#767676", fill_opacity=1, stroke_width=0,
        )
        hi = Polygon(
            O([0,  0.48, 0]), O([0.38, 0, 0]), O([0, 0.12, 0]),
            fill_color="#E0E0E0", fill_opacity=1, stroke_width=0,
        )
        return VGroup(top, bot, hi)

# Aim : Quantum computers : Harvest now decrypt later
class QuantumThreat(Slide, MovingCameraScene):

    # Self-contained color palette so the class can be copied elsewhere.
    COLORS = {
        "BG": "#000000",
        "GOLD": "#D4AA50",
        "GOLD_BRIGHT": "#F5D87A",
        "GOLD_DIM": "#8A6015",
        "WHITE_T": "#E8E8E8",
        "GREY_T": "#888888",
        "RED_T": "#E05555",
        "GREEN_T": "#55C477",
        "BLUE_T": "#5599E0",
        "ORANGE_T": "#F7931A",
        "DARK_PANEL": "#111111",
    }

    def construct(self):
        self.camera.background_color = self.COLORS["BG"]
        self.camera.frame.save_state()

        self._slide_00_qc_intro()
        self._slide_01_exp_vs_poly()
        self._slide_02_key_table()
        # self._slide_03_aes_doubling()
        # self._slide_04_cost_of_fix()
        self._slide_05_hndl_timeline()
        self._slide_06_shelf_life()
        # self._slide_07_breach()
        self._slide_08_pqc_table()

    # ─────────────────────────────────────────────────────────
    #  Helpers
    # ─────────────────────────────────────────────────────────
    def _make_padlock(self, color, scale=1.0, open_shackle=False):
        body = RoundedRectangle(
            corner_radius=0.08, width=0.7, height=0.55,
            fill_color=color, fill_opacity=1,
            stroke_color=color, stroke_width=2,
        )
        if open_shackle:
            shackle = Arc(
                radius=0.22, start_angle=0, angle=PI,
                stroke_color=color, stroke_width=3,
            ).next_to(body, UP, buff=-0.05).shift(RIGHT * 0.12)
        else:
            shackle = Arc(
                radius=0.22, start_angle=0, angle=PI,
                stroke_color=color, stroke_width=3,
            ).next_to(body, UP, buff=-0.05)
        lock = VGroup(body, shackle).scale(scale)
        return lock

    def _title(self, text, color=None, fs=36):
        if color is None:
            color = self.COLORS["GOLD_BRIGHT"]
        t = Tex(text, font_size=fs, color=color)
        t.to_edge(UP, buff=0.35)
        return t

    def _clear_slide(self):
        """Fade out everything except the camera frame."""
        mobs = [m for m in self.mobjects if m is not self.camera.frame]
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=0.4)

    # ═══════════════════════════════════════════════════════
    #  SLIDE 0 — Quantum Computer Introduction
    # ═══════════════════════════════════════════════════════
    def _slide_00_qc_intro(self):
        # Image starts centred. Text is hidden behind it, then peels out to the right.
        qc_image = ImageMobject("images/qc2.png").scale_to_fit_width(4)
        qc_image.move_to(ORIGIN)

        qc_text = Tex(
            "Impact of \\\\ Quantum Computers \\\\on \\\\ Modern Cryptography",
            font_size=58,
            color=self.COLORS["GOLD_BRIGHT"]
        )
        # qc_text.move_to(ORIGIN)             # same centre — hidden behind image

        left_target  = LEFT  * 3.2
        right_target = RIGHT * 3.2

        # Step 1 — image fades in at centre
        self.play(FadeIn(qc_image), run_time=1)
        self.next_slide()

        # Step 2 — place text behind the image silently, keep image on top,
        #           then slide both apart so text appears to emerge from under
        self.add(qc_text)
        qc_text.move_to(right_target)
        self.bring_to_front(qc_image)
    
        self.play(
            qc_image.animate.move_to(left_target),
            FadeIn(qc_text),
            run_time=1.8,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.next_slide()

        self.play(FadeOut(qc_text), run_time=1)

        # ── Build two-row table on the right half ──────────────
        FS = 36
        right_x = 3.2   # horizontal centre of right half

        # Heading
        heading = Tex(r"Impact of Quantum Computers", font_size=38, color=self.COLORS["GOLD_BRIGHT"])
        heading.move_to(RIGHT * right_x + UP * 2.8)
        self.play(Write(heading))

        # Row labels
        lbl_rsa = Tex(r"RSA / ECC", font_size=FS, color=self.COLORS["WHITE_T"])
        lbl_aes = Tex(r"AES / SHA", font_size=FS, color=self.COLORS["WHITE_T"])

        # Classical complexity labels (both start identical)
        comp_rsa = Tex(r"$\mathcal{O}(2^n)$", font_size=FS, color=self.COLORS["WHITE_T"])
        comp_aes = Tex(r"$\mathcal{O}(2^n)$", font_size=FS, color=self.COLORS["WHITE_T"])

        # Arrange each row: label on left, complexity on right
        row_rsa = VGroup(lbl_rsa, comp_rsa).arrange(RIGHT, buff=1.5)
        row_aes = VGroup(lbl_aes, comp_aes).arrange(RIGHT, buff=1.5)

        # Stack rows and centre in the right half
        table = VGroup(row_rsa, row_aes).arrange(DOWN, buff=1.0, aligned_edge=LEFT)
        table.move_to(RIGHT * right_x + DOWN * 0.5)

        self.play(FadeIn(table))
        self.next_slide()

        # ── Slide advance 1: RSA/ECC — Shor breaks it ──────────
        comp_rsa_new = Tex(r"$\mathcal{O}(n^3)$", font_size=FS+26, color=YELLOW)
        comp_rsa_new.move_to(comp_rsa.get_center())

        self.play(ReplacementTransform(comp_rsa, comp_rsa_new))
        self.next_slide()

        # ── Slide advance 2: AES/SHA — Grover weakens it ───────
        comp_aes_new = Tex(r"$\mathcal{O}(2^{n/2})$", font_size=FS+26, color=YELLOW)
        comp_aes_new.move_to(comp_aes.get_center())

        self.play(ReplacementTransform(comp_aes, comp_aes_new))
        self.next_slide()

        self._clear_slide()

    # ═══════════════════════════════════════════════════════
    #  SLIDE 1 — How Big Is Exponential?
    # ═══════════════════════════════════════════════════════
    def _slide_01_exp_vs_poly(self):
        title = self._title("How Big Is Exponential?")
        self.play(Write(title), run_time=0.5)

        # Column headings
        heading_poly = Tex("Polynomial", font_size=38,
                    color=self.COLORS["GREEN_T"]).move_to(LEFT * 3.5 + UP * 2.0)
        heading_exp  = Tex("Exponential", font_size=38,
                    color=self.COLORS["RED_T"]).move_to(RIGHT * 3.0 + UP * 2.0)

        div_line = DashedLine(UP * 2.5, DOWN * 3.0, color=self.COLORS["GREY_T"],
                      stroke_width=1).move_to(UP * -0.25)

        self.play(Write(heading_poly), Write(heading_exp), Create(div_line), run_time=0.7)

        self.next_slide()  # pause: headings visible

        # Key-size rows
        key_sizes = [64, 128, 256]
        poly_vals = [r"262{,}144", r"2{,}097{,}152", r"16{,}777{,}216"]
        poly_secs = ["$<$ 1 second", "$<$ 1 second", "$<$ 1 second"]
        exp_vals  = [r"1.8 \times 10^{19}", r"3.4 \times 10^{38}", r"1.2 \times 10^{77}"]
        exp_cmp   = [
            "Mass of Earth in kg",
            "Atoms on Earth",
            "Atoms in the universe!",
        ]

        left_col  = VGroup()
        right_col = VGroup()

        for i, n in enumerate(key_sizes):
            y = 1.0 - i * 1.55

            ks = Tex(f"n = {n}", font_size=40,
                      color=self.COLORS["GOLD"]).move_to(UP * y)

            pv = MathTex(r"n^3 = " + poly_vals[i], font_size=32,
                         color=self.COLORS["GREEN_T"])
            pv.move_to(LEFT * 3.5 + UP * y + DOWN * 0.35)
            ps = Tex(poly_secs[i], font_size=24,
                      color=self.COLORS["GREEN_T"])
            ps.next_to(pv, DOWN, buff=0.08)

            ev = MathTex(r"2^n = " + exp_vals[i], font_size=32,
                         color=self.COLORS["RED_T"])
            ev.move_to(RIGHT * 3.0 + UP * y + DOWN * 0.35)
            ec = Tex(exp_cmp[i], font_size=24,
                      color=self.COLORS["ORANGE_T"])
            ec.next_to(ev, DOWN, buff=0.08)

            left_col.add(VGroup(ks, pv, ps))
            right_col.add(VGroup(ev, ec))

        # Animate row by row with pauses
        for i in range(3):
            self.play(FadeIn(left_col[i]), FadeIn(right_col[i]), run_time=0.8)
            self.next_slide()

        # Bottom punchline
        punch = Tex(
            "Polynomial = pocket calculator. Exponential = older than the universe.",
            font_size=20, color=self.COLORS["GOLD_BRIGHT"],
        ).to_edge(DOWN, buff=0.45)
        self.play(Write(punch), run_time=0.8)

        self.next_slide()
        self._clear_slide()

    # ═══════════════════════════════════════════════════════
    #  SLIDE 2 — Classical vs Quantum Break Times (RSA + ECC)
    # ═══════════════════════════════════════════════════════
    def _slide_02_key_table(self):
        title = self._title(r"Quantum Computers Shatter Classical Cryptography", fs=34)
        self.play(Write(title), run_time=0.5)

        # ── Table layout ───────────────────────────────────────
        # Columns: System | Key Size | Classical Time | Quantum Time
        col_widths = [2.0, 2.0, 3.0, 3.2]
        row_h      = 0.60
        FS_H       = 22    # header font size
        FS_D       = 20    # data font size
        total_w    = sum(col_widths)   # 10.2

        headers = ["System", "Key Size", "Classical Time", "Quantum Time"]

        # (system, key_size, classical, quantum, quantum_color_key, use_shor)
        rows_data = [
            ("RSA", "1024-bit", r"10^{15}\text{ yr}", r"\text{seconds}",      "RED_T"),
            ("RSA", "2048-bit", r"10^{25}\text{ yr}", r"\text{minutes}",      "RED_T"),
            ("ECC", "256-bit",  r"10^{30}\text{ yr}", r"\text{minutes}",      "RED_T"),
            ("ECC", "384-bit",  r"10^{45}\text{ yr}", r"\text{hours}",        "RED_T"),
            ("AES", "128-bit",  r"10^{25}\text{ yr}", r"2^{64}\text{ ops}",   "ORANGE_T"),
            ("AES", "256-bit",  r"10^{57}\text{ yr}", r"2^{128}\text{ ops}",  "GREEN_T"),
        ]

        def make_row(cells, fill_col, text_colors, is_header=False, use_math=None):
            if use_math is None:
                use_math = [False] * len(cells)
            grp = VGroup()
            x = -total_w / 2
            for i, (cell, w) in enumerate(zip(cells, col_widths)):
                rect = Rectangle(
                    width=w, height=row_h,
                    fill_color=fill_col, fill_opacity=1,
                    stroke_color=self.COLORS["GOLD"] if is_header else self.COLORS["GOLD_DIM"],
                    stroke_width=2 if is_header else 1,
                )
                rect.move_to(RIGHT * (x + w / 2))
                fs = FS_H if is_header else FS_D
                t = MathTex(cell, font_size=fs, color=text_colors[i]) if use_math[i] \
                    else Tex(cell, font_size=fs, color=text_colors[i])
                t.move_to(rect)
                grp.add(rect, t)
                x += w
            return grp

        # Header
        hdr_colors = [self.COLORS["GOLD_BRIGHT"]] * 4
        header_row = make_row(headers, "#1a1a1a", hdr_colors, is_header=True)
        header_row.move_to(UP * 2.1)

        # Data rows
        data_rows = []
        for idx, (algo, ks, cl, qu, q_col) in enumerate(rows_data):
            fill   = "#0d0d0d" if idx % 2 == 0 else self.COLORS["DARK_PANEL"]
            colors = [
                self.COLORS["WHITE_T"],
                self.COLORS["WHITE_T"],
                self.COLORS["WHITE_T"],
                self.COLORS[q_col],
            ]
            row = make_row([algo, ks, cl, qu], fill, colors,
                           use_math=[False, False, True, True])
            row.move_to(UP * 2.1 + DOWN * (row_h * (idx + 1)))
            data_rows.append(row)

        self.play(Create(header_row), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(r) for r in data_rows], lag_ratio=0.3),
            run_time=2.5,
        )
        self.next_slide()

        # ── Legend + Age-of-universe note ─────────────────────
        shor_note = Tex(
            r"RSA / ECC $\longrightarrow$ Broken by \textbf{Shor's Algorithm} (polynomial time)",
            font_size=20, color=self.COLORS["RED_T"],
        )
        grover_note = Tex(
            r"AES $\longrightarrow$ Weakened by \textbf{Grover's Algorithm} (key strength halved)",
            font_size=20, color=self.COLORS["ORANGE_T"],
        )
        uni_note = Tex(
            r"$\bigstar$ \; Age of the universe $\approx 1.4 \times 10^{10}$ years",
            font_size=24, color=self.COLORS["GOLD_BRIGHT"],
        )
        legend = VGroup(shor_note, grover_note, uni_note).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        legend.next_to(data_rows[-1], DOWN, buff=0.4)
        self.play(LaggedStart(*[FadeIn(n) for n in legend], lag_ratio=0.6), run_time=1.5)

        self.next_slide()
        self._clear_slide()

    # ═══════════════════════════════════════════════════════
    #  SLIDE 3 — AES Needs 2x Key to Be Quantum-Safe
    # ═══════════════════════════════════════════════════════
    def _slide_03_aes_doubling(self):
        title = self._title("Symmetric Crypto: Double the Key")
        self.play(Write(title), run_time=0.5)

        intro = Tex(
            "Grover's algorithm halves symmetric key security.",
            font_size=22, color=self.COLORS["WHITE_T"],
        ).next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro), run_time=0.5)

        self.next_slide()

        # Layout: bars centered, labels INSIDE bars (dark text on colored bg)
        bar_max = 8.0
        bar_h = 0.65
        left_edge = LEFT * 4.0
        y_positions = [0.8, -0.2, -1.2]

        # Row 1: AES-128 Classical = 128-bit security (full bar)
        r1_bar = Rectangle(width=bar_max, height=bar_h,
                   fill_color=self.COLORS["GREEN_T"], fill_opacity=0.9,
                           stroke_width=0).move_to(UP * y_positions[0])
        r1_bar.align_to(left_edge, LEFT)
        r1_lbl = Tex("AES-128  Classical",
                   font_size=19, color=self.COLORS["BG"])
        r1_lbl.move_to(r1_bar).align_to(r1_bar, LEFT).shift(RIGHT * 0.2)
        r1_sec = Tex("128-bit security",
                   font_size=19, color=self.COLORS["BG"])
        r1_sec.move_to(r1_bar).align_to(r1_bar, RIGHT).shift(LEFT * 0.2)

        self.play(GrowFromEdge(r1_bar, LEFT), run_time=0.6)
        self.play(FadeIn(r1_lbl), FadeIn(r1_sec), run_time=0.3)

        self.next_slide()

        # Row 2: AES-128 + Grover = 64-bit (half bar, orange)
        r2_bar = Rectangle(width=bar_max * 0.5, height=bar_h,
                   fill_color=self.COLORS["ORANGE_T"], fill_opacity=0.9,
                           stroke_width=0)
        r2_bar.move_to(UP * y_positions[1]).align_to(left_edge, LEFT)
        r2_lbl = Tex("AES-128 + Grover",
                   font_size=19, color=self.COLORS["BG"])
        r2_lbl.move_to(r2_bar).align_to(r2_bar, LEFT).shift(RIGHT * 0.2)
        r2_sec = Tex("64-bit",
                   font_size=19, color=self.COLORS["BG"])
        r2_sec.move_to(r2_bar).align_to(r2_bar, RIGHT).shift(LEFT * 0.1)
        r2_warn = Tex("NOT SAFE",
                font_size=20, color=self.COLORS["RED_T"])
        r2_warn.next_to(r2_bar, RIGHT, buff=0.3)

        self.play(GrowFromEdge(r2_bar, LEFT), run_time=0.6)
        self.play(FadeIn(r2_lbl), FadeIn(r2_sec), FadeIn(r2_warn), run_time=0.3)

        self.next_slide()

        # Row 3: AES-256 + Grover = 128-bit security (full bar, green)
        r3_bar = Rectangle(width=bar_max, height=bar_h,
                   fill_color=self.COLORS["GREEN_T"], fill_opacity=0.9,
                           stroke_width=0)
        r3_bar.move_to(UP * y_positions[2]).align_to(left_edge, LEFT)
        r3_lbl = Tex("AES-256 + Grover",
                   font_size=19, color=self.COLORS["BG"])
        r3_lbl.move_to(r3_bar).align_to(r3_bar, LEFT).shift(RIGHT * 0.2)
        r3_sec = Tex("128-bit security",
                   font_size=19, color=self.COLORS["BG"])
        r3_sec.move_to(r3_bar).align_to(r3_bar, RIGHT).shift(LEFT * 0.2)

        self.play(GrowFromEdge(r3_bar, LEFT), run_time=0.6)
        self.play(FadeIn(r3_lbl), FadeIn(r3_sec), run_time=0.3)

        self.next_slide()

        # Brace connecting rows 1 and 3
        brace = Brace(VGroup(r1_bar, r3_bar), RIGHT, color=self.COLORS["GREEN_T"])
        brace_lbl = VGroup(
            Tex("Same security", font_size=17, color=self.COLORS["GREEN_T"]),
            Tex("level", font_size=17, color=self.COLORS["GREEN_T"])
        ).arrange(DOWN, buff=0.05)
        brace_lbl.next_to(brace, RIGHT, buff=0.1)
        self.play(Create(brace), FadeIn(brace_lbl), run_time=0.5)

        takeaway = Tex(
            "Fix: double the key.  AES-256 is already a NIST standard (2001).",
            font_size=19, color=self.COLORS["GOLD_BRIGHT"],
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(takeaway), run_time=0.6)

        self.next_slide()
        self._clear_slide()

    # ═══════════════════════════════════════════════════════
    #  SLIDE 4 — Cost of the Fix (Hard vs Easy)
    # ═══════════════════════════════════════════════════════
    def _slide_04_cost_of_fix(self):
        title = self._title("The Cost of the Fix")
        self.play(Write(title), run_time=0.5)

        box_w, box_h = 5.2, 4.0

        # Left box — PUBLIC KEY (hard)
        left_box = RoundedRectangle(
            corner_radius=0.15, width=box_w, height=box_h,
            fill_color=self.COLORS["DARK_PANEL"], fill_opacity=1,
            stroke_color=self.COLORS["RED_T"], stroke_width=2.5,
        ).move_to(LEFT * 3.3 + DOWN * 0.3)

        left_title = Tex("PUBLIC KEY CRYPTO", font_size=22,
                  color=self.COLORS["RED_T"])
        left_title.move_to(left_box.get_top() + DOWN * 0.35)
        left_sub = Tex("RSA, ECDH, ECDSA", font_size=16,
                color=self.COLORS["GREY_T"]).next_to(left_title, DOWN, buff=0.08)

        left_bullets = VGroup(*[
            Tex(t, font_size=20, color=self.COLORS["WHITE_T"])
            for t in [
                "New math foundations",
                "New protocols needed",
                "Replace entire PKI",
                "Years of migration",
                "Backward compat issues",
            ]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        left_bullets.next_to(left_sub, DOWN, buff=0.2)
        left_bullets.align_to(left_box, LEFT).shift(RIGHT * 0.4)

        # Right box — SYMMETRIC KEY (easy)
        right_box = RoundedRectangle(
            corner_radius=0.15, width=box_w, height=box_h,
            fill_color=self.COLORS["DARK_PANEL"], fill_opacity=1,
            stroke_color=self.COLORS["GREEN_T"], stroke_width=2.5,
        ).move_to(RIGHT * 3.3 + DOWN * 0.3)

        right_title = Tex("SYMMETRIC KEY CRYPTO", font_size=20,
                   color=self.COLORS["GREEN_T"])
        right_title.move_to(right_box.get_top() + DOWN * 0.35)
        right_sub = Tex("AES, ChaCha20", font_size=16,
                 color=self.COLORS["GREY_T"]).next_to(right_title, DOWN, buff=0.08)

        right_bullets = VGroup(*[
            Tex(t, font_size=20, color=self.COLORS["WHITE_T"])
            for t in [
                "AES-128 $\rightarrow$ AES-256",
                "Config change only",
                "Already standardized",
                "Done in days",
            ]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        right_bullets.next_to(right_sub, DOWN, buff=0.2)
        right_bullets.align_to(right_box, LEFT).shift(RIGHT * 0.4)

        self.play(Create(left_box), Create(right_box), run_time=0.7)
        self.play(
            FadeIn(left_title), FadeIn(left_sub),
            FadeIn(right_title), FadeIn(right_sub),
            run_time=0.5,
        )
        self.play(
            LaggedStart(*[FadeIn(b) for b in left_bullets], lag_ratio=0.2),
            run_time=1.5,
        )
        self.play(
            LaggedStart(*[FadeIn(b) for b in right_bullets], lag_ratio=0.2),
            run_time=1.5,
        )

        # Stamps
        stamp_hard = Tex("HARD", font_size=48, color=self.COLORS["RED_T"])
        stamp_hard.set_stroke(self.COLORS["RED_T"], width=3)
        stamp_hard.move_to(left_box.get_center() + DOWN * 0.7)
        stamp_hard.rotate(-PI / 12)

        stamp_easy = Tex("EASY", font_size=48, color=self.COLORS["GREEN_T"])
        stamp_easy.set_stroke(self.COLORS["GREEN_T"], width=3)
        stamp_easy.move_to(right_box.get_center() + DOWN * 0.7)
        stamp_easy.rotate(PI / 12)

        self.play(GrowFromCenter(stamp_hard), run_time=0.7)
        self.play(GrowFromCenter(stamp_easy), run_time=0.7)

        self.next_slide()
        self._clear_slide()

    # ═══════════════════════════════════════════════════════
    #  SLIDE 5 — Harvest Now, Decrypt Later
    # ═══════════════════════════════════════════════════════
    def _slide_05_hndl_timeline(self):
        title = self._title("Harvest Now, Decrypt Later")
        self.play(Write(title), run_time=0.5)

        timeline = Line(LEFT * 5.5, RIGHT * 5.5, color=self.COLORS["GREY_T"],
                        stroke_width=2).shift(DOWN * 0.2)
        self.play(Create(timeline), run_time=0.7)

        positions = {"2026": -4.5, "2030?": 0, "2035?": 4.5}
        tick_h = 0.25

        # 2026
        t_2026 = Line(
            UP * tick_h + RIGHT * positions["2026"] + DOWN * 0.2,
            DOWN * tick_h + RIGHT * positions["2026"] + DOWN * 0.2,
            color=self.COLORS["GOLD"], stroke_width=2,
        )
        lbl_2026 = Tex("2026", font_size=20,
                         color=self.COLORS["GOLD"]).next_to(t_2026, DOWN, buff=0.12)
        padlock_closed = self._make_padlock(self.COLORS["GOLD"], scale=0.6)
        padlock_closed.next_to(t_2026, UP, buff=0.25)
        msg_sent = VGroup(
            Tex("Message sent.", font_size=16, color=self.COLORS["WHITE_T"]),
            Tex("Encrypted.", font_size=16, color=self.COLORS["WHITE_T"])
        ).arrange(DOWN, buff=0.05)
        msg_sent.next_to(padlock_closed, UP, buff=0.15)
        self.play(Create(t_2026), FadeIn(lbl_2026),
                  FadeIn(padlock_closed), FadeIn(msg_sent), run_time=0.6)

        # 2030
        t_2030 = Line(
            UP * tick_h + RIGHT * positions["2030?"] + DOWN * 0.2,
            DOWN * tick_h + RIGHT * positions["2030?"] + DOWN * 0.2,
            color=self.COLORS["GREY_T"], stroke_width=2,
        )
        lbl_2030 = Tex("2030?", font_size=20,
                         color=self.COLORS["GREY_T"]).next_to(t_2030, DOWN, buff=0.12)
        self.play(Create(t_2030), FadeIn(lbl_2030), run_time=0.4)

        # 2035
        t_2035 = Line(
            UP * tick_h + RIGHT * positions["2035?"] + DOWN * 0.2,
            DOWN * tick_h + RIGHT * positions["2035?"] + DOWN * 0.2,
            color=self.COLORS["RED_T"], stroke_width=2,
        )
        lbl_2035 = Tex("2035?", font_size=20,
                         color=self.COLORS["RED_T"]).next_to(t_2035, DOWN, buff=0.12)
        q_label = VGroup(
            Tex("Quantum computer", font_size=16, color=self.COLORS["BLUE_T"]),
            Tex("arrives.", font_size=16, color=self.COLORS["BLUE_T"])
        ).arrange(DOWN, buff=0.05)
        q_label.next_to(t_2035, UP, buff=0.25)
        self.play(Create(t_2035), FadeIn(lbl_2035), FadeIn(q_label),
                  run_time=0.6)

        # Curved arrow ###
        captured_arrow = CurvedArrow(
            LEFT * 4.5 + DOWN * 0.2, RIGHT * 4.5 + DOWN * 0.2,
            color=self.COLORS["RED_T"], stroke_width=2, angle=-TAU / 4,
        )
        self.play(Create(captured_arrow), run_time=1.2)

        vault_label = Tex("Captured copy sits in vault...",
                   font_size=18, color=self.COLORS["GREY_T"])
        vault_label.next_to(captured_arrow, DOWN, buff=0.15)
        self.play(FadeIn(vault_label), run_time=0.4)

        padlock_open = self._make_padlock(self.COLORS["RED_T"], scale=0.6, open_shackle=True)
        padlock_open.move_to(RIGHT * 4.5 + DOWN * 1.5)
        open_label = Tex("Data READABLE", font_size=17,
                  color=self.COLORS["RED_T"]).next_to(padlock_open, DOWN, buff=0.1)
        self.play(
            ReplacementTransform(padlock_closed.copy(), padlock_open),
            FadeIn(open_label), run_time=0.8,
        )

        punchline = Tex(
            "Today's data.  Tomorrow's breach.",
            font_size=28, color=self.COLORS["GOLD_BRIGHT"],
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(punchline), Flash(punchline, color=self.COLORS["GOLD_BRIGHT"],
              line_length=0.2), run_time=0.8)

        self.next_slide()
        self._clear_slide()

    # ═══════════════════════════════════════════════════════
    #  SLIDE 6 — Data With Long Shelf Life
    # ═══════════════════════════════════════════════════════
    def _slide_06_shelf_life(self):
        title = self._title("What Data Has a Long Shelf Life?")
        self.play(Write(title), run_time=0.5)

        # Fixed-column grid — absolute positions, NO overlap possible
        rows = [
            ("Medical Records",  3.5, "30 years",      self.COLORS["GOLD"]),
            ("State Secrets",    4.5, "50+ years",     self.COLORS["ORANGE_T"]),
            ("Identity Docs",    5.0, "Lifetime",      self.COLORS["RED_T"]),
            ("Financial Data",   2.8, "10-20 yrs",     self.COLORS["GOLD_DIM"]),
            ("Trade Secrets",    4.0, "Decades",       self.COLORS["ORANGE_T"]),
            ("Encryption Keys",  4.5, "Until rotated", self.COLORS["RED_T"]),
        ]

        all_rows = VGroup()
        checks = []
        row_h = 0.60
        start_y = 1.5

        for i, (name, bar_w, dur, bar_col) in enumerate(rows):
            y = start_y - i * row_h

            row_bg = Rectangle(
                width=12.0, height=row_h - 0.06,
                fill_color="#0a0a0a" if i % 2 == 0 else "#0f0f0f",
                fill_opacity=1, stroke_width=0,
            ).move_to(UP * y)

            label = Tex(name, font_size=20, color=self.COLORS["WHITE_T"])
            label.move_to(LEFT * 4.5 + UP * y)

            bar = Rectangle(
                width=bar_w, height=0.22,
                fill_color=bar_col, fill_opacity=0.85, stroke_width=0,
            ).move_to(LEFT * 0.3 + UP * y)

            dur_text = Tex(dur, font_size=18, color=self.COLORS["GREY_T"])
            dur_text.move_to(RIGHT * 3.0 + UP * y)

            check = Tex("Y", font_size=22, color=self.COLORS["GREEN_T"])
            check.move_to(RIGHT * 5.0 + UP * y)
            checks.append(check)

            row_grp = VGroup(row_bg, label, bar, dur_text, check)
            all_rows.add(row_grp)

        # Column headers
        hdr_name = Tex("DATA TYPE", font_size=16,
                color=C_GOLD_BRIGHT).move_to(LEFT * 4.5 + UP * 2.1)
        hdr_life = Tex("SENSITIVITY", font_size=16,
                color=C_GOLD_BRIGHT).move_to(LEFT * 0.3 + UP * 2.1)
        hdr_dur  = Tex("DURATION", font_size=16,
                color=C_GOLD_BRIGHT).move_to(RIGHT * 3.0 + UP * 2.1)
        hdr_chk  = Tex("2035?", font_size=16,
                color=C_GOLD_BRIGHT).move_to(RIGHT * 5.0 + UP * 2.1)

        self.play(FadeIn(hdr_name), FadeIn(hdr_life),
                  FadeIn(hdr_dur), FadeIn(hdr_chk), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(r) for r in all_rows], lag_ratio=0.3),
            run_time=3.0,
        )
        self.play(*[Flash(c, color=self.COLORS["GREEN_T"], line_length=0.15)
                    for c in checks], run_time=0.5)

        note = Tex(
            "All of this data will still be sensitive when quantum computers arrive.",
            font_size=19, color=self.COLORS["GOLD_BRIGHT"],
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.7)

        self.next_slide()
        self._clear_slide()

    # ═══════════════════════════════════════════════════════
    #  SLIDE 7 — The Breach Already Happened
    # ═══════════════════════════════════════════════════════
    def _slide_07_breach(self):
        title = self._title("The Breach Already Happened.")
        self.play(Write(title), run_time=0.5)

        # ── LEFT COLUMN: TODAY ──
        left_box = RoundedRectangle(
            corner_radius=0.15, width=5.0, height=4.0,
            fill_color=self.COLORS["DARK_PANEL"], fill_opacity=1,
            stroke_color=self.COLORS["GOLD"], stroke_width=2,
        ).move_to(LEFT * 3.5 + DOWN * 0.4)

        today_hdr = Tex("TODAY  2026", font_size=24,
                 color=self.COLORS["GOLD"])
        today_hdr.move_to(left_box.get_top() + DOWN * 0.4)

        today_l1 = Tex("Your data is encrypted.",
                font_size=22, color=self.COLORS["WHITE_T"])
        today_l2 = Tex("RSA / ECDH protects it.",
                font_size=22, color=self.COLORS["WHITE_T"])
        today_l3 = Tex("Someone copies the",
                font_size=22, color=self.COLORS["GREY_T"])
        today_l4 = Tex("ciphertext and stores it.",
                font_size=22, color=self.COLORS["RED_T"])

        today_lines = VGroup(today_l1, today_l2, today_l3, today_l4)
        today_lines.arrange(DOWN, buff=0.18)
        today_lines.next_to(today_hdr, DOWN, buff=0.45)

        left_grp = VGroup(left_box, today_hdr, today_lines)
        self.play(FadeIn(left_grp), run_time=0.8)

        self.next_slide()

        # ── CENTER ARROW ──
        arrow = Arrow(
            LEFT * 0.8 + DOWN * 0.4,
            RIGHT * 0.8 + DOWN * 0.4,
            color=self.COLORS["RED_T"], stroke_width=3, buff=0.1,
        )
        arr_lbl = Tex("10+ years", font_size=15,
                       color=WHITE).next_to(arrow, UP, buff=0.08)
        self.play(Create(arrow), FadeIn(arr_lbl), run_time=0.7)

        # ── RIGHT COLUMN: 2035 ──
        right_box = RoundedRectangle(
            corner_radius=0.15, width=5.0, height=4.0,
            fill_color=self.COLORS["DARK_PANEL"], fill_opacity=1,
            stroke_color=self.COLORS["RED_T"], stroke_width=2,
        ).move_to(RIGHT * 3.5 + DOWN * 0.4)

        future_hdr = Tex("FUTURE  2035", font_size=24,
                  color=self.COLORS["RED_T"])
        future_hdr.move_to(right_box.get_top() + DOWN * 0.4)

        fut_l1 = Tex("Quantum computer arrives.",
                  font_size=22, color=self.COLORS["BLUE_T"])
        fut_l2 = Tex("Stored ciphertext is",
                  font_size=22, color=self.COLORS["WHITE_T"])
        fut_l3 = Tex("decrypted in minutes.",
                  font_size=22, color=self.COLORS["RED_T"])
        fut_l4 = Tex("Your data is exposed.",
                  font_size=22, color=self.COLORS["RED_T"])

        future_lines = VGroup(fut_l1, fut_l2, fut_l3, fut_l4)
        future_lines.arrange(DOWN, buff=0.18)
        future_lines.next_to(future_hdr, DOWN, buff=0.45)

        right_grp = VGroup(right_box, future_hdr, future_lines)
        self.play(FadeIn(right_grp), run_time=0.8)

        self.next_slide()

        # ── BOTTOM PUNCHLINE ──
        final_text = Tex(
            "The wall still stands. The data is already copied.",
            font_size=22, color=self.COLORS["GOLD_BRIGHT"],
        ).to_edge(DOWN, buff=0.35)
        self.play(Write(final_text), run_time=1.2)
        self.play(Flash(final_text, color=self.COLORS["GOLD_BRIGHT"], line_length=0.2),
                  run_time=0.5)

        self.next_slide()
        self._clear_slide()

    # ═══════════════════════════════════════════════════════
    #  SLIDE 8 — Post-Quantum Replacements (Last Slide)
    # ═══════════════════════════════════════════════════════
    def _slide_08_pqc_table(self):
        title0 = self._title("Last Slide", fs=40)
        self.play(Write(title0), run_time=0.5)

        self.wait(2)
        title1 = Tex("Post-Quantum Cryptography",  font_size=40, color=self.COLORS["GOLD_BRIGHT"])
        title1.next_to(title0, DOWN, buff=0.35)
        self.play(Write(title1), run_time=0.5)

        subtitle = Tex(
            "Post-Quantum Replacements for Public Key Algorithms",
            font_size=22, color=self.COLORS["GREY_T"],
        ).next_to(title1, DOWN, buff=0.15)
        self.play(FadeIn(subtitle), run_time=0.3)

        # 4 columns
        col_w = [2.6, 3.2, 3.4, 2.6]
        total_w = sum(col_w)
        row_h = 0.55
        col_starts = []
        x = -total_w / 2
        for w in col_w:
            col_starts.append(x + w / 2)
            x += w

        def _row(cells, colors, fill, stroke_col, is_hdr=False):
            grp = VGroup()
            for i, (txt, w) in enumerate(zip(cells, col_w)):
                r = Rectangle(
                    width=w, height=row_h,
                    fill_color=fill, fill_opacity=1,
                    stroke_color=stroke_col,
                    stroke_width=1.5 if is_hdr else 1,
                )
                r.move_to(RIGHT * col_starts[i])
                fs = 17 if is_hdr else 16
                t = Tex(txt, font_size=fs,
                         color=colors[i])
                t.move_to(r)
                grp.add(r, t)
            return grp

        hdr = _row(
            ["Classical", "PQC Replacement", "Based On", "Use Case"],
            [self.COLORS["GOLD_BRIGHT"]] * 4, "#1a1a1a", self.COLORS["GOLD"], is_hdr=True,
        )

        # Factually verified:
        # ML-KEM  = FIPS 203 (Aug 2024) — replaces key encapsulation
        # ML-DSA  = FIPS 204 (Aug 2024) — replaces digital signatures
        # SLH-DSA = FIPS 205 (Aug 2024) — SPHINCS+ hash-based sigs
        # FN-DSA  = FALCON  (draft)     — NTRU lattice sigs
        data = [
            ["RSA (encrypt)",  "ML-KEM (Kyber)",       "Module LWE",     "Key exchange"],
            ["ECDH",           "ML-KEM (Kyber)",       "Module LWE",     "Key exchange"],
            ["RSA (sign)",     "ML-DSA (Dilithium)",   "Module LWE",     "Signatures"],
            ["ECDSA",          "ML-DSA (Dilithium)",   "Module LWE",     "Signatures"],
            ["EdDSA",          "SLH-DSA (SPHINCS+)",   "Hash-based",     "Signatures"],
            ["DSA",            "FN-DSA (FALCON)",      "NTRU Lattices",  "Signatures"],
        ]

        rows = []
        for idx, cells in enumerate(data):
            fill = "#0d0d0d" if idx % 2 == 0 else self.COLORS["DARK_PANEL"]
            colors = [self.COLORS["WHITE_T"], self.COLORS["GREEN_T"], self.COLORS["BLUE_T"], WHITE]
            rows.append(_row(cells, colors, fill, self.COLORS["GOLD_DIM"]))

        table_top = UP * 1.1
        hdr.move_to(table_top)
        for i, r in enumerate(rows):
            r.move_to(table_top + DOWN * (row_h * (i + 1)))

        self.play(Create(hdr), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.3),
            run_time=3.0,
        )

        footer = Tex(
            "NIST FIPS 203, 204, 205 finalized August 2024.",
            font_size=17, color=self.COLORS["GOLD_BRIGHT"],
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(footer), run_time=0.4)

        self.next_slide()

        # ═══════════════════════════════════════════════════════
        #  QUANTUM PYRAMID — Cryptography in the Quantum Era
        #  Uses piryamid.py geometry (imported via `from piryamid import *`)
        #
        #  Tier boundaries used:
        #    Y0 = -3.80  base
        #    Y2 = -1.40  base → PQC algorithms
        #    Y5 =  0.50  PQC algorithms → Protocols
        #    Y6 =  1.60  Protocols → Applications
        #    Y7 =  4.00  apex
        #
        #  Structure (bottom → top):
        #    Tier 1 (Y0→Y2): IFP/ECDLP/DLP  →  LWE/NTRU/Hash (transformation)
        #    Tier 2 (Y2→Y5): PQC Algorithms (ML-KEM, ML-DSA, SLH-DSA, FN-DSA)
        #    Tier 3 (Y5→Y6): Protocols (TLS 1.3, Signal, SSH)
        #    Apex   (Y6→Y7): Applications
        # ═══════════════════════════════════════════════════════
        self._clear_slide()
        self.play(Restore(self.camera.frame), run_time=0.5)
        C = self.COLORS

        # ── Outer triangle shell ──────────────────────────────
        shell = Polygon(
            APEX, BL, BR,
            color=C["GOLD"], stroke_width=3.0,
            fill_color=C["BG"], fill_opacity=1,
        )
        self.play(Create(shell), run_time=1.2)
        self.next_slide()

        # ── Layout helpers ────────────────────────────────────
        # _item3: symbol (top) + bold name + small sub — for the base tier
        def _item3(sym, sym_col, name, sub, x, y, fs_n=26, fs_s=15):
            s = Tex(sym,  font_size=28,   color=sym_col)
            n = Tex(name, font_size=fs_n, color=C["WHITE_T"])
            b = Tex(sub,  font_size=fs_s, color=C["GREY_T"])
            return VGroup(s, n, b).arrange(DOWN, buff=0.10).move_to([x, y, 0])

        # _item2: bold name + small sub — for upper tiers
        def _item2(name, sub, x, y, col, fs_n=17, fs_s=12):
            n = Tex(name, font_size=fs_n, color=col)
            b = Tex(sub,  font_size=fs_s, color=C["GREY_T"])
            return VGroup(n, b).arrange(DOWN, buff=0.06).move_to([x, y, 0])

        # ─────────────────────────────────────────────────────
        # TIER 1 — Phase 1: Classical Hard Problems (RED)
        #   Y0=-3.80 → Y2=-1.40,  height 2.40
        #   Banner near base  →  3 items side-by-side in wide zone
        # ─────────────────────────────────────────────────────
        T1_BAN_Y  = Y0 + 0.30           # -3.50  — label near base edge
        T1_CONT_Y = -2.50               # content centre (well above banner)
        T1_CX     = hw(T1_CONT_Y) * 0.46   # 4.58 × 0.46 ≈ 2.11

        t1_bg_r  = trapezoid(Y0, Y2, C["RED_T"],  opacity=0.06)
        t1_div_r = tier_div(Y2, sw=2.5, col=C["RED_T"])
        t1_lbl_r = Tex(
            r"\textbf{Classical Hard Problems} \quad --- \quad Broken by Shor's Algorithm",
            font_size=20, color=C["RED_T"],
        ).move_to([0, T1_BAN_Y, 0])

        ifp   = _item3(r"$\times$", C["RED_T"], r"\textbf{IFP}",   r"RSA",      -T1_CX, T1_CONT_Y)
        ecdlp = _item3(r"$\times$", C["RED_T"], r"\textbf{ECDLP}", r"ECC",           0, T1_CONT_Y)
        dlp   = _item3(r"$\times$", C["RED_T"], r"\textbf{DLP}",   r"DH / DSA", +T1_CX, T1_CONT_Y)

        self.play(FadeIn(t1_bg_r), run_time=0.4)
        self.play(Create(t1_div_r), Write(t1_lbl_r), run_time=0.7)
        self.play(
            LaggedStart(FadeIn(ifp), FadeIn(ecdlp), FadeIn(dlp), lag_ratio=0.3),
            run_time=1.2,
        )
        self.next_slide()

        # ─────────────────────────────────────────────────────
        # TIER 1 — Phase 2: Quantum-Hard Foundations (BLUE)
        #   Same positions — red content fades out, blue fades in
        # ─────────────────────────────────────────────────────
        t1_bg_b  = trapezoid(Y0, Y2, C["BLUE_T"], opacity=0.06)
        t1_div_b = tier_div(Y2, sw=2.5, col=C["BLUE_T"])
        t1_lbl_b = Tex(
            r"\textbf{Quantum-Hard Foundations}",
            font_size=22, color=C["BLUE_T"],
        ).move_to([0, T1_BAN_Y, 0])

        lwe  = _item3(r"$\checkmark$", C["BLUE_T"], r"\textbf{LWE}",  r"Lattices", -T1_CX, T1_CONT_Y)
        ntru = _item3(r"$\checkmark$", C["BLUE_T"], r"\textbf{NTRU}", r"Lattices",       0, T1_CONT_Y)
        hsh  = _item3(r"$\checkmark$", C["BLUE_T"], r"\textbf{Hash}", r"One-way",  +T1_CX, T1_CONT_Y)

        self.play(
            FadeOut(VGroup(ifp, ecdlp, dlp, t1_bg_r, t1_lbl_r, t1_div_r)),
            run_time=0.6,
        )
        self.play(
            FadeIn(t1_bg_b), Create(t1_div_b), Write(t1_lbl_b),
            run_time=0.7,
        )
        self.play(
            LaggedStart(FadeIn(lwe), FadeIn(ntru), FadeIn(hsh), lag_ratio=0.3),
            run_time=1.2,
        )
        self.next_slide()

        # ─────────────────────────────────────────────────────
        # TIER 2 — PQC Algorithms (GREEN)
        #   Y2=-1.40 → Y5=0.50,  height 1.90
        #   Banner just above Y2  →  2 rows of 2 algorithms
        #     Row 2 (lower) at -0.70,  Row 1 (upper) at -0.10
        # ─────────────────────────────────────────────────────
        T2_BAN_Y  = Y2 + 0.24           # -1.16
        T2_ROW2_Y = -0.72               # lower row
        T2_ROW1_Y = -0.12               # upper row
        T2_CX     = hw(-0.42) * 0.45    # 3.09 × 0.45 ≈ 1.39

        t2_bg  = trapezoid(Y2, Y5, C["GREEN_T"], opacity=0.06)
        t2_div = tier_div(Y5, sw=2.0, col=C["GREEN_T"])
        t2_lbl = Tex(
            r"\textbf{PQC Algorithms}",
            font_size=22, color=C["GREEN_T"],
        ).move_to([0, T2_BAN_Y, 0])

        mlkem  = _item2(r"\textbf{ML-KEM}",  r"Kyber",     -T2_CX, T2_ROW1_Y, C["GREEN_T"])
        mldsa  = _item2(r"\textbf{ML-DSA}",  r"Dilithium", +T2_CX, T2_ROW1_Y, C["GREEN_T"])
        slhdsa = _item2(r"\textbf{SLH-DSA}", r"SPHINCS+",  -T2_CX, T2_ROW2_Y, C["GREEN_T"])
        fndsa  = _item2(r"\textbf{FN-DSA}",  r"FALCON",    +T2_CX, T2_ROW2_Y, C["GREEN_T"])

        self.play(FadeIn(t2_bg), run_time=0.4)
        self.play(Create(t2_div), Write(t2_lbl), run_time=0.7)
        self.play(
            LaggedStart(FadeIn(mlkem), FadeIn(mldsa), FadeIn(slhdsa), FadeIn(fndsa), lag_ratio=0.25),
            run_time=1.2,
        )
        self.next_slide()

        # ─────────────────────────────────────────────────────
        # TIER 3 — Protocols (ORANGE)
        #   Y5=0.50 → Y6=1.60,  height 1.10
        #   Banner just above Y5  →  3 items in a single row
        #   hw(1.10) ≈ 2.03  →  items at 0, ±T3_CX
        # ─────────────────────────────────────────────────────
        T3_BAN_Y  = Y5 + 0.17           # 0.67
        T3_CONT_Y = 1.10                # content centre
        T3_CX     = hw(T3_CONT_Y) * 0.43   # 2.03 × 0.43 ≈ 0.87

        t3_bg  = trapezoid(Y5, Y6, C["ORANGE_T"], opacity=0.10)
        t3_div = tier_div(Y6, sw=2.0, col=C["ORANGE_T"])
        t3_lbl = Tex(
            r"\textbf{Protocols}",
            font_size=20, color=C["ORANGE_T"],
        ).move_to([0, T3_BAN_Y, 0])

        tls    = _item2(r"\textbf{TLS 1.3}", r"HTTPS", -T3_CX, T3_CONT_Y, C["ORANGE_T"], fs_n=15, fs_s=11)
        signal = _item2(r"\textbf{Signal}",  r"E2E",        0, T3_CONT_Y, C["ORANGE_T"], fs_n=15, fs_s=11)
        ssh    = _item2(r"\textbf{SSH}",     r"PGP",   +T3_CX, T3_CONT_Y, C["ORANGE_T"], fs_n=15, fs_s=11)

        self.play(FadeIn(t3_bg), run_time=0.4)
        self.play(Create(t3_div), Write(t3_lbl), run_time=0.6)
        self.play(
            LaggedStart(FadeIn(tls), FadeIn(signal), FadeIn(ssh), lag_ratio=0.25),
            run_time=1.0,
        )
        self.next_slide()

        # ─────────────────────────────────────────────────────
        # APEX — Applications (GOLD)
        #   Y6=1.60 → Y7=4.00  (pyramid narrows sharply)
        #   Label at 1.82  →  row1 at 2.30 (2 items ±CX)
        #                   →  row2 at 2.75 (1 centred)
        #   hw(2.30) ≈ 1.19,  hw(2.75) ≈ 0.88
        # ─────────────────────────────────────────────────────
        APEX_LBL_Y = Y6 + 0.22          # 1.82
        APEX_R1_Y  = 2.30               # two items side-by-side
        APEX_R2_Y  = 2.75               # one centred item
        APEX_CX    = hw(APEX_R1_Y) * 0.38  # 1.19 × 0.38 ≈ 0.45

        apex_lbl  = Tex(r"\textbf{Applications}", font_size=18, color=C["GOLD_BRIGHT"]).move_to([0, APEX_LBL_Y, 0])
        apex_r1_l = Tex(r"\textbf{HTTPS}",       font_size=13, color=C["GOLD"]).move_to([-APEX_CX, APEX_R1_Y, 0])
        apex_r1_r = Tex(r"\textbf{Banking}",      font_size=13, color=C["GOLD"]).move_to([+APEX_CX, APEX_R1_Y, 0])
        apex_r2   = Tex(r"\textbf{Messaging}",    font_size=12, color=C["GOLD"]).move_to([0,         APEX_R2_Y, 0])

        self.play(Write(apex_lbl), run_time=0.6)
        self.play(
            LaggedStart(FadeIn(apex_r1_l), FadeIn(apex_r1_r), FadeIn(apex_r2), lag_ratio=0.3),
            run_time=0.9,
        )
        self.next_slide()

class LastSlide(Slide, MovingCameraScene):
    """
    Structure:
      Slide 0  — fade-in intro (one-shot, press → to start loop)
      Slide 1  — LOOP START  [loop=True]
                   Phase 1: normal spiral  (6 waypoints)
                   Phase 2: prime filter   (3 waypoints)
                   Phase 3: Ulam crossfade + hold
                   Phase 4: return to start state
                 LOOP END   (press → to exit)
      Slide 2  — blank black (graceful exit)
    """

    # ─────────────────────────────────────────────────────────
    #  PALETTE
    # ─────────────────────────────────────────────────────────
    BG          = ManimColor("#000000")
    GOLD        = ManimColor("#D4AA50")
    GOLD_BRIGHT = ManimColor("#F5D87A")
    GOLD_DIM    = ManimColor("#2A1A04")
    GOLD_MID    = ManimColor("#8A6015")
    PRIME_COLOR = ManimColor("#F5D87A")
    COMP_COLOR  = ManimColor("#1A1208")
    WHITE_T     = ManimColor("#E8E8E8")

    # ─────────────────────────────────────────────────────────
    #  TIMING
    # ─────────────────────────────────────────────────────────
    SEG_NORMAL  = 9.0    # seconds per normal spiral waypoint
    SEG_PRIME   = 11.0   # seconds per prime-filter waypoint
    ULAM_IN     = 6.0    # circle → Ulam crossfade
    ULAM_HOLD   = 22.0   # Ulam hold time
    ULAM_OUT    = 5.0    # Ulam → circle crossfade
    CROSSFADE   = 3.5    # prime filter fade in/out
    ZOOM_AMT    = 0.18   # camera zoom fraction (0.18 = ±18%)
    BASE_W      = 14.2   # default Manim frame width

    # ─────────────────────────────────────────────────────────
    #  GEOMETRY
    # ─────────────────────────────────────────────────────────
    RADIUS    = 3.0
    NUM_LINES = 220

    WAYPOINTS_NORMAL = [
        (200,   2),   # binary star
        (200,   3),   # trefoil
        (200,  51),   # mandala burst
        (300, 137),   # golden ratio sunflower
        (300,  89),   # Fibonacci daisy
        (360, 120),   # 3-fold symmetry
        (360, 144),   # 5-fold — this is also LOOP END state
    ]

    WAYPOINTS_PRIME = [
        (360, 144),   # continues from normal end
        (360,  72),   # prime constellation
        (300, 137),   # sunflower primes only
        (300, 150),   # dense prime weave
    ]

    ULAM_N     = 361
    ULAM_SCALE = 0.32
    ULAM_DOT_R = 0.055

    # ── Loop start / end tracker state ────────────────────────
    # The loop restarts from WAYPOINTS_NORMAL[0].
    # At the end of Phase 4 we reset all trackers to exactly
    # this state so the restart is seamless.
    LOOP_START_N = float(WAYPOINTS_NORMAL[0][0])   # 200.0
    LOOP_START_M = float(WAYPOINTS_NORMAL[0][1])   # 2.0

    @staticmethod
    def _sieve(n):
        """Generate set of primes up to n using Sieve of Eratosthenes."""
        is_p = [True] * (n + 1)
        is_p[0] = is_p[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_p[i]:
                for j in range(i * i, n + 1, i):
                    is_p[j] = False
        return set(i for i, v in enumerate(is_p) if v)

    @staticmethod
    def _ulam_xy(n):
        """Map integer n to (col, row) in the Ulam square spiral."""
        if n == 1:
            return (0, 0)
        x = y = 0
        dx, dy = 0, -1
        i = 1
        while i < n:
            if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
                dx, dy = -dy, dx
            x += dx
            y += dy
            i += 1
        return (x, y)

    def construct(self):
        # Generate primes set for this instance
        PRIMES = self._sieve(500)
        
        self.camera.background_color = self.BG
        self.camera.frame.save_state()

        # ── QUESTIONS? label — lives for entire presentation ──
        q_label = self._q_label()
        self.add(q_label)

        # ── ValueTrackers ─────────────────────────────────────
        N_t     = ValueTracker(self.LOOP_START_N)
        M_t     = ValueTracker(self.LOOP_START_M)
        prime_t = ValueTracker(0.0)   # 0=all lines, 1=prime-only

        # ── always_redraw mobjects ────────────────────────────
        lines_mob = always_redraw(lambda: self._lines(
            int(round(N_t.get_value())),
            M_t.get_value(),
            prime_t.get_value(),
            PRIMES,
        ))
        dots_mob = always_redraw(lambda: self._dots(
            int(round(N_t.get_value())),
            PRIMES,
        ))
        math_lbl = always_redraw(lambda: self._math_label(
            int(round(N_t.get_value())),
            M_t.get_value(),
            prime_t.get_value(),
        ))

        # ════════════════════════════════════════════════════
        #  SLIDE 0 — INTRO  (one-shot fade-in, non-looping)
        # ════════════════════════════════════════════════════
        self.play(
            FadeIn(lines_mob, run_time=2.0),
            FadeIn(dots_mob,  run_time=2.0),
            FadeIn(math_lbl,  run_time=2.0),
            run_time=2.0,
        )
        self.wait(0.5)

        # ── Press → to enter the loop ────────────────────────
        self.next_slide()

        # ════════════════════════════════════════════════════
        #  SLIDE 1 — INFINITE LOOP  ← loop=True
        #  Everything between here and the next next_slide()
        #  will replay indefinitely in manim-slides presenter.
        # ════════════════════════════════════════════════════
        self.next_slide(loop=True)

        # ── Phase 1: Normal spiral ────────────────────────────
        for i in range(1, len(self.WAYPOINTS_NORMAL)):
            n_tgt, m_tgt = self.WAYPOINTS_NORMAL[i]
            # Alternate zoom: in on even indices, out on odd
            zoom_w = self.BASE_W * (1.0 - (1 if i % 2 == 0 else -1) * self.ZOOM_AMT)
            self.play(
                N_t.animate.set_value(float(n_tgt)),
                M_t.animate.set_value(float(m_tgt)),
                self.camera.frame.animate.set_width(zoom_w),
                run_time=self.SEG_NORMAL,
                rate_func=smooth,
            )

        # ── Phase 2: Prime filter fades in ───────────────────
        self.play(
            prime_t.animate.set_value(1.0),
            self.camera.frame.animate.set_width(self.BASE_W),
            run_time=self.CROSSFADE,
            rate_func=smooth,
        )

        for i in range(1, len(self.WAYPOINTS_PRIME)):
            n_tgt, m_tgt = self.WAYPOINTS_PRIME[i]
            zoom_w = self.BASE_W * (1.0 - (1 if i % 2 == 1 else -1) * self.ZOOM_AMT)
            self.play(
                N_t.animate.set_value(float(n_tgt)),
                M_t.animate.set_value(float(m_tgt)),
                self.camera.frame.animate.set_width(zoom_w),
                run_time=self.SEG_PRIME,
                rate_func=smooth,
            )

        # Restore zoom before Ulam
        self.play(
            self.camera.frame.animate.set_width(self.BASE_W),
            run_time=2.0,
            rate_func=smooth,
        )

        # ── Phase 3: Ulam spiral ──────────────────────────────
        ulam_grp  = self._ulam(PRIMES)
        ulam_note = Text(
            "Ulam Spiral  —  primes in gold",
            font="Rajdhani", font_size=20, color=self.GOLD_MID,
        ).to_corner(DR, buff=0.42)

        # Circle → Ulam crossfade
        self.play(
            FadeOut(lines_mob, run_time=self.ULAM_IN),
            FadeOut(dots_mob,  run_time=self.ULAM_IN),
            FadeOut(math_lbl,  run_time=self.ULAM_IN),
            FadeIn(ulam_grp,   run_time=self.ULAM_IN),
            FadeIn(ulam_note,  run_time=self.ULAM_IN),
            run_time=self.ULAM_IN,
            rate_func=smooth,
        )

        # Breathe in then out while holding Ulam
        half = self.ULAM_HOLD / 2
        self.play(
            self.camera.frame.animate.set_width(self.BASE_W * (1 - self.ZOOM_AMT)),
            run_time=half,
            rate_func=smooth,
        )
        self.play(
            self.camera.frame.animate.set_width(self.BASE_W * (1 + self.ZOOM_AMT * 0.5)),
            run_time=half,
            rate_func=smooth,
        )

        # Ulam → circle crossfade
        self.play(
            FadeOut(ulam_grp,  run_time=self.ULAM_OUT),
            FadeOut(ulam_note, run_time=self.ULAM_OUT),
            FadeIn(lines_mob,  run_time=self.ULAM_OUT),
            FadeIn(dots_mob,   run_time=self.ULAM_OUT),
            FadeIn(math_lbl,   run_time=self.ULAM_OUT),
            self.camera.frame.animate.set_width(self.BASE_W),
            run_time=self.ULAM_OUT,
            rate_func=smooth,
        )

        # ── Phase 4: Reset to loop-start state ───────────────
        # This must land on exactly LOOP_START_N / LOOP_START_M
        # so the restart of the loop is visually seamless.
        self.play(
            N_t.animate.set_value(self.LOOP_START_N),
            M_t.animate.set_value(self.LOOP_START_M),
            prime_t.animate.set_value(0.0),
            self.camera.frame.animate.set_width(self.BASE_W),
            run_time=self.SEG_NORMAL,
            rate_func=smooth,
        )

        # Brief hold so the loop-start frame is visible before replay
        self.wait(1.2)

        # ════════════════════════════════════════════════════
        #  SLIDE 2 — EXIT (press → to reach here and stop)
        # ════════════════════════════════════════════════════
        self.next_slide()

        self.play(
            FadeOut(lines_mob, run_time=1.5),
            FadeOut(dots_mob,  run_time=1.5),
            FadeOut(math_lbl,  run_time=1.5),
            FadeOut(q_label,   run_time=1.5),
            run_time=1.5,
        )
        self.wait(0.5)

    # ─────────────────────────────────────────────────────────
    #  BUILDER METHODS
    # ─────────────────────────────────────────────────────────

    def _lines(self, N, M, ps, PRIMES):
        """
        Connection lines k → Mk mod N.
        ps (prime_strength 0→1): blends all-lines → prime-only.
        """
        grp  = VGroup()
        N    = max(N, 3)
        step = max(1, N // self.NUM_LINES)

        for k in range(0, N, step):
            k2 = int(round(M * k)) % N
            if k2 == k:
                continue

            is_p = k in PRIMES
            t    = k / N
            base_col = interpolate_color(self.GOLD_DIM, self.GOLD_BRIGHT, t)
            base_op  = 0.12 + 0.55 * abs(np.sin(PI * t))

            if ps > 0.01:
                if is_p:
                    col = interpolate_color(base_col, self.PRIME_COLOR, ps)
                    op  = base_op + ps * (0.85 - base_op)
                    sw  = 0.7 + ps * 0.6
                else:
                    col = interpolate_color(base_col, self.COMP_COLOR, ps)
                    op  = base_op * (1.0 - ps * 0.95)
                    sw  = 0.7 * (1.0 - ps * 0.9)
            else:
                col = base_col
                op  = base_op
                sw  = 0.7

            if op < 0.01:
                continue

            a1 = 2 * PI * k  / N - PI / 2
            a2 = 2 * PI * k2 / N - PI / 2
            p1 = np.array([self.RADIUS * np.cos(a1), self.RADIUS * np.sin(a1), 0])
            p2 = np.array([self.RADIUS * np.cos(a2), self.RADIUS * np.sin(a2), 0])

            grp.add(Line(p1, p2,
                         stroke_width=sw, color=col, stroke_opacity=op))
        return grp

    def _dots(self, N, PRIMES):
        N   = max(N, 3)
        grp = VGroup()
        for k in range(N):
            ang  = 2 * PI * k / N - PI / 2
            is_p = k in PRIMES
            grp.add(Dot(
                point=[self.RADIUS * np.cos(ang), self.RADIUS * np.sin(ang), 0],
                radius=0.028 if is_p else 0.018,
                color=self.GOLD_BRIGHT if is_p else self.GOLD_MID,
                fill_opacity=0.75 if is_p else 0.40,
            ))
        return grp

    def _ulam(self, PRIMES):
        grp = VGroup()
        s   = self.ULAM_SCALE
        r   = self.ULAM_DOT_R
        for n in range(1, self.ULAM_N + 1):
            cx, cy = self._ulam_xy(n)
            is_p   = n in PRIMES
            grp.add(Dot(
                point=[cx * s, cy * s, 0],
                radius=r if is_p else r * 0.30,
                color=self.GOLD_BRIGHT if is_p else self.GOLD_DIM,
                fill_opacity=0.92 if is_p else 0.18,
            ))
        return grp

    def _q_label(self):
        lbl = Text(
            "QUESTIONS?",
            font="Cinzel",
            font_size=42,
            color=self.GOLD,
            weight=BOLD,
        ).to_edge(DOWN, buff=0.38)
        lbl.set_stroke(self.GOLD_BRIGHT, width=2, opacity=0.25)
        return lbl

    def _math_label(self, N, M, ps):
        s = (f"k prime  →  {int(round(M))}k mod {N}"
             if ps > 0.5
             else f"k  →  {int(round(M))}k mod {N}")
        return Text(
            s, font="Rajdhani", font_size=19, color=self.GOLD_MID,
        ).to_corner(DR, buff=0.42)