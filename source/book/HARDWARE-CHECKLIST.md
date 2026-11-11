# MPC, Gently v3: hardware verification checklist

Every statement in the v3 draft is either documented in Akai's *MPC Sample User Guide* v1.3.0 (RevA), or marked in the text as unconfirmed. This list covers the unconfirmed ones, plus a few the book relies on that come from third parties. Test unit firmware: 1.3.0.12.

**Status key:** every item below is **Unconfirmed**. Nothing has been marked as passed, because no hardware results have been recorded yet. When you test one, write what you saw under "Result", change the status, and update the book.

**Safety rules for every test**

- Save your real work first. Then start each test with **SHIFT + PAD 16 › New Project**, so nothing you care about is loaded.
- Use factory sounds or a throwaway recording.
- Never use Reset Factory Data. None of these tests need it.
- If a test needs a microSD card, use a spare card, or one that's already backed up.

Page numbers refer to the v3 draft PDF (78 pages).

---

## 1. Where an audio export is saved, and how to get it off the MPC

- **Lesson and page:** L8 part D, p61 ("Where the file goes"); Your Sounds and Storage, p66–67.
- **Why it matters:** exporting is the final outcome of the course. The book can't yet tell readers where the file ends up, or how to copy it to a computer.
- **Test:**
  1. In a new project, load any factory kick onto pad A1.
  2. Record one bar into sequence 1.
  3. Open Song Mode (SHIFT + PAD 12) and add sequence 1 with B3.
  4. Export it as an audio mixdown (B1, then B2), named `TESTEXP1`, then press B3 (Do It!).
  5. Do this once with no microSD card in the slot, and once with a card in.
  6. After each export, open SAMPLE SELECT and look on both drives (B2 switches between them).
  7. Then use SD Card Access to look at the card on a computer.
- **Record:**
  - Any screen asking you to choose a destination.
  - Which drive and folder the file is on, and its name and file type.
  - Whether it shows up in SAMPLE SELECT.
  - Whether it can be copied to a computer at all when there's no card in.
- **Update once confirmed:** replace points 2 and 3 of the "Where the file goes" box on p61, and the "Exported audio" entry on p66–67, with the exact location and the steps to retrieve the file.

## 2. Switching 16 Levels off

- **Lesson and page:** L4 step 10, p34. Also troubleshooting, "plays at the wrong speed or pitch", p70.
- **Why it matters:** if 16 Levels stays on, every pad in that bank plays the same sound at a different pitch, and the bassline steps that follow stop working.
- **Test:**
  1. In a new project, load a sound onto pad B1.
  2. Press SHIFT + 16 LEVELS until the screen shows Tune.
  3. Press 16 LEVELS.
  4. Press 16 LEVELS again.
- **Record:** whether the button goes dark, whether the "16" icon disappears, and whether pads B2 to B16 go back to their own sounds (or to silence).
- **Update once confirmed:** step 10 on p34 (remove "Akai's guide doesn't describe switching it off"), and the About this book note on p78.

## 3. How far apart in pitch the 16 Levels pads are

- **Lesson and page:** L4 diagram and step 8, p31 and p33.
- **Why it matters:** the diagram now shows only what Akai documents (pad 4 plays the original pitch, lower pads are lower, higher pads are higher). If the spacing is confirmed, the diagram could teach semitones directly.
- **Test:**
  1. Load a clearly pitched sound, such as a sine or a held synth note.
  2. With 16 Levels on (Tune type), play pad 4 and then pad 16. Is pad 16 an octave above?
  3. Play pad 4 and then pad 5. Compare that step with a +1 Semi Tune copy of the sound on another pad.
- **Record:** the interval between neighbouring pads, and between pad 4 and pad 16. A tuner app on a phone helps.
- **Update once confirmed:** add the interval labels back to `levels_map()` in `svgs.py`, and update the caption on p31.

## 4. Knob FX: handing over the knobs versus bypassing the effect

