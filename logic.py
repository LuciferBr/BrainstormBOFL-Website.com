from pyscript import document
import random
from datetime import datetime
from js import document as js_doc, window

# Categorized inspirational responses
responses = {
    "climate": ["Inspiring action on climate change starts with telling stories that connect hearts to the planet. It's not just about statistics, but about showing how every small choice creates a ripple effect, reaching across oceans, and touching generations. Through empathy, education, and innovation, we can spark a movement where every person feels empowered to make an impact. Let’s transform awareness into action, and action into a global revolution of green."],
    "technology": ["Technology isn’t just the tool of progress—it’s the catalyst for transformation. From renewable energy innovations to blockchain for transparency in social causes, technology allows us to leap forward in ways we never imagined. It opens doors for global collaboration, turning problems into solutions."],
    "sustainability": ["True progress is not measured in GDP numbers, but in how we preserve the beauty of the world while building economies that work for all. Sustainability isn’t a barrier to growth; it’s the foundation."],
    "unity": ["The world is not a collection of isolated nations; it’s a web of interconnected lives. True transformation comes when we unite across borders, beyond differences."],
    "youth": ["The energy of youth is unmatched—it’s the fire that fuels revolutions, the voice that echoes across nations. They’re not waiting for change—they’re creating it."],
    "education": ["Education is the seed of global change. It’s the power to unlock potential, break down walls, and ignite minds with the understanding that the world can be different."],
    "equality": ["Social inequality is a deeply rooted system, but it’s one we can dismantle. True equality means recognizing our shared humanity and ensuring every voice is heard."],
    "collective": ["The most powerful tool is the collective will of a unified humanity. When we combine compassion with determination, we create a force capable of dismantling barriers."],
    "peace": ["Peace isn’t a mere absence of conflict; it’s a state of active harmony where differences are celebrated. It starts with small acts of kindness."],
    "local": ["Global change is built on local action. Every individual effort is a building block in the foundation of a transformed world."],
    "mental": [
        "No one cares. That's actually the advice - it frees you from worrying about others' judgments and lets you live authentically.",
        "Mental health is just as important as physical health. Don’t neglect it - nurturing your mind is key to a balanced, happy life.",
        "Take care of yourself first. You can't pour from an empty cup - self-care is the foundation for helping others effectively.",
        "It's okay to not be okay - accepting your struggles is the first step to healing and growing stronger."
    ]
}

# Keywords mapped to categories
keywords = {
    "climate": ["climate", "global warming", "environment"],
    "technology": ["technology", "innovation", "tech"],
    "sustainability": ["sustainability", "green", "renewable"],
    "unity": ["unity", "global", "together"],
    "youth": ["youth", "young", "future"],
    "education": ["education", "learning", "knowledge"],
    "equality": ["equality", "justice", "fairness"],
    "collective": ["collective", "together", "humanity"],
    "peace": ["peace", "harmony", "kindness"],
    "local": ["local", "community", "action"],
    "mental": ["mental health", "self-care", "judgment", "healing", "okay"]
}

# Flatten all responses for "all" category
all_responses = [resp for cat in responses.values() for resp in cat]

# Page switching
def switch_page(page_id):
    for section in document.querySelectorAll("section"):
        section.classList.remove("active")
    for btn in document.querySelectorAll("nav button"):
        btn.classList.remove("active")
    document.getElementById(page_id).classList.add("active")
    document.getElementById(f"{page_id}Btn").classList.add("active")

# Chat functions
def display_message(message, sender):
    chat_box = document.getElementById("chatBox")
    message_div = document.createElement("div")
    message_div.classList.add("message", sender)
    message_div.textContent = message
    chat_box.appendChild(message_div)
    chat_box.scrollTop = chat_box.scrollHeight

