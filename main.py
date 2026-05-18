import customtkinter as ctk
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


BG        = "#0A0E1A"      # deep navy
CARD      = "#111827"      # dark card
CARD2     = "#1a2235"      # slightly lighter card
ACCENT    = "#6C63FF"      # electric violet
ACCENT2   = "#00D4FF"      # electric cyan
GOLD      = "#FFD166"      # warm gold
SUCCESS   = "#06D6A0"      # mint green
TEXT      = "#E8EAF0"
MUTED     = "#5A6481"
BORDER    = "#1E2A45"

app = ctk.CTk()
app.geometry("1080x780")
app.title("AI Career Personality Scanner")
app.configure(fg_color=BG)
app.resizable(False, False)

data = pd.read_csv("career_data.csv")
X = data[["Analytical", "Creative", "Leadership", "Social", "Technical"]]
y = data["Career"]
model = DecisionTreeClassifier()
model.fit(X, y)

questions = [
    {"question": "Do you enjoy solving logical problems?",    "traits": {"Analytical": 2}, "icon": "🧠"},
    {"question": "Do you enjoy designing creative things?",   "traits": {"Creative": 2},   "icon": "🎨"},
    {"question": "Do you enjoy leading teams?",               "traits": {"Leadership": 2}, "icon": "🏆"},
    {"question": "Do you enjoy social interaction?",          "traits": {"Social": 2},     "icon": "🤝"},
    {"question": "Do you enjoy technology and coding?",       "traits": {"Technical": 2},  "icon": "💻"},
]

scores = {"Analytical": 0, "Creative": 0, "Leadership": 0, "Social": 0, "Technical": 0}
current_question = 0

def make_card(parent, **kwargs):
    defaults = dict(fg_color=CARD, corner_radius=20, border_width=1, border_color=BORDER)
    defaults.update(kwargs)
    return ctk.CTkFrame(parent, **defaults)

root_frame = ctk.CTkFrame(app, fg_color=BG)
root_frame.pack(fill="both", expand=True, padx=0, pady=0)

sidebar = ctk.CTkFrame(root_frame, fg_color=CARD, corner_radius=0, width=260)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

logo_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
logo_frame.pack(pady=(40, 20), padx=20)

logo_icon = ctk.CTkLabel(logo_frame, text="⚡", font=("Segoe UI Emoji", 40))
logo_icon.pack()

logo_title = ctk.CTkLabel(
    logo_frame,
    text="CareerAI",
    font=("Georgia", 26, "bold"),
    text_color=ACCENT2
)
logo_title.pack()

logo_sub = ctk.CTkLabel(
    logo_frame,
    text="Personality Scanner",
    font=("Georgia", 12),
    text_color=MUTED
)
logo_sub.pack()

# Divider
ctk.CTkFrame(sidebar, fg_color=BORDER, height=1).pack(fill="x", padx=20, pady=20)


trait_icons = {"Analytical": "🧠", "Creative": "🎨", "Leadership": "🏆", "Social": "🤝", "Technical": "💻"}
trait_labels_sidebar = {}

traits_header = ctk.CTkLabel(
    sidebar,
    text="TRAIT SCORES",
    font=("Courier New", 11, "bold"),
    text_color=MUTED
)
traits_header.pack(pady=(10, 12), padx=24, anchor="w")

for trait, icon in trait_icons.items():
    row = ctk.CTkFrame(sidebar, fg_color="transparent")
    row.pack(fill="x", padx=20, pady=4)

    ctk.CTkLabel(row, text=f"{icon} {trait}", font=("Segoe UI", 13), text_color=TEXT, width=140, anchor="w").pack(side="left")
    lbl = ctk.CTkLabel(row, text="0", font=("Courier New", 13, "bold"), text_color=ACCENT, width=30, anchor="e")
    lbl.pack(side="right")
    trait_labels_sidebar[trait] = lbl


ctk.CTkFrame(sidebar, fg_color=BORDER, height=1).pack(fill="x", padx=20, pady=20)

step_header = ctk.CTkLabel(sidebar, text="PROGRESS", font=("Courier New", 11, "bold"), text_color=MUTED)
step_header.pack(pady=(0, 10), padx=24, anchor="w")

step_dots = []
dots_row = ctk.CTkFrame(sidebar, fg_color="transparent")
dots_row.pack(padx=24, anchor="w")
for i in range(len(questions)):
    dot = ctk.CTkFrame(dots_row, fg_color=BORDER, width=14, height=14, corner_radius=7)
    dot.pack(side="left", padx=3)
    step_dots.append(dot)


