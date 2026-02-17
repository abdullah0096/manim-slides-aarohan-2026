from manim import *
from manim_slides import Slide

from cryptologySlide import *
from utils import *
from piryamid import *

DOTCOLOR = WHITE
def plotDotTL(s):
    dot = Dot(color=DOTCOLOR).to_corner(UL).scale(0.1)
    s.play(FadeIn(dot), run_time=0.1)
    s.play(FadeOut(dot), run_time=0.1)

class Title(Slide):
    def construct(self):
        # Create blue rounded rectangle banner
        banner = RoundedRectangle(
            width=12,
            height=2,
            corner_radius=0.2,
            fill_color=BLACK,  # Material blue
            fill_opacity=1,
            stroke_width=0
        )
        banner.shift(UP * 2)
        
        # Main title
        main_title = Tex("Modern Cryptography, ECDLP \& Quantum Computers", font_size=48, color=WHITE)
        main_title.move_to(banner.get_center() + UP * 0.2)
        self.play(FadeIn(banner))
        self.play(Write(main_title))
        self.next_slide()
        
        # Lecture subtitle
        subTitle = Text("If needed add something here", font_size=28, color=WHITE)
        subTitle.next_to(main_title, DOWN, buff=0.3)
        self.play(FadeIn(subTitle))
        
        # Author name
        author = Text("Dr. Abdullah Ansari", font_size=36, color=WHITE)
        author.next_to(banner, DOWN, buff=0.5)
        self.play(Write(author))
        self.next_slide()

        # # Department info
        dept1 = Text(
            "Aarohan 2026 - DES PU",
            font_size=22,
            color=WHITE
        )
        dept1.next_to(author, DOWN, buff=0.5)
        
        dept2 = Text(
            "24th February 2026",
            font_size=22,
            color=WHITE
        )
        dept2.next_to(dept1, DOWN, buff=0.15)
        
        university = Text(
            "Dept. of Scientific Computing, Modeling and Simulation - SPPU",
            font_size=18,
            color=WHITE
        )
        university.next_to(dept2, DOWN, buff=0.15)
        
        self.play(
            FadeIn(dept1),
            FadeIn(dept2),
            FadeIn(university)
        )
        self.next_slide()

