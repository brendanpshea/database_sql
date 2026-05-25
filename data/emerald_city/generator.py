"""Emerald City Clinic data generator.

Produces a deterministic set of source files used by Chapter 12:
- patients.csv         — Scarecrow's records team export
- labs.json            — Tin Man's lab results
- charts.xml           — the Wizard's old chart system
- pharmacy_stream.txt  — a streaming pharmacy refill feed (one JSON object per line)
- partner_directory.html — a small HTML page for the web-scraping example
- soap_response.xml    — a tiny SOAP-style response for the network-protocol example

Run from the chapter notebook with:

    from generator import generate
    generate(out_dir='emerald_city_data', seed=137)

The seed makes the row counts and values reproducible, so quizzes and
auto-graders can reference specific records.
"""
from __future__ import annotations

import csv
import json
import random
import textwrap
from pathlib import Path


FIRST_NAMES = [
    "Dorothy", "Toto", "Glinda", "Aunt Em", "Uncle Henry",
    "Boq", "Nessa", "Fiyero", "Ozma", "Tip",
    "Polychrome", "Jack", "Mombi", "Jinjur", "Trot",
]
LAST_NAMES = [
    "Gale", "Quadling", "Munchkin", "Gillikin", "Winkie",
    "Emerald", "Lurline", "Pingaree", "Pumperdink",
]
TOWNS = ["Munchkinland", "Quadling Country", "Winkie Country", "Gillikin Country", "Emerald City"]
LAB_PANELS = ["CBC", "BMP", "CMP", "Lipid Panel", "TSH", "HbA1c", "Urinalysis"]
LAB_FLAGS = ["normal", "normal", "normal", "high", "low"]
CHART_DEPTS = ["Cardiology", "Endocrinology", "Pulmonology", "Family Medicine"]
PHARMACY_DRUGS = [
    ("Lisinopril 10mg", 30),
    ("Metformin 500mg", 60),
    ("Atorvastatin 20mg", 30),
    ("Levothyroxine 50mcg", 30),
    ("Amoxicillin 500mg", 21),
]


def _patients(rng: random.Random, n: int = 25):
    rows = []
    for i in range(1, n + 1):
        first = rng.choice(FIRST_NAMES)
        last = rng.choice(LAST_NAMES)
        rows.append({
            "patient_id": f"ECC{i:04d}",
            "first_name": first,
            "last_name": last,
            "date_of_birth": f"{rng.randint(1935, 2020):04d}-{rng.randint(1,12):02d}-{rng.randint(1,28):02d}",
            "town": rng.choice(TOWNS),
            "primary_provider": f"Dr. {rng.choice(LAST_NAMES)}",
        })
    return rows


def _labs(rng: random.Random, patients):
    results = []
    for p in patients:
        for _ in range(rng.randint(0, 3)):
            results.append({
                "lab_id": f"LAB{len(results) + 1:05d}",
                "patient_id": p["patient_id"],
                "panel": rng.choice(LAB_PANELS),
                "collected_on": f"2026-{rng.randint(1,5):02d}-{rng.randint(1,28):02d}",
                "result_flag": rng.choice(LAB_FLAGS),
                "ordering_provider": p["primary_provider"],
            })
    return results


def _charts_xml(rng: random.Random, patients) -> str:
    parts = ["<charts>"]
    for p in patients[:10]:  # only the first ten have legacy charts
        parts.append(f'  <chart patient_id="{p["patient_id"]}">')
        parts.append(f'    <opened_on>{rng.randint(2010, 2024)}-0{rng.randint(1,9)}-1{rng.randint(0,9)}</opened_on>')
        parts.append(f'    <department>{rng.choice(CHART_DEPTS)}</department>')
        parts.append(f'    <note>Legacy chart imported from the Wizard system.</note>')
        parts.append('  </chart>')
    parts.append("</charts>")
    return "\n".join(parts)


def _pharmacy_stream(rng: random.Random, patients):
    """Returns a list of JSON-encoded strings, one per refill event."""
    events = []
    for _ in range(40):
        patient = rng.choice(patients)
        drug, days = rng.choice(PHARMACY_DRUGS)
        events.append(json.dumps({
            "event_id": f"PH{len(events) + 1:05d}",
            "patient_id": patient["patient_id"],
            "drug": drug,
            "days_supply": days,
            "filled_on": f"2026-05-{rng.randint(1,24):02d}",
        }))
    return events


def _partner_directory_html() -> str:
    return textwrap.dedent("""\
        <!doctype html>
        <html>
          <head><title>Emerald City Clinic Partner Directory</title></head>
          <body>
            <h1>Partner Directory</h1>
            <table id="partners">
              <thead><tr><th>Partner</th><th>Specialty</th><th>Phone</th></tr></thead>
              <tbody>
                <tr><td>Tin Man Diagnostics</td><td>Lab</td><td>555-0101</td></tr>
                <tr><td>Scarecrow Records</td><td>Records</td><td>555-0102</td></tr>
                <tr><td>Lion Security</td><td>Compliance</td><td>555-0103</td></tr>
                <tr><td>Glinda Analytics</td><td>Analytics</td><td>555-0104</td></tr>
              </tbody>
            </table>
          </body>
        </html>
    """)


def _soap_response() -> str:
    return textwrap.dedent("""\
        <?xml version="1.0"?>
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
            <GetClinicHoursResponse>
              <Hours>
                <Day>Monday</Day>
                <Open>08:00</Open>
                <Close>17:00</Close>
              </Hours>
              <Hours>
                <Day>Saturday</Day>
                <Open>09:00</Open>
                <Close>13:00</Close>
              </Hours>
            </GetClinicHoursResponse>
          </soap:Body>
        </soap:Envelope>
    """)


def generate(out_dir: str | Path = "emerald_city_data", seed: int = 137) -> Path:
    """Write all source files to ``out_dir`` and return its path."""
    rng = random.Random(seed)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    patients = _patients(rng)
    labs = _labs(rng, patients)
    pharmacy = _pharmacy_stream(rng, patients)

    # patients.csv
    with (out / "patients.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(patients[0].keys()))
        writer.writeheader()
        writer.writerows(patients)

    # labs.json
    (out / "labs.json").write_text(json.dumps(labs, indent=2), encoding="utf-8")

    # charts.xml (the Wizard's legacy system)
    (out / "charts.xml").write_text(_charts_xml(rng, patients), encoding="utf-8")

    # pharmacy_stream.txt — one JSON object per line, for the streaming example
    (out / "pharmacy_stream.txt").write_text("\n".join(pharmacy) + "\n", encoding="utf-8")

    # partner_directory.html — for the scraping example
    (out / "partner_directory.html").write_text(_partner_directory_html(), encoding="utf-8")

    # soap_response.xml — for the network-protocol example
    (out / "soap_response.xml").write_text(_soap_response(), encoding="utf-8")

    return out


if __name__ == "__main__":
    path = generate()
    print(f"Wrote source files to {path.resolve()}")
