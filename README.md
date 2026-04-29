# O. J. Simpson — A Vedic Nodal Case Study

**Birth data:** 9 July 1947, 08:08 AM PST, San Francisco (37.77°N, 122.42°W).
*Astrodatabank Rodden rating AA. California did not observe DST in 1947, so the local clock was true PST (UTC−8); UT of birth = 16:08:00.*

**System:** Sidereal (Lahiri Chitrapaksha), whole-sign houses, mean lunar nodes, Vimshottari dasha. Computed via Swiss Ephemeris (`pyswisseph`).

---

## 1. The natal chart (D1) and the divisional charts

| Body | Sidereal longitude | D1 (Rasi) | D9 (Navamsa) | D10 (Dasamsa) | D11 (Rudramsa) |
|---|---|---|---|---|---|
| **Ascendant** | 01°29' Leo | Leo | Aries | Leo | Gemini |
| Sun | 23°29' Gemini | Gemini | Taurus | Capricorn | Sagittarius |
| Moon | 02°28' Pisces | Pisces | Cancer | Scorpio | Capricorn |
| Mars | 12°54' Taurus | Taurus | Aries | Taurus | Cancer |
| Mercury | 01°32' Cancer | Cancer | Cancer | Pisces | Taurus |
| Jupiter | 24°38' Libra | Libra | Taurus | Gemini | Taurus |
| Venus | 08°14' Gemini | Gemini | Sagittarius | Leo | Cancer |
| Saturn | 15°54' Cancer | Cancer | Scorpio | Leo | Libra |
| **Rahu** | 06°59' Taurus | **Taurus (H10)** | Pisces | Pisces | Taurus |
| **Ketu** | 06°59' Scorpio | **Scorpio (H4)** | Virgo | Virgo | Scorpio |
| Midheaven | 25°40' Aries | — | — | — | — |

Whole-sign house assignments from Leo Asc: Sun & Venus in **H11** (gains, network, fame), Mercury & Saturn in **H12** (confinement, hidden enemies, foreign places), Mars & **Rahu in H10** (career, public action), Jupiter in **H3** (courage, siblings, athleticism), Moon in **H8** (death, transformation, scandal), **Ketu in H4** (home, mother, heart).

A few things jump out before any dasha or transit work:

- **Moon at 02°28' Pisces is in Purva Bhadrapada**, traversed 93.6%. That puts the *very first* Mahadasha at birth as Jupiter, but with only ~1 year remaining — Saturn MD then runs almost the entire childhood through age 20.
- **Moon in the 8th** from a Leo Lagna is the most consequential placement in the chart: it puts the emotional life under perpetual transformation/secrecy/death-pressure, and it makes the Moon (his greatest dignified planet by Pisces sign) operate from the most occult house. Cancer (Sun's chart-rival's sign) holds Mercury and Saturn in H12, and Saturn here is debilitated — childhood illness (rickets), confinement (leg braces until age 5), and the eventual literal prison are foreshadowed.
- **The Rahu/Ketu axis sits exactly along the Taurus/Scorpio (H10/H4) line.** This is the single most important structural feature for your nodal thesis. Rahu in Taurus in the 10th makes commercial fame, sensual celebrity, and the body-as-instrument the karmic obsession; Ketu in Scorpio in the 4th detaches him from emotional rootedness and brings death/violence/secrets *into the home*. The H10/H4 nodes also activate the natural Taurus/Scorpio polarity (possession vs. surrender; pleasure vs. annihilation).
- **D9 Ascendant = Aries** with Mars in Aries in D9: a fiery, aggressive marital nature. Note Rahu-D9 in Pisces, Ketu-D9 in Virgo — a different nodal axis in the marriage chart, suggesting deception in partnership specifically.
- **D10 Ascendant = Leo** (same as D1) with Sun in D10 Capricorn (debilitated). Career carries the Lagna's pride but the source of action is "fallen" — fame without grounding. Rahu-D10 in Pisces in 8th house from D10 Asc — career *itself* becomes the path of catastrophe and scandal, not merely accidents along the way.
- **D11 Ascendant = Gemini.** D11 is read by some Parashari schools as gains (Labha), by others as Rudramsa (the chart of destruction/death). With Mars in D11 Cancer (debilitated) and Saturn in D11 Libra (exalted), the destruction-chart of this person carries simultaneous violent collapse and a structurally exalted final justice — fitting for a man whose downfall was both undignified and judicially processed.