# Aim : Setup the context of the talk by starting from a point already known the the audiance
#       i.e. using examples that are popular and relatable to the audiance. 
class Introduction(Slide):
    def construct(self):
        txt1 = Tex(r"\textbf{6,000,000,000+} \\ \textbf{Internet user}", color=BLUE).scale(1.6)
        txt2 = Tex(r"\textbf{20,000,000,000+} \\ \textbf{Connected devices}", color=YELLOW).scale(1.8)

        self.play(FadeIn(txt1))
        self.next_slide()

        # scale down txt1 and translate it up
        self.play(txt1.animate.scale(0.8).shift(UP*2), FadeIn(txt2))
        self.play(FadeOut(txt1))
        self.next_slide()

        self.play(txt2.animate.scale(0.8).shift(UP*2), FadeOut(txt2))
        img_yt = ImageMobject("images/yt_icon.png").scale_to_fit_width(2.5)
        self.play(FadeIn(img_yt))
        yt_text = Tex(r"2.7+ Billion", font_size=32).next_to(img_yt, DOWN)
        self.play(Write(yt_text))

        ytGrp = Group()
        ytGrp.add(img_yt, yt_text)
        self.play(ytGrp.animate.shift(LEFT*5))
        
        img_fb = ImageMobject("images/facebook.png").scale_to_fit_width(1.6)
        img_whatsApp = ImageMobject("images/WhatsApp.png").scale_to_fit_width(1.6).next_to(img_fb, RIGHT)
        img_insta = ImageMobject("images/Instagram_.webp").scale_to_fit_width(1.6).next_to(img_whatsApp, RIGHT)

        metaGrp = Group()
        metaGrp.add(img_whatsApp, img_insta, img_fb)
        self.play(FadeIn(metaGrp))

        #make a box around the metaGrp
        box = SurroundingRectangle(metaGrp, color=BLUE_A, buff=0.2)
        self.play(Create(box))
        meta_txt = Tex(r"3.9+ Billion", font_size=32).next_to(metaGrp, DOWN, buff=0.3)
        self.play(Write(meta_txt))
        self.play(FadeOut(box))

        self.next_slide()
        
        self.play(metaGrp.animate.shift(LEFT*2.4), meta_txt.animate.shift(LEFT*2))

        img_upi = ImageMobject("images/upi2.png").scale_to_fit_width(3.2)
        upi_text = Tex(r"500+ Million", font_size=32).next_to(img_upi, DOWN, buff=0.3)
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
        e2e_text = Tex(r"End to End Encryption", font_size=56, color=GREEN_D).next_to(img_whatsApp, DOWN, buff=0.3)
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
        # make Alice appear on the top left corner
        img_alice = ImageMobject("images/d.png").scale_to_fit_width(1).to_corner(UL).shift(LEFT * 0.3 + UP * 0.3)
        txt_alice = Tex(r"Alice", font_size=32, color=BLUE).next_to(img_alice, DOWN, buff=0.1)
        self.play(FadeIn(img_alice), FadeIn(txt_alice))   

        # make Bob appear on the bottom right corner
        img_bob = ImageMobject("images/d.png").scale_to_fit_width(1).to_corner(DR).shift(RIGHT * 0.3)
        txt_bob = Tex(r"Bob", font_size=32, color=BLUE).next_to(img_bob, DOWN, buff=0.1)
        self.play(FadeIn(img_bob), FadeIn(txt_bob))  

        # make whatsApp appear in the center of the screen called whatsapp_server with a bounding box around it
        img_whatsApp = ImageMobject("images/WhatsApp.png").scale_to_fit_width(1)
        txt_whatsApp = Tex(r"Server", font_size=32).next_to(img_whatsApp, DOWN, buff=0.1)
        whatsApp_grp = Group()
        whatsApp_grp.add(img_whatsApp, txt_whatsApp)
        box = SurroundingRectangle(whatsApp_grp, color=GREEN_D, buff=0.15)
        self.play(FadeIn(img_whatsApp), FadeIn(txt_whatsApp))
        self.play(Create(box))

        # connect Alice to a cell tower called alice_tower
        img_aliceTower = ImageMobject("images/cell_tower.png").scale_to_fit_width(1)
        img_aliceTower.to_edge(UP).shift(UP * 0.3)
        self.play(FadeIn(img_aliceTower)) 


        # connect whatapp_server to a ISP called bob_isp
        img_bobISP = ImageMobject("images/server.png").scale_to_fit_width(1).to_edge(DOWN)
        self.play(FadeIn(img_bobISP))

        # connect all of them
        line1 = Line(img_alice.get_right(), img_aliceTower.get_left()+0.1, color=TEAL)
        line2 = Line(img_aliceTower.get_bottom(), box.get_top(), color=TEAL)
        line3 = Line(box.get_bottom(), img_bobISP.get_top(), color=TEAL)
        line4 = Line(img_bobISP.get_right(), img_bob.get_left()-0.2, color=TEAL)

        # Create them normally
        self.play(Create(line1))
        self.play(Create(line2))
        self.play(Create(line3))
        self.play(Create(line4))

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
            self.add(label)

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
        txt_eve = Tex(r"Eve", font_size=32, color=RED).next_to(img_eve, DOWN, buff=0.1)
        self.play(FadeIn(img_eve), FadeIn(txt_eve))
        self.next_slide()

        # making line compromised
        line5 = Line(img_eve.get_left(), line2.get_center(), color=RED)
        self.play(Create(line5), run_time=1.5)
        
        mid = (img_aliceTower.get_bottom() + box.get_top())/2
        line6 = Line(mid, mid, color=RED)
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
            self.add(label)

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
            self.add(label)

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
        txt_hello = Tex("HELLO", font_size=28).next_to(img_alice, RIGHT, buff=0.2).shift(UP*0.3)
        self.play(FadeIn(txt_hello))
        self.next_slide()

        # Give and example of encryption using cesar cipher
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet_text = VGroup(*[Tex(l, font_size=32) for l in letters])
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
            h_rect = SurroundingRectangle(alphabet_text[src], buff=0.1, color=YELLOW, stroke_width=2)
            self.play(Create(h_rect))
            self.next_slide()

            r_rect = SurroundingRectangle(alphabet_text[dst], buff=0.1, color=RED, stroke_width=2)
            self.play(TransformFromCopy(h_rect, r_rect))
            self.next_slide()
            
            letter_copy = alphabet_text[dst].copy()
            self.play(letter_copy.animate.next_to(img_whatsApp, LEFT*offset), run_time=1.5)
            offset -= 1
            self.play(FadeOut(h_rect), FadeOut(r_rect))
            copied_letters.append(letter_copy)

        txt_khoor = Tex("KHOOR", font_size=28).next_to(img_alice, RIGHT, buff=0.2).shift(DOWN*0.3)
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

        txt_helloBob = Tex("HELLO", font_size=28).next_to(img_bob, LEFT, buff=0.2).shift(DOWN*0.4)
        self.play(TransformFromCopy(txt_khoor, txt_helloBob))
        self.remove(msg2)

        self.next_slide()
        # upi ping encryption demo
        self.play(FadeOut(img_whatsApp), FadeIn(img_upi), FadeOut(txt_khoor), FadeOut(txt_helloBob))
        pin.next_to(img_alice, RIGHT, buff=0.2).shift(UP*0.3)
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
        
        txt_pinBob = Tex("Pin : 1234", font_size=28).next_to(img_bob, LEFT, buff=0.2).shift(DOWN*0.4)
        self.play(TransformFromCopy(enc_pin, txt_pinBob))