- **Lesson and page:** L3 step 16 and the "Knobs changing the wrong thing?" box, p27–28; L8 step 11, p60; Quick Reference, p64; troubleshooting, p71.
- **Why it matters:** Akai documents KNOB FX as engaging and disengaging control of K1 to K3, and B3 in FX SELECT as Bypass. The guide doesn't say whether the effect is still heard while the KNOB FX button is dark. The book currently tells readers to listen, and to light KNOB FX if the reverb is missing.
- **Test:**
  1. Load a short snare onto pad A5.
  2. In FX SELECT, choose Reverb Large and make only pad 5 bright.
  3. Press KNOB FX so it lights, set Mix to maximum, then press KNOB FX again so it goes dark.
  4. Tap pad A5.
  5. Go back to FX SELECT, press B3, and tap pad A5 again.
- **Record:**
  - Whether the reverb is heard with KNOB FX dark.
  - What B3 shows on screen, and whether pressing it again un-bypasses the effect.
  - Whether the Bypass state is kept after saving and reloading the project.
- **Update once confirmed:** the box on p28, step 11 on p60, the Bypass row on p64, and the KNOB FX entry in the glossary (p76).

## 5. Whether RESAMPLE captures Knob FX

- **Lesson and page:** L5 steps 12–16, p42–43. Also the signal-flow diagram caption, p40.
- **Why it matters:** the printed echo in Lesson 5 is meant to sound the same as what the reader heard. If RESAMPLE records the sound dry, the reverb disappears from that sound.
- **Test:**
  1. In a new project, put a snare on pad A5, with Reverb Large on pad 5 and the Mix high.
  2. Record one hit into sequence 1.
  3. Use SHIFT + PAD 11 (RESAMPLE) to record it onto pad A9.
  4. Repeat with KNOB FX lit and with it dark.
  5. Also try Sample Record with Source set to Resample, and with Rec Input Effects set to On in INPUT CONFIG.
- **Record:** whether the reverb tail is in the resampled sound in each case.
- **Update once confirmed:** the signal-flow caption on p40, and the About this book note on p78.

## 6. Whether Undo restores an erased sequence

- **Lesson and page:** troubleshooting, "A recording changed a pattern you liked", p72.
- **Why it matters:** the book offers SHIFT + minus as a first attempt at recovery after erasing a sequence, and is careful not to promise it works.
- **Test:**
  1. In a new project, record a few hits into sequence 1.
  2. Press SEQ, hold ERASE and press pad 1.
  3. Press SHIFT + minus.
- **Record:** whether a confirmation screen appeared, and whether the sequence came back.
- **Update once confirmed:** fix point 3 on p72, and the Lesson 5 tidy-up step on p43 ("If the screen asks you to confirm").

## 7. Saving a project under a name that already exists

- **Lesson and page:** L2 Go Further, p22. This is why every extra save in the book uses a new name (GENTLY2B and so on).
- **Why it matters:** readers will try it. If the MPC silently overwrites, they could lose a lesson's copy.
- **Test:**
  1. In a new project, save it as `TESTSAVE`.
  2. Change something, then save as `TESTSAVE` again.
- **Record:**
  - Any warning, or a choice to replace the existing copy.
  - Whether a second copy was created, or a number added to the name.
  - What loads afterwards.
- **Update once confirmed:** the bracketed note on p22, and the Two routes section on p3 if the behaviour is safe.

## 8. Whether Sequence Mode shares the bank letter with Sample Mode

- **Lesson and page:** L4 "A house rule for banks", p35. The "light bank A" habit is used in every lesson from L4 onwards, for example L7 p54.
- **Why it matters:** the whole "press SEQ, light bank A, tap the sequence" routine assumes the bank letter can be different in Sequence Mode. If the MPC always uses bank A for sequences 1 to 16, the routine is harmless but longer than it needs to be.
- **Test:**
  1. In a new project, record a few hits into sequence 1.
  2. In Sample Mode, press PAD BANK until B is lit.
  3. Press SEQ. Note which bank letter is lit and which pads glow.
  4. Press PAD BANK in Sequence Mode.
