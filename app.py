import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Super Bowl LX Ad Rater 🏈",
    page_icon="🏈",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Super Bowl LX (2026) AI Ads – real data with YouTube URLs
# ---------------------------------------------------------------------------
ADS = [
    {
        "id": "anthropic",
        "company": "Anthropic (Claude)",
        "title": "A Time and a Place",
        "description": "Humorous spots where AI chatbots interrupt helpful conversations with intrusive ads — driving home: 'Ads are coming to AI. But not to Claude.'",
        "icon": "🧠",
        "youtube": "https://www.youtube.com/watch?v=kQRu7DdTTVA",
    },
    {
        "id": "openai",
        "company": "OpenAI (Codex)",
        "title": "You Can Just Build Things",
        "description": "A 60-second journey tracing human creation from a child's notebook through early coding to building alongside ChatGPT/Codex.",
        "icon": "🤖",
        "youtube": "https://www.youtube.com/watch?v=aCN9iCXNJqQ",
    },
    {
        "id": "google",
        "company": "Google (Gemini)",
        "title": "New Home",
        "description": "A mom eases her son's moving anxiety by using Gemini to visualize his new room painted blue, filled with toys, and the garden transformed.",
        "icon": "🔍",
        "youtube": "https://www.youtube.com/watch?v=Z1yGy9fELtE",
    },
    {
        "id": "meta",
        "company": "Meta (Oakley)",
        "title": "Athletic Intelligence Is Here",
        "description": "Marshawn Lynch, Spike Lee, IShowSpeed, and Olympic athletes use Oakley Meta AI glasses hands-free for video, AI queries, and audio streaming.",
        "icon": "🌐",
        "youtube": "https://www.youtube.com/watch?v=NerlyGrv7WM",
    },
    {
        "id": "amazon",
        "company": "Amazon (Alexa+)",
        "title": "Scary Good",
        "description": "Chris Hemsworth spirals into paranoia that the new AI-powered Alexa+ is plotting against him — set to INXS's 'Devil Inside.'",
        "icon": "📦",
        "youtube": "https://www.youtube.com/watch?v=sCyiXmxHqSg",
    },
    {
        "id": "genspark",
        "company": "Genspark",
        "title": "You Take Monday Off!",
        "description": "Matthew Broderick channels Ferris Bueller, showing how Genspark can autopilot tedious tasks so workers can take the Monday after the Super Bowl off.",
        "icon": "✨",
        "youtube": "https://www.youtube.com/watch?v=aJUuJtGgkQg",
    },
    {
        "id": "base44",
        "company": "Base44",
        "title": "It's App to You",
        "description": "In an Office-style setting, employee Nina discovers she just built a budgeting app with Base44, sparking a wave of app-building creativity among coworkers.",
        "icon": "🚀",
        "youtube": "https://www.youtube.com/watch?v=JcMPf4sEzew",
    },
]