# Aim : Defination of cryptography and old vs modern cryptography
class EncDec(Slide):
    def construct(self):
        txt1 = Tex(r'Hello').shift(UP*3)
        self.play(FadeIn(txt1))
        self.next_slide()

        rectangle = Rectangle(width=3, height=1, color=BLUE).next_to(
            txt1, DOWN, buff=1)
        self.play(Create(rectangle))

        # Create the text "Hello" and center it in the rectangle
        hello_text = Text("Scramble", font_size=18, color=WHITE)
        hello_text.move_to(rectangle)

        self.play(Write(hello_text))
        self.next_slide()

        txt2 = Tex(r'Khoor').next_to(rectangle, DOWN, buff=0.6)
        self.play(FadeIn(txt2, shift=DOWN*1.5), run_time=1)
        self.next_slide()

        rectangle2 = Rectangle(width=3, height=1, color=RED).next_to(
            txt2, DOWN, buff=1)
        self.play(Create(rectangle2))

        # Create the text "Hello" and center it in the rectangle
        unscramble_text = Text("Un-scramble", font_size=18, color=WHITE)
        unscramble_text.move_to(rectangle2)
        self.play(Write(unscramble_text))
        self.next_slide()

        txt3 = Tex(r'Hello').next_to(rectangle2, DOWN, buff=0.6)
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
        txt_defination1[0].set_color(BLUE)

        txt_defination = Tex(r'Crypto', r'graphy', font_size=56).next_to(txt_defination1, UP, buff=0.7)

        self.play(FadeIn(txt_defination1, shift=RIGHT), run_time=1)
        self.next_slide()

        self.play(FadeIn(txt_defination, shift=UP), run_time=1)
        self.next_slide()

        self.play(txt_defination[1].animate.shift(RIGHT * 0.2), txt_defination[0].animate.shift(LEFT * 0.2))
        self.next_slide()

        self.play(txt_defination[0].animate.set_color(RED), txt_defination[1].animate.set_color(YELLOW))

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
        self.next_slide()

        self.play(FadeOut(rectangle), FadeOut(
            rectangle2), FadeOut(unscramble_text))
        grp = VGroup()
        grp.add(hello_text, txtDec)
        txt4 = Tex(r'Old Vs Modern cryptography').shift(UP*3)
        transform3 = Transform(grp, txt4)
        self.play(transform3)
        self.next_slide()

        line = Line(start=2*UP, end=2.2*DOWN)
        line.set_stroke(width=2)  # Set th

        txt_3_1 = Text("Old cryptography", color=RED, font_size=28)
        txt_4_1 = Text("Modern cryptography", color=BLUE, font_size=28)

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
            "Vigenère Cipher",
            "Playfair Cipher",
            "Polybius Square",
            "etc..."
        ]

        items_2 = [
            "AES/ DSA / RSA / ECC ",
            "Digital signatures / Hashing",
            "Homomorphic encryption",
            "ZKP / Paring based",
            "Post-Quantum cryptography",
            "etc..."
        ]

        bullet = "• "
        bullet_color = RED_B

        generic_algos = [
            Tex(f"{bullet}{item}", color=bullet_color, font_size=28) for item in items_1]
        genericAlgo_list = VGroup(*generic_algos)
        genericAlgo_list.arrange(DOWN, aligned_edge=LEFT*2)
        genericAlgo_list.next_to(txt_3_1, DOWN*1.5)

        bullet_color_special = BLUE_B
        special_algos = [
            Tex(f"{bullet}{item}", color=bullet_color_special, font_size=28) for item in items_2]
        specialAlgo_list = VGroup(*special_algos)
        specialAlgo_list.arrange(DOWN, aligned_edge=LEFT*2)
        specialAlgo_list.next_to(txt_4_1, DOWN*1.5)
        specialAlgo_list.shift(0.7*RIGHT)

        self.play(Write(genericAlgo_list), run_time=2)
        self.play(Write(specialAlgo_list), run_time=1)

        self.next_slide()
        self.play(FadeOut(genericAlgo_list), run_time=1)

        genComplexity = Tex(r'Obsolete', font_size=96, color=RED_B)
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
        highlight = SurroundingRectangle(pk_node, color=YELLOW,
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

        ellipse1 = Ellipse(width=3, height=5, stroke_width=2, color=BLUE).scale(
            0.5).next_to(oneWayFun2, DOWN, buff=1).shift(LEFT*2)
        ellipse2 = Ellipse(width=3, height=5, stroke_width=2, color=RED).scale(
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
            start_point=ellipse2.get_center(), end_point=ellipse1.get_center(), color=YELLOW, stroke_width=2)
        curved_arrow2.tip_length = 4
        self.play(Create(curved_arrow2))
        hard = Tex(r'Hard', font_size=28, color=RED).next_to(curved_arrow2, UP)
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
                     color=GREEN).next_to(n, RIGHT)
        self.play(ScaleInPlace(n_easy, 1.4), run_time=3)
        self.wait(0.5)
        self.play(ShrinkToCenter(n_easy), run_time=2)
        self.next_slide()

        inv = Tex(r'\textbf{Given $n$, Find $p,q$ ?}', font_size=30).next_to(
            n, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(inv))
        inv_hard = Tex(r'\textbf{Hard}', font_size=25,
                       color=RED).next_to(inv, RIGHT)
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
                      color=BLUE).next_to(txt_n1_val, RIGHT)
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
        txt_3[1].set_color(BLUE)
        txt_3[3].set_color(YELLOW)

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

        self.play(ifp.animate.next_to(txt_3, DOWN, buff=0.8).set_color(YELLOW))
    
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

        l4 = Line(dot4, dot41, color=BLUE)
        l5 = Line(dot5, dot51, color=BLUE)
        self.play(FadeIn(l4), FadeIn(l5))