- **Record:**
  - Whether the bank letter changes when you switch modes.
  - Whether sequence 1 still shows on pad 1.
  - What PAD BANK does in Sequence Mode (for example, sequences 17 to 32).
- **Update once confirmed:** the house-rule note on p35. The routine can stay, because it's safe either way.

## 9. Disarming recording when nothing is playing

- **Lesson and page:** the L7 carving routine, p54; Known State step 2, p65; the STOP control description, p52.
- **Why it matters:** Akai documents SEQ RECORD as arming recording, and pressing it again as stopping recording while playback continues. It doesn't describe disarming when nothing is playing. The book says to press STOP, and to press SEQ RECORD once if it's still flashing.
- **Test:**
  1. Press SEQ RECORD so it flashes, without pressing PLAY.
  2. Press STOP. Note whether it stops flashing.
  3. Arm again and press SEQ RECORD instead.
- **Record:** which button disarms it.
- **Update once confirmed:** simplify the wording on p54, p65 and p52 to the one button that works.

## 10. ERASE + pad while armed but stopped

- **Lesson and page:** the L7 carving routine, p54–55; L2 "Want to redo just one drum?", p21; troubleshooting, p73.
- **Why it matters:** Akai documents both of these:
  - With recording armed, ERASE + pad erases that pad's recorded events.
  - In Sample Mode, stopped, ERASE + pad erases the sample from the pad.

  The book's routine is "armed, not playing". This test confirms the routine removes hits and never the sound.
- **Test:**
  1. In a new project, record kick and snare into sequence 1.
  2. Press SEQ, then SEQ RECORD (flashing, no PLAY).
  3. Hold ERASE and tap the snare pad. Disarm.
  4. Play sequence 1, then press SAMPLE and tap the snare pad.
  5. Also try step 3 after pressing SAMPLE while still armed.
- **Record:**
  - Whether the snare hits are gone from the sequence.
  - Whether the snare sound is still on its pad.
  - Whether a confirmation screen appears.
- **Update once confirmed:** the warning boxes on p54 and p73, if the behaviour differs.

## 11. Whether recorded volume automation carries over into other sequences

- **Lesson and page:** L8 Go Further, "Fade the ending", p62.
- **Why it matters:** the fade is recorded into sequence 4 by turning the haze's Mix Volume down. If the final knob value sticks, the haze could stay quiet when other sequences play.
- **Test:**
  1. In a new project, record a sustained sound into sequences 1 and 2.
  2. Record a Volume fade on that pad into sequence 2, following the book's steps.
  3. Play sequence 1, then sequence 2, then sequence 1 again.
  4. Check the pad's Mix page value after each one.
  5. Then try SHIFT + minus, and the documented erase (hold ERASE, turn K1, press B3).
- **Record:** the pad's volume in sequence 1 before and after sequence 2 plays, and whether both undo and erase remove the automation.
- **Update once confirmed:** the closing check in the Go Further bullet on p62. Remove it if the fade doesn't carry over, or turn it into an instruction if it does.

## 12. Loading a factory kit with B3 (Load Kit)

- **Lesson and page:** Your Sounds and Storage, "Kits", p66.
- **Why it matters:** Akai says the ENCODER loads a kit with four default sequences, while B3 loads only the kit's samples. The guide doesn't say what happens to the current project's sequences.
- **Test:**
  1. In a new project, record something into sequence 1.
  2. Load Project › Kits, then load a kit with B3.
  3. Check sequence 1, and pads A1 to A16.
  4. Repeat in another new project using the ENCODER.
- **Record:** whether your sequence survives each method, and which pads are replaced.
- **Update once confirmed:** the Kits entry on p66.

## 13. Whether Load Project can open a project saved to the microSD card

- **Lesson and page:** troubleshooting, "A project wasn't saved as expected", p74.
- **Test:**
  1. Save a test project and choose the external drive, if Save Project offers a choice.
  2. Open Load Project and look under User and elsewhere.
