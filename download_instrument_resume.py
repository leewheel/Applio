# -*- coding: utf-8 -*-
"""Resume: download remaining instrument models (12-35)."""
import os, sys, time
now_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, now_dir)
os.chdir(now_dir)
from rvc.lib.tools.model_download import model_download_pipeline

BASE_MISC = "https://huggingface.co/RegalHyperus/MiscellaneousRVCModels/resolve/main"
BASE_DRUM = "https://huggingface.co/RegalHyperus/DrumKitRVCModels/resolve/main"

# SKIP already downloaded first 11, resume from Trumpet onwards
MODELS = [
    ("Instrument-Trumpet",             f"{BASE_MISC}/Trumpet.zip"),
    ("Instrument-Trumpet2",            f"{BASE_MISC}/Trumpet2V2.zip"),
    ("Instrument-Trumpet-Mariachi",    f"{BASE_MISC}/MariachiTrumpet.zip"),
    ("Instrument-Trumpet-Tube",        f"{BASE_MISC}/TubeTrumpet.zip"),
    ("Instrument-Trumpet-Totsugeki",   f"{BASE_MISC}/TotsugekiHumanThemeTrumpet.zip"),
    ("Instrument-Bugle",               f"{BASE_MISC}/FamilyGuyBugle.zip"),
    ("Instrument-Tuba",                f"{BASE_MISC}/FyatTuba.zip"),
    ("Instrument-Saxophone",           "https://huggingface.co/Neyto/NeytoModels/resolve/main/SaxophoneChihuahua.zip"),
    ("Instrument-Zunpet",              f"{BASE_MISC}/Zunpet.zip"),
    ("Instrument-Glissotar",           f"{BASE_MISC}/Glissotar.zip"),

    # === Drums ===
    ("Drums-CarelessWhisper", f"{BASE_DRUM}/CarelessWhisperDrums.zip"),
    ("Drums-BillieJean",      f"{BASE_DRUM}/BillieJeanDrums.zip"),
    ("Drums-Bohemian",        f"{BASE_DRUM}/BohemianRhapsodyDrums.zip"),
    ("Drums-Thriller",        f"{BASE_DRUM}/ThrillerDrums.zip"),
    ("Drums-SmoothCriminal",  f"{BASE_DRUM}/SmoothCriminalDrums.zip"),
    ("Drums-Whistle",         f"{BASE_DRUM}/WhistleJoelMerryCoverDrums.zip"),
    ("Drums-Houdini",         f"{BASE_DRUM}/HoudiniDrums.zip"),
    ("Drums-APT",             f"{BASE_DRUM}/APTDrums.zip"),
    ("Drums-BlingBangBorn",   f"{BASE_DRUM}/BlingBangBangBornDrums.zip"),
    ("Drums-Radioactive",     f"{BASE_DRUM}/RadioactiveDrums.zip"),

    # === SFX ===
    ("SFX-Tornado",           f"{BASE_MISC}/Tornado.zip"),
    ("SFX-WTFBoom",           f"{BASE_MISC}/WTFBoom.zip"),

    # === Whisper / Whistle ===
    ("Whisper-Kinito",        "https://huggingface.co/Timur04129/Kinito-Whispering/resolve/main/Kinito%20(Whispering).zip"),
    ("Whistle-KiteTenjo",     "https://huggingface.co/SileExNT/KiteTenjoWhistle/resolve/main/KiteTenjoWhistle.zip"),
]

def download_all():
    total = len(MODELS)
    ok = fail = 0
    failed = []
    print(f"\n{'='*60}")
    print(f"  RESUME: INSTRUMENT MODELS {total} remaining")
    print(f"{'='*60}\n")

    for idx, (name, url) in enumerate(MODELS, 1):
        print(f"[{idx}/{total}] {name}")
        try:
            result = model_download_pipeline(url)
            if result and result != "Error":
                ok += 1
                print(f"  [OK]")
            else:
                fail += 1
                failed.append(name)
                print(f"  [FAIL]")
        except Exception as e:
            fail += 1
            failed.append(name)
            print(f"  [FAIL] {str(e)[:80]}")
        time.sleep(0.2)

    print(f"\n{'='*60}")
    print(f"  DONE: {ok}/{total} success, {fail}/{total} failed")
    if failed: print(f"  Failed: {', '.join(failed)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    download_all()
