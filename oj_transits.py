"""
Compute Rahu / Ketu sidereal transits at each significant life event of
O. J. Simpson, and report the natal-house each node was transiting,
plus its current sign and aspect to natal points.

Uses Lahiri ayanamsa.  Houses are determined by *whole-sign* count from
the natal Ascendant (the standard Vedic system).
"""
import swisseph as swe
from datetime import datetime, timedelta, timezone

swe.set_sid_mode(swe.SIDM_LAHIRI)
FLAGS = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED

SIGNS = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo',
         'Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces']

# ---- Natal data (re-computed for self-containment) ----
BIRTH = datetime(1947, 7, 9, 16, 8, 0, tzinfo=timezone.utc)   # 08:08 PST
LAT, LON = 37.7749, -122.4194
JD0 = swe.julday(BIRTH.year, BIRTH.month, BIRTH.day,
                 BIRTH.hour + BIRTH.minute/60)

def slong(jd, pid):
    return swe.calc_ut(jd, pid, FLAGS)[0][0] % 360

natal = {
    'Sun'    : slong(JD0, swe.SUN),
    'Moon'   : slong(JD0, swe.MOON),
    'Mars'   : slong(JD0, swe.MARS),
    'Mercury': slong(JD0, swe.MERCURY),
    'Jupiter': slong(JD0, swe.JUPITER),
    'Venus'  : slong(JD0, swe.VENUS),
    'Saturn' : slong(JD0, swe.SATURN),
    'Rahu'   : slong(JD0, swe.MEAN_NODE),
}
natal['Ketu'] = (natal['Rahu'] + 180) % 360