ctk.CTkLabel(sidebar, text="v2.0 · AI Powered", font=("Courier New", 10), text_color=MUTED).pack(side="bottom", pady=20)

content = ctk.CTkFrame(root_frame, fg_color=BG)
content.pack(side="left", fill="both", expand=True, padx=30, pady=30)

header_row = ctk.CTkFrame(content, fg_color="transparent")
header_row.pack(fill="x", pady=(0, 24))

page_title_lbl = ctk.CTkLabel(
    header_row,
    text="Welcome",
    font=("Georgia", 28, "bold"),
    text_color=TEXT
)
page_title_lbl.pack(side="left")

badge = ctk.CTkLabel(
    header_row,
    text="  AI-Powered  ",
    font=("Courier New", 11, "bold"),
    text_color=ACCENT,
    fg_color=CARD2,
    corner_radius=10,
    padx=10,
    pady=4
)
badge.pack(side="right", pady=6)

start_card = make_card(content)
start_card.pack(fill="both", expand=True)

hero_frame = ctk.CTkFrame(start_card, fg_color="transparent")
hero_frame.pack(expand=True)

ctk.CTkLabel(hero_frame, text="🚀", font=("Segoe UI Emoji", 64)).pack(pady=(40, 10))

ctk.CTkLabel(
    hero_frame,
    text="Discover Your Ideal Career Path",
    font=("Georgia", 30, "bold"),
    text_color=TEXT
).pack(pady=(0, 8))

ctk.CTkLabel(
    hero_frame,
    text="Answer 5 personality questions.\nOur Decision Tree AI will analyse your traits\nand predict the career built for you.",
    font=("Segoe UI", 15),
    text_color=MUTED,
    justify="center"
).pack(pady=(0, 30))

pills_row = ctk.CTkFrame(hero_frame, fg_color="transparent")
pills_row.pack(pady=(0, 40))
for pill_text, pill_color in [("🧠 Trait Analysis", ACCENT), ("🤖 ML Prediction", ACCENT2), ("📊 Radar Chart", GOLD)]:
    pill = ctk.CTkLabel(
        pills_row,
        text=pill_text,
        font=("Segoe UI", 12, "bold"),
        text_color=pill_color,
        fg_color=CARD2,
        corner_radius=20,
        padx=14,
        pady=6
    )
    pill.pack(side="left", padx=8)

start_btn = ctk.CTkButton(
    hero_frame,
    text="Begin Assessment  →",
    command=lambda: start_test(),
    width=260,
    height=56,
    font=("Georgia", 17, "bold"),
    fg_color=ACCENT,
    hover_color="#5550DD",
    corner_radius=14,
    text_color="white"
)
start_btn.pack()
ctk.CTkLabel(hero_frame, text="Takes less than 2 minutes", font=("Segoe UI", 11), text_color=MUTED).pack(pady=8)

question_card = make_card(content)

q_inner = ctk.CTkFrame(question_card, fg_color="transparent")
q_inner.pack(expand=True, fill="both", padx=40, pady=30)

# Progress bar row
prog_row = ctk.CTkFrame(q_inner, fg_color="transparent")
prog_row.pack(fill="x", pady=(0, 20))

progress_label = ctk.CTkLabel(prog_row, text="Question 1 of 5", font=("Courier New", 12), text_color=MUTED)
progress_label.pack(side="left")

progress_bar = ctk.CTkProgressBar(prog_row, width=260, height=8, fg_color=BORDER, progress_color=ACCENT, corner_radius=4)
progress_bar.pack(side="right", pady=6)
progress_bar.set(0)

q_icon_lbl = ctk.CTkLabel(q_inner, text="", font=("Segoe UI Emoji", 48))
q_icon_lbl.pack(pady=(10, 8))

question_label = ctk.CTkLabel(
    q_inner,
    text="",
    font=("Georgia", 22, "bold"),
    text_color=TEXT,
    wraplength=560,
    justify="center"
)
question_label.pack(pady=(0, 30))

# Answer radio buttons as styled cards
answer_var = ctk.StringVar(value="")

