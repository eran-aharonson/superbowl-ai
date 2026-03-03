import streamlit as st
import time

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Super Bowl Ad Rater 🏈",
    page_icon="🏈",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Ads data
# ---------------------------------------------------------------------------
ADS = [
    {
        "id": "anthropic",
        "company": "Anthropic",
        "title": "The Thinking Machine",
        "description": "Claude takes center stage in a cinematic journey showing AI that truly understands you.",
        "icon": "🧠",
        "color": "#d97706",
    },
    {
        "id": "google",
        "company": "Google",
        "title": "Dear Sydney",
        "description": "Gemini helps a young fan write a heartfelt letter to her Olympic hero.",
        "icon": "🔍",
        "color": "#4285F4",
    },
    {
        "id": "openai",
        "company": "OpenAI",
        "title": "The Intelligence Age",
        "description": "A sweeping montage of human progress culminating in the dawn of ChatGPT.",
        "icon": "🤖",
        "color": "#10a37f",
    },
    {
        "id": "meta",
        "company": "Meta",
        "title": "The Real World",
        "description": "Ray-Ban Meta glasses blur the line between digital and physical in everyday life.",
        "icon": "🌐",
        "color": "#1877F2",
    },
]

EMOJI_OPTIONS = ["🔥", "😂", "😮", "❤️", "🏆"]