ayan = swe.get_ayanamsa_ut(JD0)
cusps_trop, ascmc_trop = swe.houses(JD0, LAT, LON, b'P')
ASC = (ascmc_trop[0] - ayan) % 360
asc_sign = int(ASC // 30)              # Leo = 4
print(f"Natal Ascendant: {ASC:.2f}° ({SIGNS[asc_sign]})")
print(f"Natal Rahu: {natal['Rahu']:.2f}° ({SIGNS[int(natal['Rahu']//30)]})")
print(f"Natal Ketu: {natal['Ketu']:.2f}° ({SIGNS[int(natal['Ketu']//30)]})\n")

def whole_sign_house(lon):
    """Whole-sign Vedic house number 1-12, given a sidereal longitude."""
    sign_idx = int(lon // 30)
    return ((sign_idx - asc_sign) % 12) + 1

# ---- Major life events (UT noon used when only date known) ----
EVENTS = [
    ("1947-07-09", "Birth (San Francisco)"),
    ("1949-07-09", "~Age 2 — diagnosed with rickets, leg braces"),
    ("1960-07-09", "~Age 13 — joins Persian Warriors gang"),
    ("1967-06-24", "Marries Marguerite Whitley"),
    ("1968-12-04", "Wins Heisman Trophy / daughter Arnelle born"),
    ("1969-01-28", "#1 NFL Draft pick — Buffalo Bills"),
    ("1973-12-16", "First NFL player to rush 2,000 yards (final game of season)"),
    ("1977-09-24", "Daughter Aaren born / meets Nicole Brown"),
    ("1978-03-28", "Traded to San Francisco 49ers"),
    ("1979-03-15", "Divorces Marguerite (approx)"),
    ("1979-08-26", "Daughter Aaren dies (drowning)"),
    ("1979-12-16", "Final NFL game — retires"),
    ("1985-02-02", "Marries Nicole Brown"),
    ("1985-08-03", "Inducted into Pro Football Hall of Fame"),
    ("1989-01-01", "First domestic-violence arrest (NYE 1989 incident)"),
    ("1992-02-25", "Nicole files for divorce"),
    ("1992-10-15", "Divorce from Nicole finalized"),
    ("1994-06-12", "Murders of Nicole Brown & Ron Goldman"),
    ("1994-06-17", "White Bronco chase / arrest"),
    ("1995-01-24", "Murder trial begins"),
    ("1995-10-03", "Acquitted of murder charges"),
    ("1997-02-04", "Civil trial — found liable, $33.5M"),
    ("2007-09-13", "Las Vegas hotel-room confrontation"),
    ("2008-10-03", "Convicted of robbery / kidnapping"),
    ("2008-12-05", "Sentenced 9–33 years, sent to Lovelock"),
    ("2013-07-25", "First parole hearing — partial parole granted"),
    ("2017-07-20", "Parole granted (full)"),
    ("2017-10-01", "Released from prison"),
    ("2023-05-01", "Announces undergoing chemotherapy"),
    ("2024-04-10", "Death (prostate cancer, Las Vegas)"),
]

print(f"{'Date':12s} {'Event':50s}  "
      f"{'Rahu':>14s} H  {'Ketu':>14s} H")
print("-"*112)
for date_str, ev in EVENTS:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    jd = swe.julday(dt.year, dt.month, dt.day, 12.0)
    rahu = slong(jd, swe.MEAN_NODE)
    ketu = (rahu + 180) % 360
    rh = whole_sign_house(rahu)
    kh = whole_sign_house(ketu)
    rsig = SIGNS[int(rahu//30)]
    ksig = SIGNS[int(ketu//30)]
    print(f"{date_str:12s} {ev[:50]:50s}  "
          f"{rahu%30:5.2f}° {rsig:9s} {rh:2d}  "
          f"{ketu%30:5.2f}° {ksig:9s} {kh:2d}")

# Also tag each event with its Vimshottari MD/AD
print("\n\nNow with Vimshottari MD/AD context:\n")

# Re-build the dasha sequence (copied from the main script)
NAKSHATRAS_LORD = ['Ketu','Venus','Sun','Moon','Mars','Rahu','Jupiter','Saturn','Mercury',
                   'Ketu','Venus','Sun','Moon','Mars','Rahu','Jupiter','Saturn','Mercury',
                   'Ketu','Venus','Sun','Moon','Mars','Rahu','Jupiter','Saturn','Mercury']
DASHA_YEARS = {'Ketu':7,'Venus':20,'Sun':6,'Moon':10,'Mars':7,'Rahu':18,'Jupiter':16,'Saturn':19,'Mercury':17}
DASHA_ORDER = ['Ketu','Venus','Sun','Moon','Mars','Rahu','Jupiter','Saturn','Mercury']
NAK_LEN = 360/27
YEAR_DAYS = 365.2425

moon = natal['Moon']
nak_idx = int(moon // NAK_LEN)
lord = NAKSHATRAS_LORD[nak_idx]
pos_in_nak = (moon - nak_idx*NAK_LEN) / NAK_LEN
consumed = pos_in_nak * DASHA_YEARS[lord]

md_full_start = BIRTH - timedelta(days=consumed*YEAR_DAYS)
seq = []  # list of (start, end, MD, AD)
md_lord = lord
md_start = md_full_start
total = 0
while total < 130:
    md_y = DASHA_YEARS[md_lord]
    md_end = md_start + timedelta(days=md_y*YEAR_DAYS)
    order = DASHA_ORDER[DASHA_ORDER.index(md_lord):] + DASHA_ORDER[:DASHA_ORDER.index(md_lord)]
    t = md_start
    for ad_lord in order:
        ad_y = md_y * DASHA_YEARS[ad_lord] / 120
        ad_end = t + timedelta(days=ad_y*YEAR_DAYS)
        seq.append((t, ad_end, md_lord, ad_lord))
        t = ad_end
    total += md_y
    md_start = md_end
    md_lord = DASHA_ORDER[(DASHA_ORDER.index(md_lord)+1) % 9]

def find_dasha(dt):
    dt_aware = dt.replace(tzinfo=timezone.utc)
    for s, e, md, ad in seq:
        if s <= dt_aware < e:
            return md, ad
    return None, None

print(f"{'Date':12s} {'Event':46s}  "
      f"{'Rahu':>16s}  {'Ketu':>16s}  {'MD':8s} {'AD':8s}")
print("-"*120)
for date_str, ev in EVENTS:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    jd = swe.julday(dt.year, dt.month, dt.day, 12.0)
    rahu = slong(jd, swe.MEAN_NODE)
    ketu = (rahu + 180) % 360
    rh = whole_sign_house(rahu)
    kh = whole_sign_house(ketu)
    rsig = SIGNS[int(rahu//30)]
    ksig = SIGNS[int(ketu//30)]
    md, ad = find_dasha(dt)
    print(f"{date_str:12s} {ev[:46]:46s}  "
          f"{rahu%30:5.2f}°{rsig:9s}H{rh:<2d}  "
          f"{ketu%30:5.2f}°{ksig:9s}H{kh:<2d}  "
          f"{md or '':8s} {ad or '':8s}")