def make_answer_btn(parent, text, value, emoji):
    card = ctk.CTkFrame(parent, fg_color=CARD2, corner_radius=12, border_width=2, border_color=BORDER)
    card.pack(fill="x", pady=6)
    inner = ctk.CTkFrame(card, fg_color="transparent")
    inner.pack(fill="x", padx=16, pady=10)
    ctk.CTkLabel(inner, text=emoji, font=("Segoe UI Emoji", 18)).pack(side="left", padx=(0, 10))
    rb = ctk.CTkRadioButton(
        inner,
        text=text,
        variable=answer_var,
        value=value,
        font=("Segoe UI", 14),
        fg_color=ACCENT,
        hover_color="#5550DD",
        text_color=TEXT,
        border_color=MUTED
    )
    rb.pack(side="left")
    return card, rb

answers_frame = ctk.CTkFrame(q_inner, fg_color="transparent")
answers_frame.pack(fill="x", padx=30)

make_answer_btn(answers_frame, "Yes, absolutely!", "yes", "✅")
make_answer_btn(answers_frame, "Sometimes / Partially", "sometimes", "🟡")
make_answer_btn(answers_frame, "Not really", "no", "❌")

next_btn = ctk.CTkButton(
    q_inner,
    text="Next Question  →",
    command=lambda: next_question(),
    width=220,
    height=50,
    font=("Georgia", 15, "bold"),
    fg_color=ACCENT,
    hover_color="#5550DD",
    corner_radius=12
)
next_btn.pack(pady=(24, 0))

result_card = make_card(content)

result_scroll = ctk.CTkScrollableFrame(result_card, fg_color="transparent")
result_scroll.pack(fill="both", expand=True, padx=30, pady=20)

res_career_lbl   = ctk.CTkLabel(result_scroll, text="", font=("Georgia", 32, "bold"), text_color=ACCENT2, justify="center", wraplength=560)
res_trait_lbl    = ctk.CTkLabel(result_scroll, text="", font=("Segoe UI", 16),        text_color=GOLD,    justify="center")
res_aura_lbl     = ctk.CTkLabel(result_scroll, text="", font=("Georgia", 14),         text_color=SUCCESS, justify="center")
res_scores_frame = ctk.CTkFrame(result_scroll, fg_color="transparent")
res_chart_btn    = ctk.CTkButton(
    result_scroll,
    text="📊  View Personality Radar Chart",
    command=lambda: show_chart(),
    width=300, height=50,
    font=("Georgia", 14, "bold"),
    fg_color=ACCENT2,
    hover_color="#00AACC",
    text_color=BG,
    corner_radius=12
)
res_restart_btn  = ctk.CTkButton(
    result_scroll,
    text="↩  Retake Assessment",
    command=lambda: restart(),
    width=200, height=44,
    font=("Segoe UI", 13),
    fg_color=CARD2,
    hover_color=BORDER,
    text_color=MUTED,
    corner_radius=12
)

def update_sidebar():
    for trait, lbl in trait_labels_sidebar.items():
        val = scores[trait]
        lbl.configure(text=str(val), text_color=ACCENT if val > 0 else MUTED)

def update_dots(current):
    for i, dot in enumerate(step_dots):
        if i < current:
            dot.configure(fg_color=SUCCESS)
        elif i == current:
            dot.configure(fg_color=ACCENT)
        else:
            dot.configure(fg_color=BORDER)

def load_question():
    q = questions[current_question]
    question_label.configure(text=q["question"])
    q_icon_lbl.configure(text=q["icon"])
    answer_var.set("")
    progress_label.configure(text=f"Question {current_question + 1} of {len(questions)}")
    progress_bar.set((current_question) / len(questions))
    update_dots(current_question)

def show_chart():
    labels = list(scores.keys())
    raw_values = list(scores.values())
    values = [(v / 2) * 100 for v in raw_values]
    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor("#0A0E1A")
    ax.set_facecolor("#111827")

    ax.plot(angles, values, linewidth=2.5, color="#6C63FF")
    ax.fill(angles, values, alpha=0.30, color="#6C63FF")

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=13, color="#E8EAF0")
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20%", "40%", "60%", "80%", "100%"], fontsize=9, color="#5A6481")
    ax.spines["polar"].set_color("#1E2A45")
    ax.grid(color="#1E2A45", linewidth=0.8)
    ax.tick_params(colors="#5A6481")

    plt.title("Personality Radar", size=18, color="#E8EAF0", pad=30)
    plt.tight_layout()
    plt.show()