# Aim : Show ECDLP, Point addition, scalar multiplication
class ECDLP(Slide):
    def construct(self):
        ecdlp = Tex(r'\textbf{Elliptic Curve Discrete Logarithm Problem}').scale(0.9)
        self.play(Create(ecdlp))
        plotDotTL(self)
        self.next_slide()

        self.play(FadeOut(ecdlp))

        ec = Tex(r'Elliptic curves ')

        self.play(Create(ec))
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

        graph = VMobject(color=RED)
        graph.set_points_smoothly(plane.coords_to_point(
            ellipticCurvePoints))

        self.play(Create(graph), run_time=2.5)
        self.next_slide()

        grp = VGroup()
        grp.add(plane, graph)
        myRect = SurroundingRectangle(grp, color=BLUE)
        grp.add(myRect)
        self.play(grp.animate.scale(0.6).to_edge(LEFT))
        # self.play(equation2.animate.shift(LEFT))
        self.next_slide()

        Text_pointAdd = Text("Point addition", color=BLUE).next_to(
            equation2, DOWN).to_corner(
            RIGHT).scale(0.7).shift(LEFT*1.5)

        P = Dot(color=WHITE)
        P.move_to(graph.point_from_proportion(0.50))
        P_label = Tex("P", font_size=28).next_to(P, DL)

        Q = Dot(color=WHITE)
        Q.move_to(graph.point_from_proportion(0.45))
        Q_label = Text("Q", font_size=18).next_to(Q, LEFT)

        self.play(Create(P), Create(P_label), Create(Q), Create(Q_label))
        self.next_slide()

        self.play(Create(Text_pointAdd))
        self.next_slide()

        points_P_Q = Tex(
            r'$P = (x_p, y_p),    Q = (x_q, y_q$)', color=GREEN).next_to(Text_pointAdd, DOWN).scale(0.7)

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

        l = Line(P, Q, color=GREEN, stroke_width=3)
        self.play(Create(l))
        self.next_slide()

        R = Dot(color=WHITE)
        R.move_to(graph.point_from_proportion(0.25))
        R_label = Text("R'", font_size=18).next_to(R, LEFT)

        l2 = Line(Q, R, color=GREEN, stroke_width=3)
        self.play(Create(R), Create(R_label), Create(l2))
        self.next_slide()

        Q2 = Dot(color=WHITE)
        Q2.move_to(graph.point_from_proportion(0.75))

        l3 = Line(R, Q2, color=GREEN, stroke_width=3)

        self.play(Create(Q2), Create(l3))
        R2 = Text(f"({Q.get_center()[0]:.1f}, {Q.get_center()[1]:.1f})", font_size=18).next_to(
            Q2, LEFT)
        R2 = Text("R = P+Q", font_size=18).next_to(
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

        Text_pointDouble = Text("Point doubling", color=BLUE).next_to(
            Text_pointAdd, DOWN).to_corner(
            RIGHT).scale(0.7).shift(LEFT*1.3)

        self.play(Create(Text_pointDouble))
        self.next_slide()

        P = Dot(color=WHITE)
        P.move_to(graph.point_from_proportion(0.47))
        P_label = Text("P", font_size=18).next_to(P, UL)

        self.play(Create(P), Create(P_label))
        self.next_slide()

        tangentToCurve = TangentLine(graph, alpha=0.47, length=8, color=BLUE_D)

        self.play(Create(tangentToCurve))
        self.next_slide()

        Q = Dot(color=WHITE)
        Q.move_to(graph.point_from_proportion(0.29))
        Q_label = Text("Q", font_size=18).next_to(Q, UL)

        self.play(Create(Q), Create(Q_label))
        self.next_slide()

        R = Dot(color=WHITE)
        R.move_to(graph.point_from_proportion(0.71))
        R_label = Tex(r"$2P = P+P$").next_to(R,
                                             RIGHT).scale(.6).shift(LEFT*0.7)
        l3 = Line(Q, R, color=BLUE_D, stroke_width=3)

        self.play(Create(l3))
        self.play(Create(R), Create(R_label))
        self.next_slide()

        points_2P = Tex(
            r'$2P = P+P$').next_to(Text_pointDouble, DOWN, aligned_edge=DOWN).scale(0.8).shift(LEFT*0.7)

        self.play(Create(points_2P))
        self.next_slide()

        self.play(Unwrite(Q), Unwrite(Q_label), Unwrite(
            tangentToCurve, reverse=True), Unwrite(l3))

        l4 = Line(R, P, color=BLUE_D, stroke_width=3)
        self.play(Create(l4))
        self.next_slide()

        d1 = Dot(color=WHITE)
        d1.move_to(graph.point_from_proportion(0.567))
        self.play(Create(d1))
        self.next_slide()

        d2 = Dot(color=WHITE)
        d2.move_to(graph.point_from_proportion(0.4316))
        l5 = Line(d1, d2, color=BLUE_D, stroke_width=3)
        self.play(Uncreate(l4))
        self.play(Create(d2), Create(l5))
        self.next_slide()

        self.play(Uncreate(l5), Uncreate(d1))

        P3_lable = Tex(r"$3P = P+P+P$").next_to(d2,
                                                RIGHT).scale(0.6).shift(LEFT*0.5)
        P3 = Tex(r"$3P = P+P+P$").next_to(points_2P,
                                          DOWN, aligned_edge=DL, buff=0.5).scale(0.78).shift(LEFT*0.4)

        self.play(Create(P3_lable), Create(P3))
        self.next_slide()

        dot_dotDot_1 = Text('.').next_to(P3, DOWN)
        dot_dotDot_2 = Text('.').next_to(dot_dotDot_1, DOWN)
        dot_dotDot_3 = Text('.').next_to(
            dot_dotDot_2, DOWN)
        mP = Tex(r'$mP = P+P+P+...+P = Q$').next_to(dot_dotDot_3,
                                                    DOWN, aligned_edge=LEFT).scale(0.8).shift(LEFT*2)

        self.play(Create(dot_dotDot_1), Create(
            dot_dotDot_2), Create(dot_dotDot_3))
        self.play(Write(mP))
        plotDotTL(self)
        self.next_slide()

        question = Tex(r'Given $m$ and $P$ \\ Compute $Q = mP$ $\in$ $\mathcal{E}$', color=GREEN_C).next_to(
            mP, DOWN, buff=0.8).scale(0.8)
        self.play(Create(question))
        plotDotTL(self)

        self.next_slide()
        self.play(FadeOut(dot_dotDot_1), FadeOut(dot_dotDot_2), FadeOut(
            dot_dotDot_3), FadeOut(P3_lable), FadeOut(P3), FadeOut(points_2P))

        self.play(mP.animate.next_to(
            Text_pointDouble, DOWN, aligned_edge=LEFT), run_time=0.4)
        self.play(question.animate.next_to(mP, DOWN), run_time=0.3)

        txt_da = Tex(r'DOUBLE and ADD \\ Algorithm', font_size=43, color=BLUE_B).next_to(
            question, DOWN, buff=0.6)

        self.play(FadeIn(txt_da))

# Aim : Double and add algorithm for scalar multiplication, complexity of ECDLP
class DoubleAndAdd(Slide):
    def construct(self):

        mP = Tex(r'$mP = P+P+P+...+P$').scale(1.5)
        m = Tex(r'$mP$').scale(1.5)

        titleText = MarkupText(
            f'<span fgcolor="{BLUE}">DOUBLE</span> and <span fgcolor="{RED}">ADD</span> algorithm', color=WHITE)
        self.play(FadeIn(titleText))
        self.next_slide()

        self.play(titleText.animate.to_edge(UL).shift(LEFT*1.3).scale(0.7))
        mP.next_to(titleText, DOWN).scale(0.6)
        self.play(Create(mP))
        m.next_to(titleText, DOWN).scale(0.6).shift(LEFT*2.28)
        self.play(FadeIn(m))
        self.next_slide()

        # self.start_loop()  # Start loop
        my_rect = Rectangle(height=m.get_height()+0.3,
                            width=(m.get_width()+0.3), color=YELLOW)
        my_rect.surround(m)
        self.play(Create(my_rect), run_time=1.5)
        self.wait(0.3)
        self.play(FadeOut(my_rect))
        # self.end_loop()  # This will loop until user inputs a key

        m_bin = Tex(
            r'$ m$', color=GREEN_D).next_to(mP, DOWN, buff=0.6).scale(1).shift(LEFT*3.2)

        transformTo_m = Transform(m, m_bin)
        self.play(transformTo_m, run_time=1.3)
        m_bin2 = Tex(
            r'$= m_0 + 2m_1 + 2^2m_2 + ... +2^sm_s$', color=GREEN).next_to(m_bin, RIGHT).scale(0.8).shift(LEFT*0.8)
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
            r'$\blacktriangleright$ DOUBLE and ADD', color=BLUE).next_to(first_One, RIGHT).scale(0.7).shift(LEFT*0.8)
        txt_secondOne = Tex(
            r'$\blacktriangleright$ DOUBLE and ADD', color=BLUE).next_to(second_One, RIGHT).scale(0.7).shift(LEFT*0.8)

        txt_firstZero = Tex(
            r'$\blacktriangleright$ DOUBLE', color=RED).next_to(first_Zero, RIGHT).scale(0.7).shift(LEFT*0.32)
        txt_secondZero = Tex(
            r'$\blacktriangleright$ DOUBLE', color=RED).next_to(seond_Zero, RIGHT).scale(0.7).shift(LEFT*0.35)

        self.play(FadeIn(txt_firstOne, shift=RIGHT), run_time=1)
        self.wait(1)
        self.play(FadeIn(txt_firstZero, shift=RIGHT), run_time=1)
        self.play(FadeIn(txt_secondZero, shift=RIGHT), run_time=1)
        self.play(FadeIn(txt_secondOne, shift=RIGHT), run_time=1)

        self.next_slide()

        complexity = Tex(r"Complexity",
                         font_size=40, color=BLUE_A).shift(RIGHT*3).shift(UP)
        complexity2 = Tex(r"$O(log_2(m))$", font_size=66).next_to(
            complexity, DOWN, buff=0.3)

        self.play(FadeIn(complexity), FadeIn(complexity2))

        grp2 = VGroup()
        grp2.add(complexity2, complexity)
        myRect = SurroundingRectangle(grp2, color=YELLOW)
        grp2.add(myRect)

        self.play(Create(myRect), run_time=2)
        self.wait(0.3)
        self.play(FadeOut(myRect))

        # nextScenePause(self)

