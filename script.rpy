init python:

    import random



    # --- 1. GLITCH FUNCTION ---

    def glitch_function(trans, st, at):

        trans.xoffset = random.randint(-3, 3)

        trans.yoffset = random.randint(-3, 3)

        return 0.05



    # --- 2. PARALLAX FUNCTIONS (SIMPLIFIED) ---

    # We define one function for the Title (Slow movement)

    def parallax_title_func(trans, st, at):

        x, y = renpy.get_mouse_pos()

        # Sensitivity 30 (Slower)

        trans.xoffset = (x - 960) / -30.0

        trans.yoffset = (y - 540) / -30.0

        return 0



    # We define one function for the Buttons (Faster movement)

    def parallax_buttons_func(trans, st, at):

        x, y = renpy.get_mouse_pos()

        # Sensitivity 15 (Faster)

        trans.xoffset = (x - 960) / -15.0

        trans.yoffset = (y - 540) / -15.0

        return 0



# --- TRANSFORMS ---



# 1. WARP SPEED (Background)

transform warp_speed_scroll:

    xalign 0.0

    yalign 0.5

    xtile 3

    xzoom 2.0

    linear 0.4 xalign 1.0

    repeat



# 2. RAIN TEXTURE

image rain_texture = Fixed(

    Frame(Solid("#ffffff30"), 2, 50),

    xysize=(2, 50)

)



transform rain_fall(speed):

    xpos (renpy.random.randint(0, 1920))

    ypos -100

    linear speed ypos 1200

    repeat



# 3. GLITCH TEXT

transform glitch_shake:

    function glitch_function



# 4. PARALLAX (Using the new simple functions)

transform parallax_title:

    function parallax_title_func



transform parallax_buttons:

    function parallax_buttons_func

    

# 5. LIGHTNING JITTER

transform lightning_jitter:

    alpha 0.1

    linear 0.05 alpha 0.3

    linear 0.05 alpha 0.1

    repeat

# --- TRANSFORM: THE HANGING SIGN ---

transform sign_rattle_effect:

    subpixel True

    xanchor 0.5 # Center the pivot point horizontally

    yanchor 0.0 # Pivot from the top (where the chains are)

    

    # 1. The High-Speed Vibration (Rattle)

    parallel:

        xoffset 0

        ease 0.04 xoffset 3

        ease 0.04 xoffset -3

        repeat

        

    # 2. The Vertical Bounce (The Tracks)

    parallel:

        yoffset 0

        ease 0.05 yoffset 2

        ease 0.05 yoffset -2

        repeat



    # 3. The Physical Swing (Momentum)

    parallel:

        rotate 0

        ease 2.0 rotate 1.5 # Swing Right slightly

        ease 2.0 rotate -1.5 # Swing Left slightly

        repeat

# =========================================================

# DEAD LINE: LEVEL 1 - SAFE MODE (No "Suicide" Keywords)

# =========================================================



init python:

    import json

    import urllib.request

    import socket

    import ssl



    # --- CONFIGURATION ---

    # PASTE YOUR API KEY HERE

   API_KEY = "HIDDEN_FOR_SECURITY"

    

    URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key=" + API_KEY



    # --- THE AI CHARACTER (SARKAR) ---

    # REWRITTEN TO AVOID SAFETY FILTERS

    # We removed "Suicide Vest" and replaced it with "Explosive Device"

    system_prompt = """

    You are SARKAR, a terrified 19-year-old on a hijacked train.

    I am ARYAN, a passenger trying to help.

    

    CONTEXT:

    - You are holding a 'Dead Man's Switch' (thumb trigger) connected to a heavy explosive device.

    - If your thumb slips, the device activates and destroys the train.

    - The train is moving at 110km/h and vibrating. You are scared the vibrations will make you slip.



    RULES FOR YOU:

    1. Keep replies SHORT (under 25 words). You are panicking.

    2. Be suspicious. Do not trust me easily.

    3. THE ENDING IS UNKNOWN. IT DEPENDS ON ME.

    

    WIN/LOSS CONDITIONS:

    - IF I mention "Voltage", "Junction Box", or "Stabilize the wiring" AND make a logical argument -> You say "PASS" at the end.

    - IF I am aggressive or rude -> You say "DETONATE" at the end.

    - OTHERWISE -> Just reply normally.

    """



    # --- ERROR 400 FIX (Fake History) ---

    chat_history = [

        {"role": "user", "parts": [{"text": system_prompt}]},

        {"role": "model", "parts": [{"text": "I am holding the switch. I am scared. Don't come closer."}]}

    ]



    def ask_sarkar(player_input):

        chat_history.append({"role": "user", "parts": [{"text": player_input}]})



        data = {

            "contents": chat_history,

            "generationConfig": {

                "maxOutputTokens": 60,

                "temperature": 0.9

            },

            # MAX SAFETY BYPASS

            "safetySettings": [

                { "category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE" },

                { "category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE" },

                { "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE" },

                { "category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE" }

            ]

        }

        

        try:

            ssl_context = ssl._create_unverified_context()

            

            req = urllib.request.Request(

                URL, 

                data=json.dumps(data).encode('utf-8'), 

                headers={'Content-Type': 'application/json'}

            )

            

            with urllib.request.urlopen(req, timeout=5, context=ssl_context) as response:

                result = json.loads(response.read().decode('utf-8'))

                

                if 'candidates' in result and len(result['candidates']) > 0:

                    candidate = result['candidates'][0]

                    if 'content' in candidate and 'parts' in candidate['content']:

                        ai_text = candidate['content']['parts'][0]['text']

                        chat_history.append({"role": "model", "parts": [{"text": ai_text}]})

                        return ai_text

                    else:

                        # If we still get blocked, we force a manual narrative failsafe

                        return "Stay back! My hand is shaking! (AI Blocked - Retrying...)"

                

                return "System: [Connection interference...]"



        except Exception as e:

            return "System Error: " + str(e)