def get_response(user_input, category_filter):
    user_input = user_input.lower()
    if category_filter == "all":
        applicable_responses = all_responses
    else:
        applicable_responses = responses.get(category_filter, all_responses)
    for category, key_list in keywords.items():
        if any(key in user_input for key in key_list):
            if category_filter == "all" or category_filter == category:
                return random.choice(responses[category])
    return random.choice(applicable_responses) if applicable_responses else "Ask me about climate, equality, or mental health for inspiration!"

def send_message(event):
    user_input = document.getElementById("userInput").value.strip()
    if not user_input:
        return
    display_message(user_input, "user")
    document.getElementById("userInput").value = ""
    category_filter = document.getElementById("categoryFilter").value
    response = get_response(user_input, category_filter)
    display_message(response, "ai")

def clear_chat(event):
    document.getElementById("chatBox").innerHTML = ""

def save_chat(event):
    chat_box = document.getElementById("chatBox")
    chat_content = chat_box.textContent
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"brainstorm_chat_{timestamp}.txt"
    try:
        with open(filename, "w") as f:
            f.write(chat_content)
        display_message(f"Chat saved as {filename}", "ai")
    except:
        display_message("Save not supported in browser. Copy the chat manually!", "ai")

# Game functions
def display_game_output(output):
    game_area = document.getElementById("gameArea")
    output_div = document.createElement("div")
    output_div.classList.add("game-output")
    output_div.textContent = output
    game_area.appendChild(output_div)
    game_area.scrollTop = game_area.scrollHeight

def play_game(event):
    user_input = document.getElementById("gameInput").value.strip()
    if not user_input:
        return
    game_type = document.getElementById("gameSelect").value
    display_game_output(f"Your input: {user_input}")
    if game_type == "wordAssociation":
        words = user_input.split()
        response = f"Associated idea: {random.choice(words)} + {random.choice(['hope', 'action', 'nature', 'unity'])}"
    elif game_type == "ideaChain":
        response = f"Next in chain: {user_input} → {random.choice(['community', 'innovation', 'sustainability', 'peace'])}"
    elif game_type == "whatIf":
        response = f"What if {user_input} led to {random.choice(['global peace', 'clean energy', 'equal opportunities'])}?"
    display_game_output(response)
    document.getElementById("gameInput").value = ""

def clear_game(event):
    document.getElementById("gameArea").innerHTML = ""

# Theme toggle
saved_theme = window.localStorage.getItem("theme")
if saved_theme == "dark":
    document.querySelector("body").classList.add("dark-theme")
    document.getElementById("themeToggle").textContent = "Light Mode"
else:
    document.getElementById("themeToggle").textContent = "Dark Mode"

def toggle_theme(event):
    body = document.querySelector("body")
    body.classList.toggle("dark-theme")
    if "dark-theme" in body.classList:
        window.localStorage.setItem("theme", "dark")
        document.getElementById("themeToggle").textContent = "Light Mode"
    else:
        window.localStorage.setItem("theme", "light")
        document.getElementById("themeToggle").textContent = "Dark Mode"

# Bind navigation
document.getElementById("homeBtn").onclick = lambda e: switch_page("home")
document.getElementById("aboutBtn").onclick = lambda e: switch_page("about")
document.getElementById("igcBtn").onclick = lambda e: switch_page("igc")
document.getElementById("plansBtn").onclick = lambda e: switch_page("plans")
document.getElementById("gameBtn").onclick = lambda e: switch_page("game")
document.getElementById("themeToggle").onclick = toggle_theme

# Bind IGC chat controls
document.getElementById("sendButton").onclick = send_message
document.getElementById("clearChat").onclick = clear_chat
document.getElementById("saveChat").onclick = save_chat

# Bind game controls
document.getElementById("playGame").onclick = play_game
document.getElementById("clearGame").onclick = clear_game

# Enter key support
def on_chat_enter(event):
    if event.key == "Enter":
        send_message(event)
document.getElementById("userInput").onkeypress = on_chat_enter

def on_game_enter(event):
    if event.key == "Enter":
        play_game(event)
document.getElementById("gameInput").onkeypress = on_game_enter