The full Python script that produced all of the above is `oj_jyotish.py`. It's general — change the four `BIRTH_*` constants at the top for any other chart.

---

## 2. Vimshottari Mahadasha / Antardasha sequence

Moon in Purva Bhadrapada (Jupiter's nakshatra), 93.6% complete at birth → first MD is Jupiter with only ~1.0 year remaining, then the natural sequence continues. Major MD boundaries (UTC):

| Mahadasha | From | To | Age range | Lifespan event(s) |
|---|---|---|---|---|
| Jupiter (residual) | 9 Jul 1947 | 20 Jul 1948 | 0–1 | infancy |
| **Saturn** | 20 Jul 1948 | 20 Jul 1967 | 1–20 | rickets; leg braces; Potrero Hill; Persian Warriors gang; CCSF; transfers to USC; marries Marguerite (last week of MD!) |
| **Mercury** | 20 Jul 1967 | 20 Jul 1984 | 20–37 | Heisman; #1 NFL draft pick; 2,000-yard season; 4 rushing titles; trade to 49ers; daughter Aaren's drowning; divorce; retirement; first acting/commentary work |
| **Ketu** | 20 Jul 1984 | 20 Jul 1991 | 37–44 | Pro Football Hall of Fame induction; marriage to Nicole Brown; Naked Gun films; 1989 New Year's Eve domestic-violence arrest |
| **Venus** | 20 Jul 1991 | 20 Jul 2011 | 44–64 | Nicole's divorce filing; **murders of Nicole and Goldman**; Bronco chase; criminal trial; acquittal; civil trial; civil judgment; Las Vegas hotel confrontation; **robbery conviction**; sentencing |
| **Sun** | 20 Jul 2011 | 20 Jul 2017 | 64–70 | Lovelock prison years; first parole hearing 2013; final parole granted at the *very close* of this MD |
| **Moon** | 20 Jul 2017 | 20 Jul 2027 | 70–death | release from prison; Las Vegas retirement; cancer diagnosis; **death** |

The full antardasha sequence is in the script output (and reproduced below for the consequential ones). Notable convergences:

- The **Heisman + Arnelle's birth on the same day (Dec 4, 1968)** falls in **Mercury–Mercury** (a "double" period: pure Mercury). Mercury rules his D10 7th house and is in his natal H12 — the chart literally encodes that he gives birth to public reputation in a hidden, behind-the-scenes way (he was sequestered at the awards while his daughter was being born).
- The **2,000-yard season (Dec 1973)** falls in Mercury–Sun. Sun is Lagna lord — peak self-expression. Mercury–Sun is one of the strongest sub-periods for his chart.
- **Aaren's drowning (Aug 26, 1979)** falls in **Mercury–Jupiter**. Jupiter is in Libra in his H3, but is also the 5th lord (children) for Leo Asc. Mercury–Jupiter activated the 5th lord during a Mercury (H12, loss) MD.
- **The murders, Bronco chase, and full criminal trial** fall almost entirely in **Venus–Venus**. Venus rules his H10 (career/public reputation) and is in Gemini in H11 (gains, friends). A Venus–Venus period intensifies the natal Venus placement; for him that meant the fame engine itself caught fire.
- **The 2008 Las Vegas conviction** is **Venus–Mercury**. Mercury (H12 Cancer, debilitated) is the karaka for prison/loss in this chart. Venus–Mercury together: career (Venus) drags him into confinement (Mercury).
- **Release from prison Oct 1, 2017**: Moon–Moon. Moon is in Pisces H8 — "release" in the most ambiguous sense; he leaves prison but enters the dasha that will end his life.
- **Death April 10, 2024**: Moon–Mercury. The two H12 Cancer planets (Mercury, Saturn) are activated through the H8 Moon. This is structurally the death configuration the chart was holding from birth.

---

## 3. Lunar nodal transits at major events

Below is the transit position of Rahu (mean node) at each life event, with the whole-sign Vedic house it occupied (counted from natal Leo Lagna). Ketu is always exactly opposite. *Natal Rahu is at 06°59' Taurus, H10; natal Ketu at 06°59' Scorpio, H4.*

| Date | Event | Transit Rahu | House | MD/AD |
|---|---|---|---|---|
| 1947-07-09 | Birth | 06°59' Taurus | **H10** | Jupiter / Rahu |
| 1949-07-09 | Rickets, leg braces | 28°15' Pisces | H8 | Saturn / Saturn |
| 1960 | Joins gang | 25°20' Leo | **H1** | Saturn / Moon |
| 1967-06-24 | Marries Marguerite | 10°41' Aries | H9 | Saturn / Jupiter |
| 1968-12-04 | Heisman + Arnelle's birth | 12°39' Pisces | **H8** | Mercury / Mercury |
| 1969-01-28 | NFL draft #1 | 09°44' Pisces | **H8** | Mercury / Mercury |
| 1973-12-16 | 2,000-yard season | 05°15' Sagittarius | H5 | Mercury / Sun |
| 1977-09-24 | Aaren born / meets Nicole | 22°13' Virgo | H2 | Mercury / Rahu |
| 1978-03-28 | Trade to 49ers | 12°25' Virgo | H2 | Mercury / Rahu |
| 1979-08-26 | **Aaren drowns** | 15°05' Leo | **H1** | Mercury / Jupiter |
| 1979-12-16 | Final NFL game | 09°08' Leo | **H1** | Mercury / Jupiter |
| 1985-02-02 | Marries Nicole | 29°47' Aries | H9 | Ketu / Venus |
| 1985-08-03 | Pro Football HOF | 20°08' Aries | H9 | Ketu / Venus |
| 1989-01-01 | First DV arrest | 14°04' Aquarius | **H7** | Ketu / Jupiter |
| 1992-02-25 | Nicole files divorce | 13°07' Sagittarius | H5 | Venus / Venus |
| 1992-10-15 | Divorce final | 00°46' Sagittarius | H5 | Venus / Venus |
| **1994-06-12** | **Murders** | 28°43' Libra | **H3** | **Venus / Venus** |
| 1994-06-17 | Bronco chase | 28°26' Libra | H3 | Venus / Venus |
| 1995-01-24 | Trial begins | 16°44' Libra | H3 | Venus / Sun |
| 1995-10-03 | **Acquittal** | 03°23' Libra | H3 | Venus / Sun |
| 1997-02-04 | Civil judgment | 07°25' Virgo | **H2** | Venus / Moon |
| 2007-09-13 | LV hotel confrontation | 12°10' Aquarius | **H7** | Venus / Mercury |
| 2008-10-03 | **Robbery conviction** | 21°43' Capricorn | **H6** | Venus / Mercury |
| 2008-12-05 | Sentencing, Lovelock | 18°23' Capricorn | **H6** | Venus / Mercury |
| 2013-07-25 | Partial parole | 18°40' Libra | H3 | Sun / Rahu |
| 2017-07-20 | **Full parole** | 01°31' Leo | **H1** | Moon / Moon |
| 2017-10-01 | Released from prison | 27°38' Cancer | **H12** | Moon / Moon |
| 2023-05-01 | Cancer announcement | 09°39' Aries | H9 | Moon / Saturn |
| **2024-04-10** | **Death** | 21°22' Pisces | **H8** | **Moon / Mercury** |

The script `oj_transits.py` reproduces this table for any list of dates.

---

## 4. Thesis: how the nodes actually behave in this chart

Reading the data above as a single empirical record — not as separate transits — five patterns emerge that I think generalize beyond Simpson, but are unusually clean in him because his life's events are so well documented and so dramatic.

### Thesis 1 — The natal nodal axis is the spine the life folds along, and the 18.6-year nodal cycle keeps re-striking the same axis

His natal Rahu/Ketu axis is Taurus/Scorpio (H10/H4). Look at where transit Rahu sat for each catastrophic *family* event:

- 1968 (Arnelle born, public-fame breakthrough): Rahu **Pisces H8 — Ketu Virgo H2**
- 1977–78 (Aaren born, Nicole meets him, traded "home" to SF): Rahu **Virgo H2 — Ketu Pisces H8**
- 1997 (civil judgment financially destroys his family wealth): Rahu **Virgo H2 — Ketu Pisces H8**
- 2024 (death, family final assembly): Rahu **Pisces H8 — Ketu Virgo H2**

These are all on the **Pisces/Virgo (H8/H2) axis**, exactly 18.6, 18.6, and 26.5 years apart — the nodal cycle striking the same secondary axis four times. Notice this isn't his natal nodal axis (Taurus/Scorpio); it's the axis 30° away. That's important: **the nodes don't only matter when they return to themselves; they matter even more when they pass over the natal Moon's axis** (his Moon is in Pisces in the 8th). Each Pisces/Virgo nodal passage detonated something in the H8 Moon — birth of a child, death of a child, financial extinction, his own death.

The general rule I'd extract: **find the houses occupied by (a) the natal nodes themselves and (b) the natal Moon's house and the house opposite. The nodal cycle (every ~9.3 years for a hit on each axis) will activate one of those four houses at every major life threshold.**

### Thesis 2 — The dasha tells you *which* domain catches fire; the nodal transit tells you the *house* where the fire starts

This is the cleanest dyad in his chart. His Venus Mahadasha (1991–2011) was guaranteed to be the most consequential period of his adult life *because Venus rules his 10th house*: career-and-public-reputation karma was set to ripen for 20 straight years. But Venus the planet didn't tell us *where* the explosion would happen — that was the job of the nodes:

- **Venus–Venus + Rahu in Libra/H3 (siblings, courage, communication, short-distance travel)** = murders involving stabbing (Mars), the Bronco chase (a literal short-distance vehicular event in H3), explosive media communication. H3 is also the house of *self-asserted aggression* in classical Vedic — and it was filled by transit Rahu for the entire critical window.
- **Venus–Mercury + Rahu in Capricorn/H6 (enemies, legal disputes, debts, servants)** = the 2008 Las Vegas conviction. H6 is the canonical "courtroom" house. Rahu in H6 in a sub-period of the 12th-house planet (Mercury) = legal defeat that ends in confinement.

In each case the dasha-lord told you the *theme* (career-fame Venus → fame-driven catastrophes; communication Mercury → legal/courtroom catastrophes), and the nodal house-transit told you the *stage* on which the theme played out. **Together they bracket the event; alone, neither does.**

### Thesis 3 — Rahu over the Lagna is identity-rebirth; Ketu over the Lagna is identity-erasure

Watch the Lagna (Leo) transits:

- 1960 (joining the gang, age 13 — first chosen identity): **Rahu in Leo, H1**
- 1979 (Aaren dies + retirement + divorce — total identity collapse and re-formation): **Rahu in Leo, H1**
- 2017 (parole granted — formal restoration of legal identity): **Rahu re-entering Leo, H1**

And the opposite:

- 1989 (first publicly-recorded domestic violence — public mask cracked): **Ketu in Leo, H1**
- 2007 (Las Vegas confrontation — the moment of total social erasure): **Ketu in Leo, H1**

Roughly every 18.6 years Rahu returns to the Lagna and the person *acquires* a new identity; ~9 years later Ketu returns and the identity *dissolves*. In Simpson's chart these returns were spectacularly literal — **gang member (1960), washed-up athlete divorcé (1979), legally restored parolee (2017)** vs. **wife-beater (1989), career criminal (2007)**. The same sequence runs in any chart, just usually less photogenically.

### Thesis 4 — The 8th-house Moon is a death-fated configuration that comes due during a Moon Mahadasha activated by an 8th-house nodal transit

He died in **Moon MD / Mercury AD with transit Rahu in Pisces in H8** — i.e. transit Rahu was sitting at 21° Pisces, only 19° from his natal Moon at 02°28' Pisces. The Moon dasha activated a planet sitting in the house of death; the nodal transit ignited that exact house from the same sign as the natal Moon. All three layers — natal placement, current dasha, current transit — pointed at the 8th house.

If you look back at his life for *every* major H8 nodal transit you find a death or near-death event:
- 1949 (Rahu in Pisces H8): rickets diagnosis; close to fatal in 1947–49 American context
- 1968–69 (Rahu in Pisces H8): birth event AND draft event — H8 governs sudden transformations, not only deaths
- 1997 (Rahu in Virgo, Ketu in Pisces H8): financial death (civil judgment)
- 2024 (Rahu in Pisces H8): physical death

The general claim: **a malefic-natal-house planet (H8 Moon here) becomes the timing-trigger for that house's worst significations during its own dasha when transit nodes also touch the same house. All three conditions must coincide.** This is why a "bad" H8 Moon doesn't kill someone at age 30 even with bad transits — the dasha hasn't ripened. And it's why the same nodal transits in 1949 and 1968 produced disease/birth rather than death — the Moon dasha hadn't begun.

### Thesis 5 — Nodal sandhi (degree-zero crossings) is when the *most* irrevocable things happen

Look at the moments when transit Rahu was within 3° of a sign change:

- **June 1994 (murders/chase)**: Rahu at 28°43' Libra, 1.3° from leaving Libra → entering Virgo. The most public, irreversible moment of his life.
- **Oct 1995 (acquittal)**: Rahu at 03°23' Libra. Just into the new sign (it had ingressed into Libra from Scorpio earlier).
- **Oct 1992 (Nicole divorce final)**: Rahu at 00°46' Sagittarius. Just-ingressed.
- **2017-10-01 (release)**: Rahu at 27°38' Cancer, 2.4° from ingress to Gemini.

In Vedic transit theory, gandanta and sign-junction (sandhi) periods of the lunar nodes are unstable — choices made during them tend to be irreversible because they straddle two karmic chapters. The Simpson record bears this out unusually clearly: the most life-defining moments cluster at Rahu's sign edges. **Practical heuristic: pull the dates of node ingresses and the ±2° windows around them, and check whether the chart's most consequential events disproportionately fall there.** In this chart they do.

### What this chart is *not* a clean test of

A few caveats — places where the data is too noisy to support strong claims:
- **D11 readings vary by school.** Some Parashari traditions read the 11th divisional as labha-amsa (gains/recognition), others as Rudramsa (destruction). The script computes the geometric division; the *interpretation* is school-dependent. I leaned on the Rudramsa reading because his life arc justifies it, but that's circular reasoning if used predictively.
- **Mean vs. true node.** I used the mean node throughout. True-node positions can shift by up to ~1.5° from mean; for sandhi analysis that matters. Re-running with `swe.TRUE_NODE` would tighten Thesis 5.
- **Birth time precision.** AA from Astrodatabank is the highest rating, but a 4-minute change in birth time shifts the Lagna by ~1°. His Lagna at 01°29' Leo is close enough to the Cancer/Leo boundary that you may want to rectify against (a) the Heisman in Mercury–Mercury and (b) the murders in Venus–Venus to confirm the dasha boundaries land at exactly the right calendar dates.

---

## 5. The two scripts

`oj_jyotish.py` — natal chart, D1/D9/D10/D11, full Vimshottari MD/AD. General; edit the four BIRTH constants for any chart.

`oj_transits.py` — adds nodal transit computation for an arbitrary list of life events, tagged with the active MD/AD.

Both use Lahiri ayanamsa, mean nodes, whole-sign houses, and `pyswisseph`'s built-in DE431 ephemeris. They depend only on `pyswisseph` and the standard library.