# Aim : Show ECDLP, inverse problem is hard
class ECDLP2(Slide):
    def construct(self):

        txt_1 = Tex(r'$mP = Q$')
        txt_2 = Tex(r'EASY !!!', color=GREEN).next_to(
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
                     color=BLUE).next_to(txt_4, DOWN, buff=1)
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
        txt_21 = Tex(r'Elliptic curve cryptography').shift(UL*3.5)
        self.play(FadeIn(txt_21), run_time=0.1)
        # self.next_slide()

        img_whatsApp = ImageMobject("images/WhatsApp.png").scale(0.7).shift(UP)
        txt_app1 = Tex(r'WhatsAPP \\ End to End \\ encryption',
                       color=GREEN_D).next_to(img_whatsApp, DOWN)

        self.play(FadeIn(img_whatsApp), FadeIn(txt_app1))
        # self.next_slide()

        self.play(txt_app1.animate.shift(LEFT*5),
                  img_whatsApp.animate.shift(LEFT*5))

        img_UPI = ImageMobject(
            "images/upi2.png").scale(0.7).shift(UP)
        txt_app2 = Tex(r'UPI \\ Google Pay \\ PhonePe',
                       color=BLUE_B).next_to(txt_app1, RIGHT, buff=1).next_to(img_UPI, DOWN)
        self.play(FadeIn(txt_app2), FadeIn(img_UPI))

        # self.next_slide()
        self.play(txt_app2.animate.shift(LEFT*1.7),
                  img_UPI.animate.shift(LEFT*1.7))

        img_bitEth = ImageMobject(
            "images/bitEth.png").scale(0.2).next_to(img_UPI, RIGHT, buff=0.8)
        txt_app3 = Tex(r'Crypto \\ Curriencies',
                       color=YELLOW_A).next_to(img_bitEth, DOWN)
        self.play(FadeIn(txt_app3), FadeIn(img_bitEth))

        # self.next_slide()

        txt_TLS = Tex(r"SSL/TLS").scale(1.3).next_to(img_bitEth,
                                                     RIGHT, buff=1)
        txt_Https = Tex(r'HTTPS \\ Email \\ etc...',
                        color=BLUE).next_to(txt_TLS, DOWN)
        self.play(FadeIn(txt_Https), FadeIn(txt_TLS))
        # self.next_slide()

        grp = Group()
        grp.add(img_whatsApp, txt_app1, img_UPI, txt_app2,
                img_bitEth, txt_app3, txt_TLS, txt_Https)
        self.play(grp.animate.shift(UP).scale(0.8))

        txt_ecdlp = Tex(
            r'Elliptic curve discrete logarithm problem').next_to(grp, DOWN, buff=1).scale(1.2)
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
        tri_outline = Polygon(left_base, right_base, apex_point, color=WHITE, stroke_width=4)

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
            color=BLUE,
            stroke_width=3,
        )
        mid_divider = Line(
            np.array([-mid_half, y_mid_div, 0]),
            np.array([mid_half, y_mid_div, 0]),
            color=BLUE,
            stroke_width=3,
        )

        wa_apex = ImageMobject("images/WhatsApp.png").scale(0.7)
        upi_apex = ImageMobject("images/upi2.png").scale(0.2)
        biteth_apex = ImageMobject("images/bitEth.png").scale(0.095)

        apps_top_row = Group(wa_apex).move_to(np.array([0, 2.2, 0]))
        apps_bottom_row = Group(upi_apex, biteth_apex).arrange(RIGHT, buff=0.18).move_to(np.array([0, 1.45, 0]))
        apps_icons = Group(apps_top_row, apps_bottom_row)

        txt_ecdlp_target = Tex(r'Elliptic curve discrete \\ logarithm problem').scale(0.86).move_to(np.array([0, -2.35, 0]))
        txt_21_target = Tex(r'Elliptic curve \\ cryptography').scale(1.0).move_to(np.array([0, -0.4, 0]))

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
class QuantumThreat(Slide):
    def construct(self):
        pass

    