# ---------------------------------------------------------------------------
# Custom CSS – dark glassmorphism theme
# ---------------------------------------------------------------------------
st.markdown(
    """
<style>
/* ---------- global dark theme ---------- */
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #1a1a2e 40%, #16213e 100%);
    color: #e0e0e0;
}
#MainMenu, footer, header {visibility: hidden;}

/* ---------- glassmorphism card ---------- */
.glass-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 24px 22px 18px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    margin-bottom: 6px;
}
.glass-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.55);
}
.card-icon { font-size: 2.4rem; margin-bottom: 2px; }
.card-company {
    font-size: 0.8rem; text-transform: uppercase;
    letter-spacing: 2px; opacity: 0.6; margin-bottom: 2px;
}
.card-title {
    font-size: 1.2rem; font-weight: 700;
    margin-bottom: 4px; color: #fff;
}
.card-desc {
    font-size: 0.88rem; line-height: 1.4;
    opacity: 0.78; margin-bottom: 0;
}

/* ---------- video container ---------- */
.video-wrapper {
    position: relative; padding-bottom: 56.25%;
    height: 0; overflow: hidden;
    border-radius: 14px; margin-bottom: 10px;
}
.video-wrapper iframe {
    position: absolute; top: 0; left: 0;
    width: 100%; height: 100%;
    border: none; border-radius: 14px;
}

/* ---------- star rating (HTML/JS clickable) ---------- */
.star-rating {
    display: flex;
    gap: 2px;
    margin: 6px 0 12px 0;
}
.star-rating .star {
    font-size: 1.3rem;
    cursor: pointer;
    transition: transform 0.12s;
    user-select: none;
    color: #555;
}
.star-rating .star.active {
    color: #fbbf24;
}
.star-rating .star:hover {
    transform: scale(1.25);
}

/* ---------- leaderboard ---------- */
.lb-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 24px 22px 18px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
}
.lb-title {
    font-size: 1.25rem; font-weight: 700;
    margin-bottom: 14px; color: #fff;
}
.lb-row {
    display: flex; align-items: center;
    padding: 10px 12px; border-radius: 12px;
    margin-bottom: 6px;
    background: rgba(255,255,255,0.04);
    transition: background 0.2s, transform 0.2s;
}
.lb-row:hover { background: rgba(255,255,255,0.09); transform: translateX(4px); }
.lb-row.gold   { background: rgba(251,191,36,0.12); border: 1px solid rgba(251,191,36,0.25); }
.lb-row.silver { background: rgba(192,192,192,0.08); border: 1px solid rgba(192,192,192,0.18); }
.lb-row.bronze { background: rgba(205,127,50,0.08); border: 1px solid rgba(205,127,50,0.18); }
.lb-rank {
    font-size: 1.2rem; font-weight: 800;
    width: 32px; text-align: center; flex-shrink: 0;
}
.lb-icon {
    font-size: 1.1rem; margin-left: 6px; flex-shrink: 0;
}
.lb-name {
    flex: 1; font-weight: 600;
    margin-left: 8px; color: #fff;
    font-size: 0.88rem; white-space: nowrap;
    overflow: hidden; text-overflow: ellipsis;
}
.lb-stars {
    margin-left: auto; font-size: 0.85rem;
    letter-spacing: 1px; flex-shrink: 0;
    color: #fbbf24;
}
.lb-avg {
    font-weight: 700; margin-left: 10px;
    min-width: 32px; text-align: right;
    color: #fbbf24; font-size: 0.95rem;
    flex-shrink: 0;
}
.lb-votes {
    font-size: 0.72rem; opacity: 0.5;
    margin-left: 6px; min-width: 50px;
    text-align: right; flex-shrink: 0;
}

/* ---------- header ---------- */
.hero { text-align: center; padding: 24px 10px 8px; }
.hero h1 {
    font-size: 2.6rem; font-weight: 800;
    background: linear-gradient(90deg, #fbbf24, #f97316, #ef4444);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 4px;
}
.hero p { opacity: 0.6; font-size: 1.05rem; }

/* ---------- submit button ---------- */
div.stButton > button[kind="primary"],
div.stButton > button[data-testid="stBaseButton-primary"] {
    background: linear-gradient(135deg, #f97316, #ef4444) !important;
    color: #fff !important; border: none !important;
    border-radius: 14px !important;
    padding: 14px 36px !important;
    font-size: 1.1rem !important; font-weight: 700 !important;
    letter-spacing: 0.5px !important; cursor: pointer !important;
    transition: transform 0.2s, box-shadow 0.2s !important;
    width: 100% !important; margin-top: 10px !important;
}
div.stButton > button[kind="primary"]:hover,
div.stButton > button[data-testid="stBaseButton-primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 24px rgba(249,115,22,0.45) !important;
}
div.stButton > button[kind="primary"]:active,
div.stButton > button[data-testid="stBaseButton-primary"]:active {
    transform: scale(0.97) !important;
}

.vote-badge {
    display: inline-block;
    background: rgba(251,191,36,0.15); color: #fbbf24;
    border-radius: 999px; padding: 4px 14px;
    font-size: 0.85rem; font-weight: 600; margin-top: 2px;
}

/* ---------- confetti ---------- */
.confetti-canvas {
    position: fixed; top: 0; left: 0;
    width: 100vw; height: 100vh;
    pointer-events: none; z-index: 9999;
}

/* ---------- responsive ---------- */
@media (max-width: 768px) {
    .hero h1 { font-size: 1.7rem; }
    .glass-card { padding: 16px 12px 12px; }
    .card-title { font-size: 1rem; }
    .lb-card { padding: 16px 12px 12px; }
}

/* ---------- star buttons: small, inline, no box ---------- */
div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] button {
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
    min-height: 0 !important;
    min-width: 0 !important;
    line-height: 1 !important;
    font-size: 1.25rem !important;
    color: #555 !important;
    transition: transform 0.12s !important;
    width: auto !important;
}
div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] button:hover {
    transform: scale(1.3) !important;
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    color: #fbbf24 !important;
}
div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] button:focus {
    box-shadow: none !important;
    outline: none !important;
}

/* Override for the Submit button (primary) so it keeps its style */
div.stButton > button[kind="primary"],
div.stButton > button[data-testid="stBaseButton-primary"] {
    font-size: 1.1rem !important;
    padding: 14px 36px !important;
    min-height: unset !important;
}

.stSelectbox label, .stRadio label, .stSlider label {
    color: #e0e0e0 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Confetti JS
# ---------------------------------------------------------------------------
CONFETTI_JS = """
<canvas id="confetti-canvas" class="confetti-canvas"></canvas>
<script>
(function(){
    const c=document.getElementById('confetti-canvas'),x=c.getContext('2d');
    c.width=window.innerWidth;c.height=window.innerHeight;
    const p=[],cl=['#fbbf24','#f97316','#ef4444','#10b981','#3b82f6','#8b5cf6','#ec4899'];
    for(let i=0;i<200;i++){p.push({x:Math.random()*c.width,y:Math.random()*c.height-c.height,
    w:Math.random()*10+5,h:Math.random()*6+3,color:cl[Math.floor(Math.random()*cl.length)],
    vy:Math.random()*4+2,vx:(Math.random()-0.5)*3,rot:Math.random()*360,vr:(Math.random()-0.5)*8});}
    let f=0;function d(){x.clearRect(0,0,c.width,c.height);p.forEach(q=>{x.save();
    x.translate(q.x,q.y);x.rotate(q.rot*Math.PI/180);x.fillStyle=q.color;
    x.fillRect(-q.w/2,-q.h/2,q.w,q.h);x.restore();q.y+=q.vy;q.x+=q.vx;
    q.rot+=q.vr;q.vy+=0.05;});f++;if(f<180)requestAnimationFrame(d);
    else{x.clearRect(0,0,c.width,c.height);c.remove();}}d();
})();
</script>
"""

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
if "votes" not in st.session_state:
    st.session_state.votes = {ad["id"]: [] for ad in ADS}
if "current_ratings" not in st.session_state:
    st.session_state.current_ratings = {ad["id"]: 0 for ad in ADS}
if "show_confetti" not in st.session_state:
    st.session_state.show_confetti = False
if "total_submissions" not in st.session_state:
    st.session_state.total_submissions = 0

# Ensure new ads get added to existing state
for ad in ADS:
    if ad["id"] not in st.session_state.votes:
        st.session_state.votes[ad["id"]] = []
    if ad["id"] not in st.session_state.current_ratings:
        st.session_state.current_ratings[ad["id"]] = 0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def avg_rating(ad_id: str) -> float:
    v = st.session_state.votes.get(ad_id, [])
    return sum(v) / len(v) if v else 0.0


def star_display(rating: float) -> str:
    full = int(rating)
    half = rating - full >= 0.5
    return "★" * full + ("½" if half else "") + "☆" * (5 - full - (1 if half else 0))


def youtube_embed_url(url: str) -> str:
    video_id = url.split("v=")[-1].split("&")[0]
    return f"https://www.youtube.com/embed/{video_id}"


def star_rating_component(ad_id: str, current: int) -> int:
    """Render an inline clickable star rating using HTML/JS via components."""
    stars_html = ""
    for i in range(1, 6):
        cls = "star active" if i <= current else "star"
        stars_html += f'<span class="{cls}" data-val="{i}">★</span>'

    html = f"""
    <div id="sr-{ad_id}" class="star-rating" style="display:flex;gap:2px;margin:4px 0 8px 0;">
        {stars_html}
    </div>
    <style>
        body {{ margin: 0; background: transparent; overflow: hidden; }}
        .star-rating .star {{
            font-size: 1.3rem; cursor: pointer;
            transition: transform 0.12s, color 0.15s;
            user-select: none; color: #555;
        }}
        .star-rating .star.active {{ color: #fbbf24; }}
        .star-rating .star:hover {{ transform: scale(1.25); }}
    </style>
    <script>
        const stars = document.querySelectorAll('#sr-{ad_id} .star');
        stars.forEach(s => {{
            s.addEventListener('click', () => {{
                const val = parseInt(s.dataset.val);
                // Send the value back to Streamlit
                window.parent.postMessage({{
                    type: 'streamlit:setComponentValue',
                    value: val,
                    dataType: 'json',
                }}, '*');
            }});
            s.addEventListener('mouseenter', () => {{
                const val = parseInt(s.dataset.val);
                stars.forEach((ss, idx) => {{
                    ss.style.color = idx < val ? '#fbbf24' : '#555';
                }});
            }});
        }});
        document.getElementById('sr-{ad_id}').addEventListener('mouseleave', () => {{
            stars.forEach(ss => {{
                ss.style.color = ss.classList.contains('active') ? '#fbbf24' : '#555';
            }});
        }});
    </script>
    """
    return html


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    """
<div class="hero">
    <h1>🏈 Super Bowl LX Ad Rater</h1>
    <p>Rate every AI ad from the Big Game — who won the Super Bowl of AI?</p>
</div>
""",
    unsafe_allow_html=True,
)

if st.session_state.show_confetti:
    st.markdown(CONFETTI_JS, unsafe_allow_html=True)
    st.session_state.show_confetti = False

# ---------------------------------------------------------------------------
# Layout: Cards (left 3/5) + Leaderboard (right 2/5)
# ---------------------------------------------------------------------------
col_cards, col_lb = st.columns([3, 2], gap="large")

# ---------------------------------------------------------------------------
# Ad cards – 2 columns, with embedded YouTube videos + clickable stars
# ---------------------------------------------------------------------------
with col_cards:
    card_cols = st.columns(2)
    for idx, ad in enumerate(ADS):
        with card_cols[idx % 2]:
            embed = youtube_embed_url(ad["youtube"])
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

            # Embedded YouTube player
            st.markdown(
                f"""
<div class="video-wrapper">
    <iframe src="{embed}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
""",
                unsafe_allow_html=True,
            )

            # Clickable star rating – inline buttons, no box
            current = st.session_state.current_ratings[ad["id"]]
            star_cols = st.columns([1, 1, 1, 1, 1, 3], gap="small")
            for s in range(1, 6):
                with star_cols[s - 1]:
                    filled = s <= current
                    label = "★" if filled else "☆"
                    if st.button(
                        label,
                        key=f"star_{ad['id']}_{s}",
                        help=f"{s} star{'s' if s > 1 else ''}",
                    ):
                        if current == s:
                            st.session_state.current_ratings[ad["id"]] = 0
                        else:
                            st.session_state.current_ratings[ad["id"]] = s
                        st.rerun()

            st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Leaderboard
# ---------------------------------------------------------------------------
with col_lb:
    # Sort: ads with votes first (by avg desc, then by vote count desc),
    # then unvoted ads in their original order
    voted = [
        (ad, avg_rating(ad["id"]), len(st.session_state.votes[ad["id"]]))
        for ad in ADS
        if st.session_state.votes[ad["id"]]
    ]
    unvoted = [ad for ad in ADS if not st.session_state.votes[ad["id"]]]
    voted.sort(key=lambda x: (x[1], x[2]), reverse=True)
    sorted_ads = [ad for ad, _, _ in voted] + unvoted

    num_voted = len(voted)
    rank_medals = ["🥇", "🥈", "🥉"] + [f"{i}." for i in range(4, len(ADS) + 1)]
    rank_classes = ["gold", "silver", "bronze"] + ["" for _ in range(len(ADS) - 3)]

    lb_rows = ""
    for rank, ad in enumerate(sorted_ads):
        avg = avg_rating(ad["id"])
        vote_count = len(st.session_state.votes[ad["id"]])
        has_votes = vote_count > 0
        stars_str = star_display(avg) if has_votes else "☆☆☆☆☆"
        avg_str = f"{avg:.1f}" if has_votes else "—"
        votes_str = f"{vote_count} vote{'s' if vote_count != 1 else ''}" if has_votes else "no votes"
        # Only apply medal highlighting to voted ads
        cls = rank_classes[rank] if has_votes and rank < 3 else ""

        lb_rows += f"""
        <div class="lb-row {cls}">
            <div class="lb-rank">{rank_medals[rank]}</div>
            <div class="lb-icon">{ad['icon']}</div>
            <div class="lb-name">{ad['company']}</div>
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

    st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

    # Total votes badge
    if st.session_state.total_submissions:
        st.markdown(
            f'<div style="text-align:center"><span class="vote-badge">'
            f'🗳️ {st.session_state.total_submissions} total '
            f'submission{"s" if st.session_state.total_submissions != 1 else ""}'
            f'</span></div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # Submit button
    has_any_rating = any(v > 0 for v in st.session_state.current_ratings.values())

    if st.button("🏈  Submit Your Vote!", use_container_width=True, disabled=not has_any_rating, type="primary"):
        for ad in ADS:
            r = st.session_state.current_ratings[ad["id"]]
            if r > 0:
                st.session_state.votes[ad["id"]].append(r)
        st.session_state.current_ratings = {ad["id"]: 0 for ad in ADS}
        st.session_state.total_submissions += 1
        st.session_state.show_confetti = True
        st.rerun()

    if not has_any_rating:
        st.markdown(
            '<p style="text-align:center;opacity:0.45;font-size:0.85rem;margin-top:6px;">'
            "Rate at least one ad to submit</p>",
            unsafe_allow_html=True,
        )