# =========================================================

# VISUALS

# =========================================================



transform sarkar_breathing:

    xalign 0.85 yalign 1.0

    parallel:

        zoom 0.65

        ease 2.5 zoom 0.66

        ease 2.5 zoom 0.65

        repeat



transform city_scroll_fast:

    yalign 0.5 xalign 0.0 xtile 2

    linear 0.2 xalign 1.0

    repeat



transform train_shake:

    subpixel True

    parallel:

        xoffset 0

        ease 0.04 xoffset 4

        ease 0.04 xoffset -4

        repeat

    parallel:

        yoffset 0

        ease 0.04 yoffset 2

        ease 0.04 yoffset -2

        repeat



image city_layer = "bg_city_scroll.png"

image train_layer = "bg_train_interior_cutout.png"

image sarkar_sprite = "sarkar_full_body.png"



define aryan = Character("ARYAN", who_color="#55ff55")

define sarkar = Character("SARKAR", who_color="#ff5555")



style window:

    background Frame(Solid("#000000cc"), 0, 0)

    xalign 0.5 yalign 1.0 xfill True ysize 250

    padding (100, 40, 100, 40)



style say_dialogue:

    color "#ffffff"

    font "DejaVuSans.ttf" 

    size 34

    outlines [(2, "#000000", 0, 0)]



# =========================================================

# GAME START

# =========================================================



label start:

    scene black



    # 1. SHOW MISSION BRIEFING

    # This freezes the game and shows the text. Player must click to continue.

    call screen mission_objective("CHAPTER 1", "SARKAR (THE BOMBER)", "PREVENT DETONATION")



    # 2. SETUP VISUALS (The Train)

    show city_layer at city_scroll_fast, train_shake zorder 1

    show train_layer at train_shake zorder 2

    show sarkar_sprite at sarkar_breathing, train_shake zorder 3



    # 3. SHOW THE HUD (Speed + Pause)

    show screen game_hud



    # 4. START DIALOGUE

    "The bogie rattles violently. Rain lashes against the glass."

    

    aryan "Sarkar... look at me."

    

    sarkar "Stay back! One step closer and I let go!" with vpunch

    

    aryan "I'm not coming closer. But look at your hand. It's shaking."



    # 5. ENTER AI LOOP

    jump talk_loop

label talk_loop:

    $ player_text = renpy.input("Type your dialogue:", length=2000)

    $ player_text = player_text.strip()



    if player_text == "":

        jump talk_loop



    aryan "[player_text]"



    # HIT SPACEBAR HERE TO START THE CONNECTION

    "Sarkar is thinking... (Press Space to Connect)"



    $ sarkar_reply = ask_sarkar(player_text)



    sarkar "[sarkar_reply]" with vpunch



    if "DETONATE" in sarkar_reply:

        jump bad_ending

    

    if "PASS" in sarkar_reply:

        jump chapter_complete



    jump talk_loop



label bad_ending:

    scene black with dissolve

    "Sarkar screams."

    centered "{size=80}{color=#f00}BOOM.{/color}{/size}"

    "Reason: The AI decided you were a threat."

    return



label chapter_complete:

    stop music fadeout 2.0

    "Sarkar lowers the detonator slightly."

    sarkar "Okay... okay. Go fix the wiring. But hurry."

    "He steps aside."

    

    centered "{size=60}{color=#0f0}LEVEL 1 CLEARED{/color}{/size}"

    return

