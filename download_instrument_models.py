# -*- coding: utf-8 -*-
"""Download instrument-only RVC models."""
import os, sys, time
now_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, now_dir)
os.chdir(now_dir)
from rvc.lib.tools.model_download import model_download_pipeline

BASE_MISC = "https://huggingface.co/RegalHyperus/MiscellaneousRVCModels/resolve/main"
BASE_DRUM = "https://huggingface.co/RegalHyperus/DrumKitRVCModels/resolve/main"

MODELS = [
    # === String Instruments ===
    ("Instrument-Violin",              "https://huggingface.co/0x3e9/0x3e9_RVC_models/resolve/main/violin.zip"),
    ("Instrument-Guitar",              "https://huggingface.co/0x3e9/0x3e9_RVC_models/resolve/main/guitar.zip"),
    ("Instrument-Erhu",                f"{BASE_MISC}/Erhu.zip"),
    ("Instrument-GuitarSolo-V2",       f"{BASE_MISC}/BohemianRhapsodyGuitarSoloV2.zip"),
    ("Instrument-GuitarSolo-Stairway", f"{BASE_MISC}/StairwayToHeavenGuitarSolo.zip"),
    ("Instrument-Guitar-Electric",     f"{BASE_MISC}/DumbestGirlAliveElectricGuitar.zip"),
    ("Instrument-Guitar-Shred",        f"{BASE_MISC}/StratenMarshallKieselHD6Shred.zip"),
    ("Instrument-Bass-Brodyquest",     f"{BASE_MISC}/BrodyquestBass.zip"),
    ("Instrument-Bass-GoyangUbur",     f"{BASE_MISC}/GoyangUburUburBass.zip"),
    ("Instrument-Bass-Haruhayuku",     f"{BASE_MISC}/HaruhayukuBass.zip"),

    # === Wind Instruments ===
    ("Instrument-Flute",               f"{BASE_MISC}/Flute.zip"),
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
    ("SFX-Tornado",          f"{BASE_MISC}/Tornado.zip"),
    ("SFX-WTFBoom",          f"{BASE_MISC}/WTFBoom.zip"),

    # === Whisper / Whistle ===
    ("Whisper-Kinito",       "https://huggingface.co/Timur04129/Kinito-Whispering/resolve/main/Kinito%20(Whispering).zip"),
    ("Whistle-KiteTenjo",    "https://huggingface.co/SileExNT/KiteTenjoWhistle/resolve/main/KiteTenjoWhistle.zip"),
]

def download_all():
    total = len(MODELS)
    ok = fail = 0
    failed = []
    print(f"\n{'='*60}")
    print(f"  INSTRUMENT RVC MODELS - {total} models")
    print(f"  Strings: 10 | Winds: 11 | Drums: 10 | SFX: 2 | Whisper: 2")
    print(f"{'='*60}\n")

    for idx, (name, url) in enumerate(MODELS, 1):
        print(f"[{idx}/{total}] {name}")
        try:
            result = model_download_pipeline(url)
            if result and result != "Error":
                pth, idx_files = result
                print(f"  [OK]")
                ok += 1
            else:
                print(f"  [FAIL]")
                fail += 1
                failed.append(name)
        except Exception as e:
            print(f"  [FAIL] {str(e)[:80]}")
            fail += 1
            failed.append(name)
        time.sleep(0.2)

    print(f"\n{'='*60}")
    print(f"  DONE: {ok}/{total} success, {fail}/{total} failed")
    if failed:
        print(f"  Failed: {', '.join(failed)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    download_all()