# ---------------------------------------------------------------------------
# Custom CSS – dark glassmorphism theme
# ---------------------------------------------------------------------------
st.markdown(
    """
<style>
/* ---------- global dark theme overrides ---------- */
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #1a1a2e 40%, #16213e 100%);
    color: #e0e0e0;
}

/* hide default streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}

/* ---------- glassmorphism card ---------- */
div[data-testid="stVerticalBlock"] .glass-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 28px 24px 20px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    margin-bottom: 8px;
}
div[data-testid="stVerticalBlock"] .glass-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.55);
}

.card-icon {
    font-size: 2.8rem;
    margin-bottom: 4px;
}
.card-company {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    opacity: 0.6;
    margin-bottom: 2px;
}
.card-title {
    font-size: 1.35rem;
    font-weight: 700;
    margin-bottom: 6px;
    color: #fff;
}
.card-desc {
    font-size: 0.92rem;
    line-height: 1.45;
    opacity: 0.78;
    margin-bottom: 14px;
}

/* ---------- star rating ---------- */
.star-row {
    display: flex;
    gap: 4px;
    margin-bottom: 10px;
}
.star-btn {
    font-size: 1.6rem;
    cursor: pointer;
    background: none;
    border: none;
    padding: 2px 3px;
    transition: transform 0.15s;
    filter: grayscale(0.8) brightness(0.6);
}
.star-btn.active {
    filter: none;
    transform: scale(1.15);
}
.star-btn:hover {
    transform: scale(1.25);
}

/* ---------- emoji reactions ---------- */
.emoji-row {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
    margin-bottom: 4px;
}
.emoji-chip {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 999px;
    padding: 4px 12px;
    font-size: 0.95rem;
    cursor: pointer;
    transition: background 0.2s, transform 0.15s;
    user-select: none;
}
.emoji-chip:hover {
    background: rgba(255,255,255,0.18);
    transform: scale(1.08);
}
.emoji-chip.selected {
    background: rgba(255,255,255,0.22);
    border-color: rgba(255,255,255,0.35);
    transform: scale(1.08);
}
.emoji-count {
    font-size: 0.78rem;
    opacity: 0.7;
    margin-left: 2px;
}

/* ---------- leaderboard ---------- */
.lb-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 28px 26px 22px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
}
.lb-title {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 18px;
    color: #fff;
}
.lb-row {
    display: flex;
    align-items: center;
    padding: 12px 14px;
    border-radius: 12px;
    margin-bottom: 8px;
    background: rgba(255,255,255,0.04);
    transition: background 0.2s;
}
.lb-row:hover {
    background: rgba(255,255,255,0.09);
}
.lb-rank {
    font-size: 1.3rem;
    font-weight: 800;
    width: 36px;
    text-align: center;
}
.lb-name {
    flex: 1;
    font-weight: 600;
    margin-left: 10px;
    color: #fff;
}
.lb-stars {
    margin-left: auto;
    font-size: 0.95rem;
}
.lb-avg {
    font-weight: 700;
    margin-left: 8px;
    min-width: 36px;
    text-align: right;
    color: #fbbf24;
}
.lb-votes {
    font-size: 0.78rem;
    opacity: 0.5;
    margin-left: 8px;
    min-width: 50px;
    text-align: right;
}

/* ---------- header ---------- */
.hero {
    text-align: center;
    padding: 30px 10px 10px;
}
.hero h1 {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #fbbf24, #f97316, #ef4444);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 4px;
}
.hero p {
    opacity: 0.6;
    font-size: 1.05rem;
}

/* ---------- submit button ---------- */
div.stButton > button {
    background: linear-gradient(135deg, #f97316, #ef4444) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 14px 36px !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    cursor: pointer !important;
    transition: transform 0.2s, box-shadow 0.2s !important;
    width: 100% !important;
    margin-top: 10px !important;
}
div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 24px rgba(249,115,22,0.45) !important;
}
div.stButton > button:active {
    transform: scale(0.97) !important;
}

/* ---------- vote counter badge ---------- */
.vote-badge {
    display: inline-block;
    background: rgba(251,191,36,0.15);
    color: #fbbf24;
    border-radius: 999px;
    padding: 4px 14px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-top: 2px;
}

/* ---------- confetti canvas ---------- */
.confetti-canvas {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    pointer-events: none;
    z-index: 9999;
}

/* ---------- responsive ---------- */
@media (max-width: 768px) {
    .hero h1 { font-size: 1.7rem; }
    .glass-card { padding: 18px 14px 14px; }
    .card-title { font-size: 1.1rem; }
    .lb-card { padding: 18px 14px 14px; }
}

/* Streamlit overrides for dark theme */
.stSelectbox label, .stRadio label, .stSlider label {
    color: #e0e0e0 !important;
}
div[data-baseweb="select"] {
    background: rgba(255,255,255,0.06) !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Confetti JS (injected once, triggered by function call)
# ---------------------------------------------------------------------------
CONFETTI_JS = """
<canvas id="confetti-canvas" class="confetti-canvas"></canvas>
<script>
(function(){
    const canvas = document.getElementById('confetti-canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const pieces = [];
    const colors = ['#fbbf24','#f97316','#ef4444','#10b981','#3b82f6','#8b5cf6','#ec4899'];
    for(let i=0;i<200;i++){
        pieces.push({
            x: Math.random()*canvas.width,
            y: Math.random()*canvas.height - canvas.height,
            w: Math.random()*10+5,
            h: Math.random()*6+3,
            color: colors[Math.floor(Math.random()*colors.length)],
            vy: Math.random()*4+2,
            vx: (Math.random()-0.5)*3,
            rot: Math.random()*360,
            vr: (Math.random()-0.5)*8
        });
    }
    let frame=0;
    function draw(){
        ctx.clearRect(0,0,canvas.width,canvas.height);
        pieces.forEach(p=>{
            ctx.save();
            ctx.translate(p.x,p.y);
            ctx.rotate(p.rot*Math.PI/180);
            ctx.fillStyle=p.color;
            ctx.fillRect(-p.w/2,-p.h/2,p.w,p.h);
            ctx.restore();
            p.y+=p.vy;
            p.x+=p.vx;
            p.rot+=p.vr;
            p.vy+=0.05;
        });
        frame++;
        if(frame<180) requestAnimationFrame(draw);
        else { ctx.clearRect(0,0,canvas.width,canvas.height); canvas.remove(); }
    }
    draw();
})();
</script>
"""

# ---------------------------------------------------------------------------
# Session state initialisation
# ---------------------------------------------------------------------------
if "votes" not in st.session_state:
    # votes: { ad_id: [list of ratings] }
    st.session_state.votes = {ad["id"]: [] for ad in ADS}

if "emojis" not in st.session_state:
    # emojis: { ad_id: { emoji: count } }
    st.session_state.emojis = {
        ad["id"]: {e: 0 for e in EMOJI_OPTIONS} for ad in ADS
    }

if "current_ratings" not in st.session_state:
    st.session_state.current_ratings = {ad["id"]: 0 for ad in ADS}

if "current_emojis" not in st.session_state:
    st.session_state.current_emojis = {ad["id"]: set() for ad in ADS}

if "show_confetti" not in st.session_state:
    st.session_state.show_confetti = False

if "total_submissions" not in st.session_state:
    st.session_state.total_submissions = 0


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def avg_rating(ad_id: str) -> float:
    v = st.session_state.votes[ad_id]
    return sum(v) / len(v) if v else 0.0


def star_display(rating: float) -> str:
    full = int(rating)
    half = rating - full >= 0.5
    stars = "★" * full + ("½" if half else "") + "☆" * (5 - full - (1 if half else 0))
    return stars


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    """
<div class="hero">
    <h1>🏈 Super Bowl Ad Rater</h1>
    <p>Rate the biggest AI ads of the game — who won the Super Bowl of AI?</p>
</div>
""",
    unsafe_allow_html=True,
)

# Show confetti if just submitted
if st.session_state.show_confetti:
    st.markdown(CONFETTI_JS, unsafe_allow_html=True)
    st.session_state.show_confetti = False

# ---------------------------------------------------------------------------
# Layout: Cards (left) + Leaderboard (right)
# ---------------------------------------------------------------------------
col_cards, col_lb = st.columns([3, 2], gap="large")

# ---------------------------------------------------------------------------
# Ad cards
# ---------------------------------------------------------------------------
with col_cards:
    card_cols = st.columns(2)
    for idx, ad in enumerate(ADS):
        with card_cols[idx % 2]:
            # --- Star rating via selectbox mapped to stars ---
            rating_key = f"star_{ad['id']}"

            st.markdown(
                f"""
<div class="glass-card">
    <div class="card-icon">{ad['icon']}</div>
    <div class="card-company">{ad['company']}</div>
    <div class="card-title">{ad['title']}</div>
    <div class="card-desc">{ad['description']}</div>
</div>
""",
                unsafe_allow_html=True,
            )

            # Star rating
            star_val = st.select_slider(
                f"Rate {ad['company']}",
                options=[0, 1, 2, 3, 4, 5],
                format_func=lambda x: "☆☆☆☆☆" if x == 0 else "★" * x + "☆" * (5 - x),
                value=st.session_state.current_ratings[ad["id"]],
                key=rating_key,
            )
            st.session_state.current_ratings[ad["id"]] = star_val

            # Emoji reactions
            emoji_cols = st.columns(len(EMOJI_OPTIONS))
            for ei, emoji in enumerate(EMOJI_OPTIONS):
                with emoji_cols[ei]:
                    count = st.session_state.emojis[ad["id"]][emoji]
                    is_selected = emoji in st.session_state.current_emojis[ad["id"]]
                    label = f"{emoji} {count}" if count else emoji
                    if st.button(
                        label,
                        key=f"emoji_{ad['id']}_{ei}",
                        use_container_width=True,
                    ):
                        if is_selected:
                            st.session_state.current_emojis[ad["id"]].discard(emoji)
                            st.session_state.emojis[ad["id"]][emoji] = max(0, count - 1)
                        else:
                            st.session_state.current_emojis[ad["id"]].add(emoji)
                            st.session_state.emojis[ad["id"]][emoji] = count + 1
                        st.rerun()

            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Leaderboard
# ---------------------------------------------------------------------------
with col_lb:
    # Leaderboard
    sorted_ads = sorted(ADS, key=lambda a: avg_rating(a["id"]), reverse=True)
    rank_medals = ["🥇", "🥈", "🥉", "4️⃣"]

    lb_rows = ""
    for rank, ad in enumerate(sorted_ads):
        avg = avg_rating(ad["id"])
        vote_count = len(st.session_state.votes[ad["id"]])
        stars_str = star_display(avg) if avg > 0 else "—"
        avg_str = f"{avg:.1f}" if avg > 0 else "—"
        votes_str = f"{vote_count} vote{'s' if vote_count != 1 else ''}" if vote_count else "no votes"

        lb_rows += f"""
        <div class="lb-row">
            <div class="lb-rank">{rank_medals[rank]}</div>
            <div class="lb-name">{ad['icon']} {ad['company']}</div>
            <div class="lb-stars">{stars_str}</div>
            <div class="lb-avg">{avg_str}</div>
            <div class="lb-votes">{votes_str}</div>
        </div>
        """

    st.markdown(
        f"""
<div class="lb-card">
    <div class="lb-title">🏆 Live Leaderboard</div>
    {lb_rows}
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    # Total votes badge
    if st.session_state.total_submissions:
        st.markdown(
            f'<div style="text-align:center"><span class="vote-badge">🗳️ {st.session_state.total_submissions} total submission{"s" if st.session_state.total_submissions != 1 else ""}</span></div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

    # Submit button
    has_any_rating = any(v > 0 for v in st.session_state.current_ratings.values())

    if st.button("🏈  Submit Your Vote!", use_container_width=True, disabled=not has_any_rating):
        for ad in ADS:
            r = st.session_state.current_ratings[ad["id"]]
            if r > 0:
                st.session_state.votes[ad["id"]].append(r)
        st.session_state.current_ratings = {ad["id"]: 0 for ad in ADS}
        st.session_state.current_emojis = {ad["id"]: set() for ad in ADS}
        st.session_state.total_submissions += 1
        st.session_state.show_confetti = True
        st.rerun()

    if not has_any_rating:
        st.markdown(
            '<p style="text-align:center;opacity:0.45;font-size:0.85rem;margin-top:6px;">Rate at least one ad to submit</p>',
            unsafe_allow_html=True,
        )
