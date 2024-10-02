from manim import *

class BootProcessIntro(Scene):
    def construct(self):
        # Title of the animation
        title = Text("Boot Process Introduction", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Step 1: Boot Process Overview
        boot_overview = Text("Boot Process Steps", font_size=36)
        self.play(Write(boot_overview))
        self.wait(1)
        self.play(FadeOut(boot_overview))

        # Boot process steps
        steps = VGroup(
            Text("1. Power On", font_size=28),
            Text("2. BIOS/UEFI Initialization", font_size=28),
            Text("3. Bootloader Execution", font_size=28),
            Text("4. OS Kernel Load", font_size=28),
            Text("5. User Space Initialization", font_size=28),
        )
        steps.arrange(DOWN, buff=0.5)
        self.play(FadeIn(steps))
        self.wait(3)
        self.play(FadeOut(steps))

        # Section 2: Introduction of projects
        intro_text = VGroup(
            Text("Introduction to:", font_size=36),
            Text("Linux Kernel", font_size=36, color=GREEN),
            Text("Coreboot", font_size=36, color=ORANGE),
            Text("KolibriOS", font_size=36, color=BLUE),
        )
        intro_text.arrange(DOWN, buff=0.7)
        self.play(FadeIn(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Step 3: Explanation of each project and its role in the boot process

        # Linux Kernel explanation
        linux_text = VGroup(
            Text("Linux Kernel", font_size=36, color=GREEN),
            Text("Handles system calls,", font_size=28),
            Text("process management,", font_size=28),
            Text("and hardware interaction.", font_size=28)
        )
        linux_text.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(linux_text))
        self.wait(3)
        self.play(FadeOut(linux_text))

        # Coreboot explanation
        coreboot_text = VGroup(
            Text("Coreboot", font_size=36, color=ORANGE),
            Text("Open-source firmware,", font_size=28),
            Text("designed for fast booting,", font_size=28),
            Text("with minimal overhead.", font_size=28),
            Text("Executes in Step 2.", font_size=28)
        )
        coreboot_text.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(coreboot_text))
        self.wait(3)
        self.play(FadeOut(coreboot_text))

        # KolibriOS explanation
        kolibri_text = VGroup(
            Text("KolibriOS", font_size=36, color=BLUE),
            Text("A lightweight, fast,", font_size=28),
            Text("and open-source OS.", font_size=28),
            Text("Executes in Step 4.", font_size=28)
        )
        kolibri_text.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(kolibri_text))
        self.wait(3)
        self.play(FadeOut(kolibri_text))

        # End of the animation
        end_text = Text("Thank you for watching!", font_size=48)
        self.play(FadeIn(end_text))
        self.wait(2)
        self.play(FadeOut(end_text))