- **Record:** whether a drive choice is offered, and where the project appears.
- **Update once confirmed:** point 3 of the fix on p74.

## 14. Greyed areas outside Start and End

- **Lesson and page:** troubleshooting, "Parts of my waveform are greyed out", p69.
- **Status:** reported by a beginner on firmware 1.3.0.12. Akai's guide documents only the whole-waveform grey of a muted sample.
- **Test:**
  1. Load a sound and move Start and End inwards on the Trim page.
  2. Photograph the screen.
  3. Move Start fully down and End fully up.
- **Record:** how the excluded part is drawn, and whether turning K1 fully down and K2 fully up restores the full range.
- **Update once confirmed:** the entry on p69, if the wording or the fix differs.

## 15. Whether Semi Tune also changes a sound's length

- **Lesson and page:** L4 "Pitch and length are different things", p31.
- **Test:**
  1. Load a sound with a clear ending.
  2. Copy it to a second pad and set that copy's Semi Tune to −12.
  3. Compare how long each copy lasts, with Warp Off.
- **Record:** whether the −12 copy lasts longer.
- **Update once confirmed:** the last two sentences of that paragraph on p31.

## 16. Factory folder names

- **Lesson and page:** L2 step 5, p19; L3 step 2, p26; L4 step 2, p32; L5 step 2, p41.
- **Status:** only "Snares" is named in Akai's guide.
- **Test:** in SAMPLE SELECT, write down the top-level folder names.
- **Record:** the folder list, including whether there are kick, bass and sustained or pad folders.
- **Update once confirmed:** name the folders in those steps.

## 17. Note Repeat lengths and pad pressure

- **Lesson and page:** L2 step 19, p20; L7 step 9, p55.
- **Test:**
  1. Arm recording and press NOTE REPEAT.
  2. Read the B1 to B3 labels.
  3. Hold a pad, pressing harder and softer.
- **Record:** which note lengths are offered, and whether volume follows pressure.
- **Update once confirmed:** steps 19 (p20) and 9 (p55).

## 18. The prompt when loading a project

- **Lesson and page:** L1 step 22, p13; troubleshooting, "You want an earlier version back", p75; Known State step 9, p65.
- **Test:**
  1. Make a change to a project without saving it.
  2. Choose Load Project and pick another project.
- **Record:**
  - Whether a prompt appears, and its wording.
  - What B1 and B3 do.
  - Whether B1 returns you to the Project menu so you can save first.
- **Update once confirmed:** those three places.

## 19. Background saving

- **Lesson and page:** L1 "How saving works", p13; Your Sounds and Storage, "Background saving", p67.
- **Status:** documented by Akai ("your progress is saved in the background"). This test checks exactly what comes back.
- **Test:**
  1. In a new project, record something, but don't save a named copy.
  2. Switch off and on.
- **Record:** whether the unsaved recording returns.
- **Update once confirmed:** add one sentence to p13 if the behaviour is clear.

---

## Claims from third parties, not Akai

These are not equivalent to the official guide. The book either avoids relying on them or labels them.

- **"A computer can't reach the internal drive"** (mpc-samples.com). The book now says only that Akai describes computer access for the microSD card. See test 1.
- **"Sample packs need firmware 1.2.1 or later"** (mpc-samples.com). This is labelled as a third-party report on p67.
- **The Project menu item is labelled "SD Card Access."** Akai's guide uses the name "SD Card Access Mode". Check the exact on-screen wording during test 1.

## Pacing

These are estimates. Time a reader working through each lesson for the first time, without rushing.

| Lesson | Estimate in v3 | Measured |
|---|---|---|
| 1 | 15 to 20 min | |
| 2 | 20 to 25 min | |
| 3 | 15 to 20 min | |
| 4 | 20 min | |
| 5 | 20 min | |
| 6 | 25 min | |
| 7 | 25 to 30 min | |
| 8 | 20 to 25 min | |
| Each Go Further | 10 to 20 min | |
