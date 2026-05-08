# 🎯 TalentBridge — Smart HR & Recruitment Dashboard

> A fully interactive HR & Recruitment analytics dashboard built with **Streamlit** and **Plotly**, based on the TalentBridge platform. Tracks the complete candidate journey from application to successful hire.

---

## 🚀 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://talentbridge-dashboard.streamlit.app)

---

## 📸 Features

- **Hero KPI Summary** — Applications, Avg. Time-to-Hire, Offer Acceptance Rate at a glance
- **Hiring Funnel** — Visual drop-off from 1,842 applications → 104 confirmed hires (Q1 2025)
- **6 Live KPI Cards** — Open Roles, Applications, Offers Made, Hires Placed, Time-to-Hire, Cost Per Hire
- **Interactive Charts** — Monthly hiring trend (line chart) + Department-wise hires (donut chart)
- **Open Roles Board** — 6 live job listings across Engineering, Sales, Product, Operations & HR
- **Testimonials** — Client success stories from NovaTech, FinServe India & MedPlus Group
- **FAQ Section** — Expandable answers to common recruitment questions
- **Dark Theme UI** — Custom dark-mode design matching the original TalentBridge brand

---

## 🗂️ Project Structure

```
talentbridge-dashboard/
│
├── streamlit_app.py      # Main Streamlit application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation (this file)
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web app framework |
| [Plotly](https://plotly.com/python/) | Interactive charts |
| [Pandas](https://pandas.pydata.org/) | Data handling |
| HTML + CSS | Custom dark UI styling |

---

## 📦 Installation & Local Setup

Follow these steps to run the dashboard on your own machine:

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/talentbridge-dashboard.git
cd talentbridge-dashboard
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run streamlit_app.py
```

The app will open automatically at `http://localhost:8501`

---

## ☁️ Deploy on Streamlit Community Cloud (Free)

1. Push this repository to **GitHub** (must be Public)
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
3. Click **"New app"**
4. Select this repository and set the main file to `streamlit_app.py`
5. Click **Deploy** ✅

Your app will be live at:
```
https://YOUR_USERNAME-talentbridge-dashboard.streamlit.app
```

---

## 📊 Dashboard Data (Q1 2025)

| Metric | Value |
|--------|-------|
| Total Applications | 1,842 |
| Screened | 920 (50%) |
| Interviewed | 460 (25%) |
| Offers Made | 127 (7%) |
| Hires Placed | 104 (6%) |
| Offer Acceptance Rate | 82% |
| Avg. Time-to-Hire | 28 days |
| Cost Per Hire | ₹41,000 |
| Open Roles | 48 |
| Client Satisfaction | 98% |

---

## 🏢 Open Roles Featured

| Role | Department | Location | Salary |
|------|-----------|----------|--------|
| Senior Full Stack Engineer | Engineering | Bangalore | ₹22–30 LPA |
| Enterprise Account Executive | Sales | Mumbai | ₹18–24 LPA |
| Product Manager — Growth | Product | Remote | ₹20–28 LPA |
| Supply Chain Analyst | Operations | Chennai | ₹10–14 LPA |
| HR Business Partner | HR | Hyderabad | ₹12–16 LPA |
| DevOps / Cloud Infrastructure Lead | Engineering | Pune | ₹25–35 LPA |

---

## 📬 Contact

| | |
|--|--|
| 📍 Location | Coimbatore, TN, India |
| 📞 Phone | +91 98765 43210 |
| ✉️ Email | hello@talentbridge.in |
| 🕐 Hours | Mon–Fri: 9AM – 7PM |

---

## 📄 License

This project is for demonstration and portfolio purposes.
© 2025 TalentBridge. All Rights Reserved.
