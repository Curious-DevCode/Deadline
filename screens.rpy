# =========================================================
# FINAL: THE "ROOF LOCKED" MENU
# =========================================================

# --- 1. ANIMATION DEFINITIONS ---

transform sign_rattle_huge_heavy:
    subpixel True
    # CRITICAL: We set the anchor HERE to ensure the rotation happens from the hooks
    xanchor 0.5 
    yanchor 0.0 
    
    # 1. Vibration
    parallel:
        xoffset 0
        ease 0.04 xoffset 2
        ease 0.04 xoffset -2
        repeat
    # 2. Sway (Slow & Heavy)
    parallel:
        rotate 0
        ease 5.0 rotate 1.5
        ease 5.0 rotate -1.5
        repeat

transform button_hover_shake:
    on idle:
        xoffset 0 yoffset 0
    on hover:
        function glitch_function

# --- 2. THE MENU SCREEN ---

screen main_menu():
    tag menu

    # --- BACKGROUND ---
    add "menu_bg2.png":
        xalign 0.5 yalign 0.5
        zoom 1.0 
    
    # Dark Vignette
    add Solid("#000000") alpha 0.6

    # --- RAIN ---
    add "rain_texture" at rain_fall(0.3) alpha 0.4
    add "rain_texture" at rain_fall(0.4) alpha 0.2

    # --- OPTIONS (LEFT SIDE) ---
    vbox:
        xpos 0.08       
        yalign 0.75      
        spacing 25

        textbutton "INITIATE SEQUENCE":
            action Start()
            at button_hover_shake
            text_font "DejaVuSans.ttf"
            text_size 70 
            text_color "#cccccc"
            text_hover_color "#ffffff"
            text_outlines [(4, "#000000", 0, 0)]

        textbutton "ACCESS MEMORY":
            action ShowMenu("load")
            at button_hover_shake
            text_font "DejaVuSans.ttf"
            text_size 50
            text_color "#888888"
            text_hover_color "#aaaaaa"
            text_outlines [(4, "#000000", 0, 0)]

        textbutton "TERMINATE":
            action Quit(confirm=False)
            at button_hover_shake
            text_font "DejaVuSans.ttf"
            text_size 50
            text_color "#888888"
            text_hover_color "#ff3333" 
            text_outlines [(4, "#000000", 0, 0)]
# =========================================================
# 1. THE IN-GAME HUD (Speed + Pause)
# =========================================================
screen game_hud():
    zorder 100 # Always on top of everything

    # --- SPEEDOMETER (Top Left) ---
    frame:
        background None
        xalign 0.02 
        yalign 0.02
        vbox:
            text "SPEED" size 20 color "#888888" font "DejaVuSans.ttf"
            text "110 KM/H" size 35 color "#ff3333" font "DejaVuSans.ttf" bold True outlines [(2, "#000", 0, 0)]

    # --- PAUSE BUTTON (Top Right) ---
    # We use a text button that looks like an icon "||"
    textbutton "||":
        xalign 0.98 
        yalign 0.02
        text_size 60
        text_color "#ffffff"
        text_hover_color "#ff3333"
        text_outlines [(2, "#000", 0, 0)]
        action ShowMenu("pause_menu") # Opens our custom menu

# =========================================================
# 2. THE CUSTOM PAUSE MENU
# =========================================================
screen pause_menu():
    tag menu      # Tells Ren'Py this is a menu
    modal True    # Blocks clicking the game behind it

    # Darken the background
    add Solid("#000000cc")

    vbox:
        xalign 0.5 
        yalign 0.5
        spacing 30

        text "GAME PAUSED" size 80 color "#ffffff" xalign 0.5 bold True font "DejaVuSans.ttf"

        textbutton "RESUME":
            action Return() # Go back to game
            text_size 50 text_color "#aaaaaa" text_hover_color "#ffffff" xalign 0.5 text_font "DejaVuSans.ttf"

        textbutton "MAIN MENU":
            action MainMenu()
            text_size 50 text_color "#aaaaaa" text_hover_color "#ffffff" xalign 0.5 text_font "DejaVuSans.ttf"

        textbutton "QUIT":
            action Quit()
            text_size 50 text_color "#aaaaaa" text_hover_color "#ff3333" xalign 0.5 text_font "DejaVuSans.ttf"

# =========================================================
# 3. THE MISSION OBJECTIVE (Cinematic Text)
# =========================================================
screen mission_objective(chapter_name, target, objective):
    modal True
    
    # Black background
    add Solid("#000000")
    
    vbox:
        xalign 0.5 
        yalign 0.5
        spacing 20
        
        # Animations: Text fades in one by one
        text "[chapter_name]" size 40 color "#888888" xalign 0.5 font "DejaVuSans.ttf":
            at objective_fade_in(0.5)
            
        text "TARGET: [target]" size 50 color "#ffffff" xalign 0.5 bold True font "DejaVuSans.ttf":
            at objective_fade_in(1.5)
            
        text "GOAL: [objective]" size 60 color "#ff3333" xalign 0.5 bold True font "DejaVuSans.ttf":
            at objective_fade_in(2.5)

    # Click to start prompt
    text "- CLICK TO START -" size 25 color "#555555" xalign 0.5 yalign 0.9 font "DejaVuSans.ttf":
        at objective_fade_in(4.0)
    
    # Clicking anywhere dismisses the screen
    key "dismiss" action Return()

# Animation Transform
transform objective_fade_in(delay_time):
    alpha 0.0
    pause delay_time
    linear 0.5 alpha 1.0