"""
O. J. Simpson — Vedic (Jyotish) chart computation.

Birth: 9 July 1947, 08:08:00 PST (UTC-8), San Francisco, CA
       (37.7749 N, 122.4194 W).  Rodden AA (Astrodatabank).
California did NOT observe daylight saving time in 1947, so PST = UTC-8.

Outputs:
  D1  (Rasi)        — natal sign positions, ascendant, houses
  D9  (Navamsa)     — marriage / dharma / inner truth
  D10 (Dasamsa)     — career / public action
  D11 (Rudramsa)    — destruction, downfall, death-events
                       (some schools call D11 'Labha-amsa' for gains.
                        Here we use the classical 11-part division;
                        Parashara's Rudramsa is the destructive reading.)
  Vimshottari Mahadasha + Antardasha sequence from birth onward,
  using sidereal Moon (Lahiri ayanamsa).

The script is general — change BIRTH_* constants for any chart.
"""
import swisseph as swe
from datetime import datetime, timedelta, timezone

# ---------------------------------------------------------------------------
# 1. BIRTH DATA  (edit these for any other chart)
# ---------------------------------------------------------------------------
BIRTH_LOCAL    = datetime(1947, 7, 9, 8, 8, 0)     # local clock time
UTC_OFFSET_HRS = -8.0                              # PST in 1947 (no DST)
LAT, LON       = 37.7749, -122.4194                # San Francisco

# Sidereal system: Lahiri (Chitrapaksha), the Indian Govt standard.
swe.set_sid_mode(swe.SIDM_LAHIRI)

# ---------------------------------------------------------------------------
# 2. JULIAN DAY (UT)
# ---------------------------------------------------------------------------
birth_utc = BIRTH_LOCAL - timedelta(hours=UTC_OFFSET_HRS)
JD_UT = swe.julday(birth_utc.year, birth_utc.month, birth_utc.day,
                   birth_utc.hour + birth_utc.minute/60 + birth_utc.second/3600)

# ---------------------------------------------------------------------------
# 3. SIDEREAL PLANET LONGITUDES
# ---------------------------------------------------------------------------
SIGNS = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo',
         'Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces']

PLANETS = {
    'Sun'    : swe.SUN,
    'Moon'   : swe.MOON,
    'Mars'   : swe.MARS,
    'Mercury': swe.MERCURY,
    'Jupiter': swe.JUPITER,
    'Venus'  : swe.VENUS,
    'Saturn' : swe.SATURN,
    'Rahu'   : swe.MEAN_NODE,         # mean north node (classical)
}
FLAGS = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED

def sidereal_long(jd, planet_id):
    pos, _ = swe.calc_ut(jd, planet_id, FLAGS)
    return pos[0] % 360

natal = {name: sidereal_long(JD_UT, pid) for name, pid in PLANETS.items()}
# Ketu is exactly opposite Rahu
natal['Ketu'] = (natal['Rahu'] + 180) % 360

# Ascendant (sidereal) — use Placidus and convert
cusps_trop, ascmc_trop = swe.houses(JD_UT, LAT, LON, b'P')
ayan = swe.get_ayanamsa_ut(JD_UT)
ASC = (ascmc_trop[0] - ayan) % 360
MC  = (ascmc_trop[1] - ayan) % 360

natal['Asc'] = ASC