def show_result():
    global current_question
    question_card.pack_forget()
    page_title_lbl.configure(text="Your Results")
    update_dots(len(questions))
    progress_bar.set(1.0)

    max_score = max(scores.values())
    total_score = sum(scores.values())
    
    if total_score < 2:   

    
        res_career_lbl.configure(text="Not enough data", text_color=GOLD)
        res_trait_lbl.configure(text="Please try again with more varied answers.")
        res_career_lbl.pack(pady=(30, 10))
        res_trait_lbl.pack()
        result_card.pack(fill="both", expand=True)
        return

    dominant_trait = max(scores, key=scores.get)
    user_input = pd.DataFrame([scores])
    predicted_career = model.predict(user_input)[0]

    
    auras = {
        "Analytical":  "The Rational Architect ⚙️",
        "Creative":    "The Visionary Creator 🌈",
        "Leadership":  "The Commanding Strategist 👑",
        "Social":      "The Empathetic Connector 🌿",
        "Technical":   "The Digital Pioneer 🛸",
    }
    aura = auras.get(dominant_trait, "Visionary Thinker ✨")

    
    ctk.CTkLabel(result_scroll, text="🎯", font=("Segoe UI Emoji", 52)).pack(pady=(20, 4))
    ctk.CTkLabel(result_scroll, text="AI Predicted Career", font=("Courier New", 13, "bold"), text_color=MUTED).pack()
    res_career_lbl.configure(text=predicted_career)
    res_career_lbl.pack(pady=(6, 4))

    res_trait_lbl.configure(text=f"Dominant Trait  ·  {trait_icons.get(dominant_trait, '⭐')} {dominant_trait}")
    res_trait_lbl.pack(pady=(0, 4))

    res_aura_lbl.configure(text=f"Career Aura  ·  {aura}")
    res_aura_lbl.pack(pady=(0, 20))

    
    ctk.CTkFrame(result_scroll, fg_color=BORDER, height=1).pack(fill="x", pady=10)
    ctk.CTkLabel(result_scroll, text="TRAIT BREAKDOWN", font=("Courier New", 11, "bold"), text_color=MUTED).pack(anchor="w", pady=(4, 10))

    res_scores_frame.pack(fill="x")
    bar_colors = {"Analytical": ACCENT, "Creative": "#FF6B9D", "Leadership": GOLD, "Social": SUCCESS, "Technical": ACCENT2}
    for trait, val in scores.items():
        row = ctk.CTkFrame(res_scores_frame, fg_color="transparent")
        row.pack(fill="x", pady=5)
        ctk.CTkLabel(row, text=f"{trait_icons[trait]} {trait}", font=("Segoe UI", 13), text_color=TEXT, width=130, anchor="w").pack(side="left")
        bar = ctk.CTkProgressBar(row, width=260, height=10, fg_color=BORDER, progress_color=bar_colors[trait], corner_radius=5)
        bar.pack(side="left", padx=10)
        bar.set(val / 2)
        ctk.CTkLabel(row, text=f"{val}/2", font=("Courier New", 12, "bold"), text_color=bar_colors[trait]).pack(side="left")

    ctk.CTkFrame(result_scroll, fg_color=BORDER, height=1).pack(fill="x", pady=16)
    res_chart_btn.pack(pady=(0, 10))
    res_restart_btn.pack(pady=(0, 20))

    result_card.pack(fill="both", expand=True)

def next_question():
    global current_question
    answer = answer_var.get()
    if answer == "yes":
        for trait, value in questions[current_question]["traits"].items():
            scores[trait] += value
    elif answer == "sometimes":
        for trait, value in questions[current_question]["traits"].items():
            scores[trait] += value / 2

    update_sidebar()
    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        question_card.pack_forget()
        show_result()

def start_test():
    start_card.pack_forget()
    page_title_lbl.configure(text="Assessment")
    question_card.pack(fill="both", expand=True)
    load_question()

def restart():
    global current_question, scores
    current_question = 0
    scores = {"Analytical": 0, "Creative": 0, "Leadership": 0, "Social": 0, "Technical": 0}
    update_sidebar()
    update_dots(-1)

    result_card.pack_forget()

    for w in result_scroll.winfo_children():
        try:
            if w not in (res_career_lbl, res_trait_lbl, res_aura_lbl, res_scores_frame, res_chart_btn, res_restart_btn):
                w.destroy()
        except Exception:
            pass
    for w in res_scores_frame.winfo_children():
        w.destroy()
    res_career_lbl.pack_forget()
    res_trait_lbl.pack_forget()
    res_aura_lbl.pack_forget()
    res_scores_frame.pack_forget()
    res_chart_btn.pack_forget()
    res_restart_btn.pack_forget()

    page_title_lbl.configure(text="Welcome")
    start_card.pack(fill="both", expand=True)

app.mainloop()