import pathlib

VOW = ("I promise to love you through every firmware update — and if my heart "
       "ever bricks, I'll restore from the backup where I first said yes.")

pathlib.Path("/output").mkdir(parents=True, exist_ok=True)
(pathlib.Path("/output") / "entry.txt").write_text(VOW, encoding="utf-8")