# ---------------------------------------------------------------------------
# 4. HELPERS — sign / nakshatra / divisional charts
# ---------------------------------------------------------------------------
def sign_of(lon):
    return SIGNS[int(lon // 30)]

def deg_in_sign(lon):
    return lon % 30

def fmt(lon):
    s = sign_of(lon)
    d = deg_in_sign(lon)
    deg = int(d); m = (d - deg)*60; mi = int(m); sec = (m-mi)*60
    return f"{deg:02d}°{mi:02d}'{sec:04.1f}\" {s}"

# ---------- D1 (Rasi) — same as natal sign ----------
def d1_sign(lon): return sign_of(lon)

# ---------- D9 (Navamsa) ----------
# Each 30° sign is split into 9 parts of 3°20'.  Starting sign of the
# navamsa cycle depends on the rasi's element:
#   movable (Aries, Cancer, Libra, Capricorn)   -> start from same sign
#   fixed   (Taurus, Leo, Scorpio, Aquarius)    -> start from 9th sign
#   dual    (Gemini, Virgo, Sag, Pisces)        -> start from 5th sign
def d9_sign(lon):
    sign_idx = int(lon // 30)
    pada     = int((lon % 30) // (30/9))         # 0..8
    mode = sign_idx % 3        # 0 movable, 1 fixed, 2 dual
    if   mode == 0: start = sign_idx
    elif mode == 1: start = (sign_idx + 8) % 12
    else:           start = (sign_idx + 4) % 12
    return SIGNS[(start + pada) % 12]

# ---------- D10 (Dasamsa) ----------
# 30° split into 10 parts of 3°.
#   from odd  signs : start from same sign
#   from even signs : start from the 9th sign
def d10_sign(lon):
    sign_idx = int(lon // 30)
    part     = int((lon % 30) // 3)              # 0..9
    if sign_idx % 2 == 0:                         # odd sign (Aries=0 is odd in Jyotish)
        start = sign_idx
    else:                                         # even sign
        start = (sign_idx + 8) % 12
    return SIGNS[(start + part) % 12]

# ---------- D11 (Rudramsa / Labhamsa) ----------
# 30° split into 11 parts of ~2°43.6"
# Per Parashara (BPHS): from any sign count begins from the 11th sign,
# proceeding direct.  (There are competing conventions; this one is the
# most-cited classical rule.)
def d11_sign(lon):
    sign_idx = int(lon // 30)
    part     = int((lon % 30) // (30/11))         # 0..10
    start = (sign_idx + 10) % 12                  # 11th from natal sign
    return SIGNS[(start + part) % 12]

DIVISIONAL = {'D1': d1_sign, 'D9': d9_sign, 'D10': d10_sign, 'D11': d11_sign}

# ---------------------------------------------------------------------------
# 5. NAKSHATRA + VIMSHOTTARI DASHA
# ---------------------------------------------------------------------------
NAKSHATRAS = [
    ('Ashwini',     'Ketu'),     ('Bharani',     'Venus'),
    ('Krittika',    'Sun'),      ('Rohini',      'Moon'),
    ('Mrigashira',  'Mars'),     ('Ardra',       'Rahu'),
    ('Punarvasu',   'Jupiter'),  ('Pushya',      'Saturn'),
    ('Ashlesha',    'Mercury'),  ('Magha',       'Ketu'),
    ('Purva Phalguni','Venus'),  ('Uttara Phalguni','Sun'),
    ('Hasta',       'Moon'),     ('Chitra',      'Mars'),
    ('Swati',       'Rahu'),     ('Vishakha',    'Jupiter'),
    ('Anuradha',    'Saturn'),   ('Jyeshtha',    'Mercury'),
    ('Mula',        'Ketu'),     ('Purva Ashadha','Venus'),
    ('Uttara Ashadha','Sun'),    ('Shravana',    'Moon'),
    ('Dhanishta',   'Mars'),     ('Shatabhisha', 'Rahu'),
    ('Purva Bhadrapada','Jupiter'),('Uttara Bhadrapada','Saturn'),
    ('Revati',      'Mercury'),
]
DASHA_YEARS = {                       # Vimshottari periods (total = 120 y)
    'Ketu':7,    'Venus':20, 'Sun':6,    'Moon':10, 'Mars':7,
    'Rahu':18,   'Jupiter':16,'Saturn':19,'Mercury':17,
}
DASHA_ORDER = ['Ketu','Venus','Sun','Moon','Mars','Rahu','Jupiter','Saturn','Mercury']

NAK_LEN = 360/27          # 13°20' = 13.3333...

def nakshatra_of(lon):
    idx = int(lon // NAK_LEN)
    return idx, NAKSHATRAS[idx]

def vimshottari(birth_dt_utc, moon_lon, horizon_years=130):
    """Yield list of (start_dt, end_dt, MD_lord, AD_lord) covering the
    full life from birth onward."""
    nak_idx, (nak_name, lord) = nakshatra_of(moon_lon)
    # fraction of nakshatra Moon has already traversed
    pos_in_nak = (moon_lon - nak_idx*NAK_LEN) / NAK_LEN
    # time consumed in current MD before birth
    md_total = DASHA_YEARS[lord]
    consumed = pos_in_nak * md_total
    md_remaining = md_total - consumed

    YEAR_DAYS = 365.2425
    sequence = []
    # first MD = current lord, only the remainder
    cur_lord = lord
    cur_start = birth_dt_utc
    cur_end   = cur_start + timedelta(days=md_remaining*YEAR_DAYS)

    # for the first MD we still need antardashas, but only those covering
    # the remaining slice — easier to compute *all* AD positions inside
    # the full natural MD, then clip by birth.
    def antardashas(md_lord, md_full_start, md_years):
        """Yield (ad_start, ad_end, ad_lord) for the natural (uncropped) MD."""
        order = DASHA_ORDER[DASHA_ORDER.index(md_lord):] + DASHA_ORDER[:DASHA_ORDER.index(md_lord)]
        t = md_full_start
        for ad_lord in order:
            ad_years = md_years * DASHA_YEARS[ad_lord] / 120
            ad_end = t + timedelta(days=ad_years*YEAR_DAYS)
            yield t, ad_end, ad_lord
            t = ad_end

    # natural start of the current MD = birth - consumed time
    md_full_start = birth_dt_utc - timedelta(days=consumed*YEAR_DAYS)

    # walk MDs across horizon
    total_years = 0
    md_lord = cur_lord
    md_start_natural = md_full_start
    while total_years < horizon_years:
        md_years = DASHA_YEARS[md_lord]
        md_end_natural = md_start_natural + timedelta(days=md_years*YEAR_DAYS)
        for ad_start, ad_end, ad_lord in antardashas(md_lord, md_start_natural, md_years):
            if ad_end <= birth_dt_utc:
                continue
            ad_start_eff = max(ad_start, birth_dt_utc)
            sequence.append((ad_start_eff, ad_end, md_lord, ad_lord))
        total_years += md_years
        md_start_natural = md_end_natural
        md_lord = DASHA_ORDER[(DASHA_ORDER.index(md_lord)+1) % 9]
    return sequence, nak_name, lord, pos_in_nak

# ---------------------------------------------------------------------------
# 6. PRINT THE NATAL CHART
# ---------------------------------------------------------------------------
print("="*72)
print(f"O. J. SIMPSON — Sidereal (Lahiri) chart")
print(f"Birth: {BIRTH_LOCAL}  PST   (UTC {birth_utc} ; JD {JD_UT:.6f})")
print(f"Place: San Francisco  ({LAT}, {LON})")
print(f"Ayanamsa (Lahiri) = {ayan:.4f}°")
print("="*72)

print(f"\nAscendant: {fmt(ASC)}   (sign lord = ?)")
print(f"Midheaven: {fmt(MC)}\n")

print(f"{'Body':8s} {'Longitude':>22s}   {'D1':12s} {'D9':12s} {'D10':12s} {'D11':12s}")
print("-"*82)
order = ['Sun','Moon','Mars','Mercury','Jupiter','Venus','Saturn','Rahu','Ketu','Asc']
for p in order:
    lon = natal[p]
    print(f"{p:8s} {fmt(lon):>22s}   "
          f"{d1_sign(lon):12s} {d9_sign(lon):12s} "
          f"{d10_sign(lon):12s} {d11_sign(lon):12s}")

# ---------------------------------------------------------------------------
# 7. VIMSHOTTARI DASHA
# ---------------------------------------------------------------------------
seq, nak_name, lord, pos = vimshottari(
    birth_utc.replace(tzinfo=timezone.utc), natal['Moon'], horizon_years=80)

print(f"\nMoon nakshatra: {nak_name}  (lord = {lord}, "
      f"{pos*100:.1f}% traversed at birth)")
print(f"\nVimshottari Mahadasha-Antardasha sequence:")
print(f"{'Start (UTC)':23s} {'End (UTC)':23s}  MD/AD")
print("-"*72)
prev_md = None
for s, e, md, ad in seq:
    tag = f"{md} / {ad}"
    flag = "  <-- new MD" if md != prev_md else ""
    print(f"{s.strftime('%Y-%m-%d %H:%M:%S'):23s} "
          f"{e.strftime('%Y-%m-%d %H:%M:%S'):23s}  {tag}{flag}")
    prev_md = md
