import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="TalentBridge — Smart HR & Recruitment",
    page_icon="🎯",
    layout="wide",
)

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

/* Hero */
.hero-box {
    background: linear-gradient(135deg, #0d0f14 0%, #141720 100%);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    margin-bottom: 1.5rem;
}
.hero-title { font-size: 2.6rem; font-weight: 800; color: #f0f2f8; line-height: 1.1; margin-bottom: 0.5rem; }
.hero-title em { color: #4f8ef7; font-style: normal; }
.hero-sub { font-size: 1rem; color: #8b90a7; margin-bottom: 1.5rem; max-width: 540px; }
.hero-badge {
    display: inline-block;
    background: rgba(79,142,247,0.12);
    border: 1px solid rgba(79,142,247,0.3);
    color: #4f8ef7;
    font-size: 0.72rem;
    font-weight: 600;
    padding: 5px 14px;
    border-radius: 99px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

/* Stat pill */
.stat-pill {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    text-align: center;
}
.stat-pill strong { display: block; font-size: 1.8rem; font-weight: 800; color: #f0f2f8; }
.stat-pill span { font-size: 0.75rem; color: #8b90a7; }

/* KPI card */
.kpi-card {
    background: #1e2235;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.5rem;
}
.kpi-label { font-size: 0.68rem; color: #8b90a7; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }
.kpi-val { font-size: 1.9rem; font-weight: 800; line-height: 1; margin-bottom: 4px; }
.kpi-trend { font-size: 0.72rem; color: #8b90a7; }
.up { color: #34d399; } .dn { color: #f87171; }

/* Section label */
.sec-label { font-size: 0.72rem; font-weight: 600; color: #4f8ef7; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
.sec-title { font-size: 1.7rem; font-weight: 800; color: #f0f2f8; line-height: 1.15; margin-bottom: 0.4rem; }
.sec-sub { font-size: 0.9rem; color: #8b90a7; line-height: 1.7; }

/* Funnel row */
.funnel-label { font-size: 0.8rem; color: #8b90a7; }
.funnel-val { font-size: 0.8rem; font-weight: 600; }

/* Role card */
.role-card {
    background: #1c2030;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 0.75rem;
    transition: border-color 0.2s;
}
.role-title { font-size: 1rem; font-weight: 700; color: #f0f2f8; margin-bottom: 4px; }
.role-meta { font-size: 0.78rem; color: #8b90a7; }
.dept-badge {
    display: inline-block;
    font-size: 0.65rem;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 99px;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 8px;
}

/* Service card */
.svc-card {
    background: #1e2235;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 1.4rem;
    height: 100%;
}
.svc-icon { font-size: 1.6rem; margin-bottom: 10px; }
.svc-title { font-size: 1rem; font-weight: 700; color: #f0f2f8; margin-bottom: 6px; }
.svc-desc { font-size: 0.82rem; color: #8b90a7; line-height: 1.6; }

/* Testi card */
.testi-card {
    background: #1e2235;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 1.5rem;
    height: 100%;
}
.testi-stars { color: #f59e0b; font-size: 0.9rem; margin-bottom: 10px; }
.testi-text { font-size: 0.88rem; color: #8b90a7; line-height: 1.7; font-style: italic; margin-bottom: 14px; }
.testi-name { font-size: 0.88rem; font-weight: 600; color: #f0f2f8; }
.testi-role { font-size: 0.75rem; color: #8b90a7; }

/* Step card */
.step-card {
    background: #1c2030;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 1.6rem;
    height: 100%;
}
.step-num { font-size: 2.8rem; font-weight: 800; color: rgba(79,142,247,0.18); line-height: 1; margin-bottom: 10px; }
.step-title { font-size: 1rem; font-weight: 700; color: #f0f2f8; margin-bottom: 8px; }
.step-desc { font-size: 0.82rem; color: #8b90a7; line-height: 1.6; }

/* FAQ */
.faq-q { font-size: 0.95rem; font-weight: 600; color: #f0f2f8; }
.faq-a { font-size: 0.85rem; color: #8b90a7; line-height: 1.7; padding-top: 8px; }

/* Footer */
.footer-box {
    background: #141720;
    border-top: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 2rem;
    margin-top: 2rem;
}
.footer-brand { font-size: 1.1rem; font-weight: 800; color: #f0f2f8; }
.footer-desc { font-size: 0.82rem; color: #8b90a7; line-height: 1.7; margin-top: 8px; }
.footer-head { font-size: 0.75rem; font-weight: 700; color: #f0f2f8; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; }
.footer-link { font-size: 0.82rem; color: #8b90a7; display: block; margin-bottom: 6px; }

div[data-testid="stExpander"] { background: #1c2030; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; }
</style>
""", unsafe_allow_html=True)


# ── PLOTLY DARK THEME ────────────────────────────────────────────────────────
PLOT_BG   = "#1e2235"
PAPER_BG  = "#1e2235"
GRID_COL  = "rgba(255,255,255,0.04)"
TEXT_COL  = "#8b90a7"

def dark_layout(fig, title=""):
    fig.update_layout(
        paper_bgcolor=PAPER_BG, plot_bgcolor=PLOT_BG,
        font=dict(family="Inter", color=TEXT_COL, size=12),
        title=dict(text=title, font=dict(color="#f0f2f8", size=13)),
        margin=dict(l=16, r=16, t=36 if title else 16, b=16),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=11)),
    )
    fig.update_xaxes(gridcolor=GRID_COL, zerolinecolor=GRID_COL, tickfont=dict(color=TEXT_COL))
    fig.update_yaxes(gridcolor=GRID_COL, zerolinecolor=GRID_COL, tickfont=dict(color=TEXT_COL))
    return fig


# ════════════════════════════════════════════════════════════════════════════
# HERO
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-box">
  <div class="hero-badge">🎯 Smart HR & Recruitment Platform</div>
  <div class="hero-title">Hire <em>Smarter.</em><br/>Grow Faster.</div>
  <div class="hero-sub">Transform your talent acquisition with data-driven insights, automated pipelines, and precision hiring — built for modern HR teams that demand results.</div>
</div>
""", unsafe_allow_html=True)

h1, h2, h3 = st.columns(3)
with h1:
    st.markdown('<div class="stat-pill"><strong>1,842</strong><span>Applications Q1</span></div>', unsafe_allow_html=True)
with h2:
    st.markdown('<div class="stat-pill"><strong>28d</strong><span>Avg. Time-to-Hire</span></div>', unsafe_allow_html=True)
with h3:
    st.markdown('<div class="stat-pill"><strong>82%</strong><span>Offer Acceptance</span></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# ABOUT + FUNNEL
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-label">About Us</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Discover how we transform recruitment into a precision science</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-sub">TalentBridge combines intelligent automation with human expertise to help organizations hire the right people — faster and smarter.</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

ab1, ab2 = st.columns([1, 1], gap="large")

with ab1:
    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown('<div class="kpi-card"><div class="kpi-label">Industries Served</div><div class="kpi-val" style="color:#4f8ef7">25+</div><div class="kpi-trend">With tailored hiring strategies</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-card"><div class="kpi-label">Support</div><div class="kpi-val" style="color:#34d399">24/7</div><div class="kpi-trend">Pipeline monitoring</div></div>', unsafe_allow_html=True)
    with sc2:
        st.markdown('<div class="kpi-card"><div class="kpi-label">Client Satisfaction</div><div class="kpi-val" style="color:#a78bfa">98%</div><div class="kpi-trend">On placement quality</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-card"><div class="kpi-label">Speed vs. Traditional</div><div class="kpi-val" style="color:#f59e0b">2.4x</div><div class="kpi-trend">Faster hiring</div></div>', unsafe_allow_html=True)

with ab2:
    st.markdown('<div class="sec-label" style="margin-bottom:10px">Hiring Funnel — Q1 2025</div>', unsafe_allow_html=True)
    funnel_data = [
        ("Applications", 1842, "#4f8ef7"),
        ("Screened",     920,  "#a78bfa"),
        ("Interviewed",  460,  "#34d399"),
        ("Offers Made",  127,  "#f59e0b"),
        ("Hires Placed", 104,  "#f87171"),
    ]
    for label, count, color in funnel_data:
        pct = round(count / 1842 * 100)
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px">
          <div style="width:100px;font-size:12px;color:#8b90a7;flex-shrink:0">{label}</div>
          <div style="flex:1;height:26px;background:rgba(255,255,255,0.05);border-radius:6px;overflow:hidden">
            <div style="width:{pct}%;height:100%;background:{color};display:flex;align-items:center;padding-left:10px">
              <span style="font-size:11px;font-weight:600;color:rgba(255,255,255,0.9)">{count:,}</span>
            </div>
          </div>
          <div style="width:38px;font-size:12px;font-weight:600;color:{color};text-align:right">{pct}%</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")


# ════════════════════════════════════════════════════════════════════════════
# SERVICES
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-label">What We Do</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Empowering your growth through expert HR service offerings</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

services = [
    ("🔍", "Talent Sourcing",           "Multi-channel sourcing across job boards, LinkedIn, referrals, and direct pipelines to build a rich candidate pool."),
    ("📋", "Applicant Tracking",         "End-to-end ATS to manage every candidate from application to offer — with real-time stage visibility."),
    ("📊", "HR Analytics & Reporting",   "Executive dashboards with funnel conversion, time-to-hire, cost-per-hire, and department breakdown insights."),
    ("🚀", "Onboarding Automation",      "Seamless digital onboarding workflows — from offer acceptance to first-day checklist and beyond."),
    ("🤝", "Interview Coordination",     "Automated scheduling, panel management, and structured feedback collection to accelerate decisions."),
    ("🏆", "Employer Branding",          "Build a magnetic employer brand with career pages, candidate experience design, and NPS tracking."),
]
cols = st.columns(3, gap="small")
for i, (icon, title, desc) in enumerate(services):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="svc-card">
          <div class="svc-icon">{icon}</div>
          <div class="svc-title">{title}</div>
          <div class="svc-desc">{desc}</div>
        </div><br>
        """, unsafe_allow_html=True)

st.markdown("---")


# ════════════════════════════════════════════════════════════════════════════
# HOW IT WORKS
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-label">How It Works</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Step-by-step breakdown of our reliable HR recruitment approach</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

steps = [
    ("01", "Discovery & Workforce Planning",       "We analyse your business goals, headcount requirements, and role specifications through collaborative sessions with your HR leadership team."),
    ("02", "Sourcing & Pipeline Build",             "Targeted multi-channel sourcing activates job boards, social media, referral programs, and passive candidate outreach simultaneously."),
    ("03", "Screening & Interview Management",      "Structured screening, competency-based interviews, and panel coordination ensure every candidate is assessed consistently and fairly."),
    ("04", "Offer, Hire & Onboarding",              "From negotiation through digital offer delivery to 90-day onboarding tracking — we make every hire stick from day one."),
]
scols = st.columns(4, gap="small")
for i, (num, title, desc) in enumerate(steps):
    with scols[i]:
        st.markdown(f"""
        <div class="step-card">
          <div class="step-num">{num}</div>
          <div class="step-title">{title}</div>
          <div class="step-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>---", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# KPI DASHBOARD
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-label">Live Insights</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Q1 2025 — Recruitment performance metrics</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

kpis = [
    ("Open Roles",       "48",    "#4f8ef7", "↑", "up",  "+6 vs last quarter"),
    ("Applications",     "1,842", "#34d399", "↑", "up",  "+18% growth"),
    ("Offers Made",      "127",   "#a78bfa", "↑", "up",  "6.9% offer rate"),
    ("Hires Placed",     "104",   "#f59e0b", "↑", "up",  "81.9% acceptance"),
    ("Avg Time-to-Hire", "28d",   "#f87171", "↓", "dn",  "–4d improved"),
    ("Cost Per Hire",    "₹41k",  "#34d399", "↓", "dn",  "–₹3k saved"),
]
k_cols = st.columns(6, gap="small")
for i, (label, val, color, arrow, cls, trend) in enumerate(kpis):
    with k_cols[i]:
        st.markdown(f"""
        <div class="kpi-card" style="border-top:3px solid {color}">
          <div class="kpi-label">{label}</div>
          <div class="kpi-val" style="color:{color}">{val}</div>
          <div class="kpi-trend"><span class="{cls}">{arrow}</span> {trend}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Charts ──────────────────────────────────────────────────────────────────
ch1, ch2 = st.columns([1.6, 1], gap="medium")

with ch1:
    df_trend = pd.DataFrame({
        "Month":        ["Jan", "Feb", "Mar"],
        "Applications": [560, 682, 600],
        "Offers Made":  [42,  48,  37],
        "Hires Placed": [32,  38,  34],
    })
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(x=df_trend["Month"], y=df_trend["Applications"],
        name="Applications", line=dict(color="#4f8ef7", width=2.5), fill="tozeroy",
        fillcolor="rgba(79,142,247,0.08)", mode="lines+markers", marker=dict(size=6)))
    fig_trend.add_trace(go.Scatter(x=df_trend["Month"], y=df_trend["Offers Made"],
        name="Offers Made", line=dict(color="#a78bfa", width=2.5, dash="dot"),
        mode="lines+markers", marker=dict(size=6)))
    fig_trend.add_trace(go.Scatter(x=df_trend["Month"], y=df_trend["Hires Placed"],
        name="Hires Placed", line=dict(color="#34d399", width=2.5, dash="dash"),
        mode="lines+markers", marker=dict(size=6)))
    dark_layout(fig_trend, "Monthly hiring trend — Jan to Mar")
    fig_trend.update_layout(height=270, legend=dict(orientation="h", y=-0.2))
    st.plotly_chart(fig_trend, use_container_width=True)

with ch2:
    depts = ["Engineering", "Sales", "Product", "Operations", "HR"]
    counts = [40, 25, 18, 13, 8]
    colors = ["#4f8ef7", "#34d399", "#a78bfa", "#f59e0b", "#f87171"]
    fig_donut = go.Figure(go.Pie(
        labels=depts, values=counts,
        hole=0.62,
        marker=dict(colors=colors, line=dict(color="#1e2235", width=3)),
        textinfo="none",
        hovertemplate="%{label}: %{value} hires<extra></extra>"
    ))
    dark_layout(fig_donut, "Hires by department")
    fig_donut.update_layout(
        height=270,
        legend=dict(orientation="v", x=1.02, font=dict(size=11)),
        annotations=[dict(text="104<br><span style='font-size:10px'>total</span>",
                          x=0.5, y=0.5, font_size=16, showarrow=False,
                          font=dict(color="#f0f2f8"))]
    )
    st.plotly_chart(fig_donut, use_container_width=True)

st.markdown("---")


# ════════════════════════════════════════════════════════════════════════════
# OPEN ROLES
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-label">Live Positions</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Select your next hire</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

roles = [
    ("Engineering", "#4f8ef7", "rgba(79,142,247,0.15)",  "Senior Full Stack Engineer",       "📍 Bangalore",  "💼 Full-time", "₹22–30 LPA", True),
    ("Sales",       "#34d399", "rgba(52,211,153,0.15)",   "Enterprise Account Executive",     "📍 Mumbai",     "💼 Full-time", "₹18–24 LPA", False),
    ("Product",     "#a78bfa", "rgba(167,139,250,0.15)",  "Product Manager — Growth",         "📍 Remote",     "💼 Full-time", "₹20–28 LPA", True),
    ("Operations",  "#f59e0b", "rgba(245,158,11,0.15)",   "Supply Chain Analyst",             "📍 Chennai",    "💼 Full-time", "₹10–14 LPA", False),
    ("HR",          "#f87171", "rgba(248,113,113,0.15)",  "HR Business Partner",              "📍 Hyderabad",  "💼 Full-time", "₹12–16 LPA", True),
    ("Engineering", "#4f8ef7", "rgba(79,142,247,0.15)",  "DevOps / Cloud Infrastructure Lead","📍 Pune",      "💼 Full-time", "₹25–35 LPA", False),
]
rc1, rc2 = st.columns(2, gap="medium")
for i, (dept, color, bg, title, loc, wtype, sal, is_new) in enumerate(roles):
    col = rc1 if i % 2 == 0 else rc2
    with col:
        new_badge = '<span style="font-size:11px;font-weight:600;color:#34d399">● New</span>' if is_new else ""
        st.markdown(f"""
        <div class="role-card">
          <div style="display:flex;justify-content:space-between;margin-bottom:6px">
            <span class="dept-badge" style="background:{bg};color:{color}">{dept}</span>
            {new_badge}
          </div>
          <div class="role-title">{title}</div>
          <div class="role-meta">{loc} &nbsp;·&nbsp; {wtype} &nbsp;·&nbsp; {sal}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")


# ════════════════════════════════════════════════════════════════════════════
# TESTIMONIALS
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-label">Our Testimonials</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Client stories that showcase our commitment to hiring excellence</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

testimonials = [
    ("MS", "#4f8ef7", "rgba(79,142,247,0.2)",
     "TalentBridge completely transformed how we hire engineers. The pipeline visibility alone saved our team weeks of manual tracking every quarter.",
     "Maya Singh", "VP of Engineering, NovaTech"),
    ("AR", "#34d399", "rgba(52,211,153,0.2)",
     "From sourcing to onboarding, every step is tracked and measured. We reduced our average time-to-hire from 45 days down to 28 days within a single quarter.",
     "Arjun Rajan", "Head of HR, FinServe India"),
    ("PK", "#a78bfa", "rgba(167,139,250,0.2)",
     "The analytics dashboards give our leadership real insight into hiring health. We now make workforce decisions backed by data, not guesswork.",
     "Priya Krishnan", "CHRO, MedPlus Group"),
]
tc = st.columns(3, gap="medium")
for i, (initials, color, bg, text, name, role) in enumerate(testimonials):
    with tc[i]:
        st.markdown(f"""
        <div class="testi-card">
          <div class="testi-stars">★★★★★</div>
          <div class="testi-text">"{text}"</div>
          <div style="display:flex;align-items:center;gap:10px">
            <div style="width:38px;height:38px;border-radius:50%;background:{bg};color:{color};
                        display:flex;align-items:center;justify-content:center;
                        font-weight:800;font-size:13px;flex-shrink:0">{initials}</div>
            <div>
              <div class="testi-name">{name}</div>
              <div class="testi-role">{role}</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>---", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# FAQ
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-label">FAQs</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Answers to common questions about our services</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

faqs = [
    ("What types of roles do you specialise in recruiting?",
     "We specialise across all functions — Engineering, Product, Sales, Operations, Finance, and HR — for startups to enterprise organisations. Our recruiters are domain-matched to ensure deep role understanding and faster, higher-quality placements."),
    ("How long does a typical hire take with TalentBridge?",
     "Our current average time-to-hire is 28 days end-to-end, down from an industry average of 45 days. For senior roles or niche skills, we provide a realistic timeline estimate upfront during our discovery call."),
    ("Can you integrate with our existing HRMS or ATS?",
     "Yes. TalentBridge integrates natively with major platforms including Workday, Darwinbox, Zoho People, Greenhouse, and Lever. Our engineering team also supports custom API integrations for enterprise clients."),
    ("What is your replacement guarantee policy?",
     "All permanent placements come with a 90-day replacement guarantee. If a placed candidate exits within this window for performance or fit reasons, we re-initiate the search at no additional cost."),
    ("How do we get started with TalentBridge?",
     "Simply fill out our 'Post a Job' form or schedule a free 30-minute consultation call. Our onboarding team will set up your account, configure your dashboard, and launch your first sourcing campaign within 48 hours."),
]
for q, a in faqs:
    with st.expander(q):
        st.markdown(f'<div class="faq-a">{a}</div>', unsafe_allow_html=True)

st.markdown("<br>---", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# CTA
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:#1c2030;border:1px solid rgba(255,255,255,0.08);border-radius:20px;
            padding:3rem 2rem;text-align:center;margin-bottom:1.5rem">
  <div class="sec-label" style="text-align:center">Join Us Today</div>
  <div class="sec-title" style="text-align:center">Ready to build your dream team?</div>
  <div class="sec-sub" style="text-align:center;margin:0 auto 1.5rem;max-width:540px">
    Don't settle for slow, costly hiring. Join hundreds of companies that trust TalentBridge to find and retain exceptional talent.
  </div>
  <div style="display:flex;justify-content:center;gap:40px;flex-wrap:wrap;margin-top:1.5rem">
    <div style="text-align:center"><strong style="font-size:1.4rem;font-weight:800;color:#4f8ef7">4.9/5</strong>
      <div style="font-size:0.72rem;color:#8b90a7;margin-top:4px">Over 1,200 reviews</div></div>
    <div style="text-align:center"><strong style="font-size:1.4rem;font-weight:800;color:#34d399">500+</strong>
      <div style="font-size:0.72rem;color:#8b90a7;margin-top:4px">Companies hired</div></div>
    <div style="text-align:center"><strong style="font-size:1.4rem;font-weight:800;color:#a78bfa">₹0</strong>
      <div style="font-size:0.72rem;color:#8b90a7;margin-top:4px">To get started</div></div>
  </div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer-box">
  <div style="display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:2rem;flex-wrap:wrap">
    <div>
      <div class="footer-brand">🔵 TalentBridge</div>
      <div class="footer-desc">Empowering organisations with intelligent recruitment, data-driven hiring decisions, and seamless onboarding automation.</div>
    </div>
    <div>
      <div class="footer-head">Quick Links</div>
      <span class="footer-link">About Us</span>
      <span class="footer-link">Services</span>
      <span class="footer-link">Open Roles</span>
      <span class="footer-link">Contact</span>
    </div>
    <div>
      <div class="footer-head">Services</div>
      <span class="footer-link">Talent Sourcing</span>
      <span class="footer-link">Applicant Tracking</span>
      <span class="footer-link">HR Analytics</span>
      <span class="footer-link">Onboarding</span>
    </div>
    <div>
      <div class="footer-head">Contact Us</div>
      <span class="footer-link">📍 Coimbatore, TN, India</span>
      <span class="footer-link">📞 +91 98765 43210</span>
      <span class="footer-link">✉️ hello@talentbridge.in</span>
      <span class="footer-link">Mon–Fri: 9AM – 7PM</span>
    </div>
  </div>
  <div style="border-top:1px solid rgba(255,255,255,0.08);margin-top:1.5rem;padding-top:1rem;
              font-size:0.75rem;color:#555c75;text-align:center">
    © 2025 TalentBridge. All Rights Reserved.
  </div>
</div>
""", unsafe_allow_html=True)
