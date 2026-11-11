# MPC, Gently: revision 2 (November 2026)

Targeted technical revision of the 60-page first edition. 61 pages. Same design, page size, structure, voice, HELLO1 and GENTLY2 to GENTLY8.

## Navigation and state
- All Sample Mode page moves now read "Press B1/B2/B3 until <page> appears" (L3 p23-24, L4 p29, L5 p36-37, L6 p42, L8 p51). No fixed press counts remain.
- "Before you start" state checks added to L3 to L8 (project loaded, KNOB FX dark, SEQ RECORD not armed, 16 Levels/Note Repeat dark where relevant).
- L2 p18: tempo mode set to GBL so all sequences share 84 BPM; noted that quantise, metronome and count-in stay set.

## Knob FX (L3 p23-24, L5, L8, quick reference)
- Rewritten per the Knob FX page of the User Guide as five separate actions: open FX SELECT (SHIFT+KNOB FX), choose effect (ENCODER), choose pads (tap; B2 = all pads), engage KNOB FX and adjust K1-K3, disengage.
- Standard warning added: "Before editing sample settings, check KNOB FX. If it is lit, press it to disengage it."
- L8 p53: KNOB FX re-engaged before playing the finished song.

## Resampling (L5 p37)
- Tape Delay resample replaced. Akai does not document whether RESAMPLE captures Knob FX, or whether Rec Input Effects applies to it. New exercise: play a hand-made echo (four fading hits) in a helper sequence, resample with SHIFT+PAD 11, normalise, reverse. Uses only documented steps. Knob FX printing moved to an optional, clearly labelled experiment.
- Helper sequence 15 erased afterwards so it never reaches Song Mode.

## 16 Levels and bassline (L4 p27-30)
- Akai confirms only that pad 4 is original pitch. Diagram relabelled as conditional ("IF one semitone per pad... not yet confirmed").
- Bass now recorded from three normal pads tuned with Semi Tune (B1 0, B2 +3, B3 -2), which Akai documents in semitones, in Mute Group 1. 16 Levels kept for ear exploration only and switched off before recording, so playback never depends on undocumented 16 Levels recording behaviour.
- Bassline diagram updated to B1/B2/B3. L7 erase steps updated to all three bass pads. Where Next scale tip uses Semi Tune.

## Recording and backups
- Sequence-16 safety copies removed (L3, L4, L6). Overdub described as Akai documents it; UNDO (SHIFT + minus) offered for a bad take. Saving a new project each lesson kept.

## Educational edits
- Welcome p3 and L1 p9: Lesson 1 is an exploration; Lessons 2 to 8 build the original track.
- L2 p14: "This project uses four beats per bar", not "beats come in groups of four".
- L3 p23: what makes a good atmospheric source (length, sustain or natural decay, clear pitch, enough body) plus a crash/ride cymbal fallback; short drum hits discouraged.
- L5 p32: waveform pitch applies to pitched, periodic sounds only (text and caption).
- L7 p48: "rising" removed; optional firmer-press crescendo flagged as untested.
- L8 p50-52: compressor made optional and framed as a finishing touch.

## Visual
- p5: hardware overview enlarged to near full page width.
- Lesson panels: wider (60%), larger button, pad and knob labels; highlights matched to each control list (L1 adds B3; L2 adds B2, ERASE, PAD 14; L4, L5, L7, L8 revised to the new procedures).
- Control lists set inline beside panels; long two-control labels no longer overlap.
- Glossary: Resample definition no longer claims effects are captured.

## Still to verify on hardware
See "About this book" (p61) and the summary delivered with this revision.

# Revision 3 (November 2026)
- p29, L4 step 5: octave test reworded. An octave on pad 16 is consistent with the semitone layout but does not prove every pad between; explore by ear; the bassline uses independently tuned pads. Diagram unchanged.
- p48, L7: optional "Your swell in the Break" box. Records pad C3 into sequence 3 (bank A to select, bank C to play) on the one of bars 1 and 3, using only the select, SEQ RECORD, PAD BANK, PLAY and UNDO steps already used in the book. Sequence stays 4 bars, so the song is still about 80 seconds. Arrangement diagrams unchanged.
- p59-60, glossary: Bar and Waveform definitions corrected.

# v0.9.0-preview public release (November 2026)
- p61, About this book: first paragraph reworded for public release (author, independence, licence, Akai artwork, repository link).
- PDF author metadata set to slowphase.

# v3 draft (November 2026)

An editorial, teaching and technical revision of the published v0.9.0-preview edition (called "v2" in the briefs), followed by a final correction pass. 78 pages, up from 61. Same page size, typography, illustrations, eight lessons, project names, 84 BPM and the 80-second track. Primary reference: Akai *MPC Sample User Guide* v1.3.0 (RevA). Page numbers below are for the current v3 draft.

## Release-candidate fixes (11 November 2026)
- **L2 Go Further, p21–22, "Three ways to feel the same beat".**
  - Sequences 9, 10 and 11 now each follow the same pattern:
    1. Press SEQ, light bank A and tap the sequence.
    2. Press SEQ RECORD.
    3. For 10 and 11, erase the snare (A2) or hats (A3) with bank A lit, before pressing PLAY.
    4. Play.
    5. End with SEQ RECORD, then STOP.
  - Sequence 11 also reminds readers to switch NOTE REPEAT off.
  - Checked against the guide: p41 (arming and erasing while armed), p18 (SEQ RECORD again stops recording while playback continues) and p23 (STOP). The creative outcomes are unchanged.
- **Meet the MPC Sample, p6, "Around the edges".** "AUDIO IN / OUT ... not needed in this book" is now two entries:
  - AUDIO OUT, for powered monitors or other suitable audio equipment.
  - AUDIO IN, for recording external sources, with REC GAIN setting the incoming level. It's marked optional, because the book uses the built-in microphone.
- **Proposed README:** "eight relaxed evenings" is now "eight approachable lessons". Release URLs and version labels are unchanged.
- No other pages changed. A page-by-page comparison with the previous draft shows differences on pp. 6, 21 and 22 only.

## Final correction pass

### Critical errors corrected
- **L7, p53 to 55: sequence workflow.** Every section (Intro 2, Break 3, Outro 4, Lift 5) now starts from the top: press SEQ, light bank A, tap the sequence, arm SEQ RECORD, choose the bank, erase, then disarm. Nothing relies on the previous step's selection. The snare-roll step reselects sequence 5 explicitly, because the optional swell changes the selection. Erasing was checked against the guide (p18 and p41: with recording armed, ERASE + pad erases that pad's events from the current sequence).
- **L7, p55: arrangement.** The written order now matches the diagram, Song Mode and the final track: Intro, Main, Main, Break, Lift, Main, Outro (sequences 2, 1, 1, 3, 5, 1, 4). In the live run-through, Main is allowed to loop twice instead of being queued onto itself. The duplicate arrangement diagram was removed from L7; L8 keeps it (p60).
- **L7, p53:** the copy step now checks that pads 2 to 5 are dim first, and a warning separates erasing hits (armed) from erasing the sound itself (Sample Mode, stopped, not armed).

### Go Further routes and sequence slots
- **Welcome, p3: "Two routes".** The guided route continues from GENTLYn; the creative route continues from GENTLYnB. Every "Starts from" line and "Before you start" note now names both. Every Go Further ends by saving a B copy (L2 to L8).
- **L2, p21: sequence slots.**
  - 1 to 5: the track.
  - 6: L8's backup.
  - 9 to 11: L2's Go Further.
  - 12 to 14: L4's Go Further.
  - 15: L5's temporary helper.
  - 16: L7's Hold section.

  Every use first checks that the pad is dim; L5 and L7 offer a fallback slot.
- **L4 Go Further, p36:** no longer copies a variation onto sequence 1. What happens when copying onto a sequence that already has hits isn't documented, and the troubleshooting advice now copies only to a dim sequence (p71).
- Challenges that change shared material now say so: L3 (the reverb's pad list is shared), L6 (the winner is recorded into sequence 1), L7 (mutes are cleared before saving). L7's carving steps tell creative-route readers to erase their extra pads too.

### Teaching improvements
- **L4, p33: "Do these sounds belong together?"** A three-step listening check of haze against bass, tuning B1 by ear. B2 and B3 are now set relative to B1 (3 above, 2 below), with a small table, so the Night Walk shape survives any change to the home note (p34). The B4 challenge and the bass-pattern caption are relative too.
- **L4, p31: 16 Levels diagram.** It now shows only what's documented: pad 4 is the original pitch, lower pads are lower, higher pads are higher. No semitone values. The listening step no longer depends on an octave test.
- **L6, p48:** five mug taps, matching the chop diagram. The caption and step 13 say threshold chopping won't always find exactly five.
- **L8 Go Further, p62: fade automation, rewritten.** Select the Outro, arm, press SAMPLE (recording stays armed), select the haze without triggering it (hold SAMPLE + pad, guide p24), open Mix, play, and turn K1. Undo with SHIFT + minus; erase with ERASE + K1, then B3 (guide p19 and p41–42). It ends with a check that the fade hasn't carried into sequence 1.
- **Lesson times** now vary by lesson: L1 15 to 20, L2 20 to 25, L3 15 to 20, L4 20, L5 20, L6 25, L7 25 to 30, L8 20 to 25 minutes.
- **Equipment:** "IEMs" replaced by headphones or monitors throughout, with hearing-protection advice kept. L6 warns about mic pickup from monitors.

### Technical documentation corrections
- **Mute.** The guide (p31 and p34) says MUTE works in any mode. The earlier changelog line saying it "only works in Sample Mode" was wrong and has been removed. The book still presses SAMPLE first, as a habit, and the Quick Reference says "works in any mode" (p64).
- **Knob FX** (L3 p25 and p27–28, L8 p58 and p60, Meet p7, Quick Reference p64, troubleshooting p71, glossary p76). The book now separates three things:
  - Choosing the effect and pads (FX SELECT).
  - Handing K1 to K3 to it (KNOB FX).
  - Bypassing it (B3 in FX SELECT, guide p51).

  L8 no longer tells readers to light KNOB FX before playing the song. It says to check FX SELECT and Bypass first, and to light KNOB FX only if the reverb is still dry.
- **Import formats, p67.** Replaced "not documented" with the guide's list: WAV, MP3, AIF/AIFF, SND, S1S, S3S, FLAC and OGG, at 16 or 24 bit and 44.1, 48 or 96 kHz. WAV is recommended for sample packs.
- **Export and storage, p61 and p66–67.** Exporting (documented) is kept separate from where the file is stored (undocumented) and from copying it to a computer (SD Card Access, card only). Inserting a card is no longer implied to decide where the file goes. "A computer can't reach the internal drive" is now "Akai describes computer access only for the microSD card".
- **Kits, p66.** New entry: the ENCODER loads a kit with four default sequences; B3 loads only its samples (guide p62). Also added to the glossary.
- **Saving, p13 and p67.** These pages now separate:
  - The working project, which Akai says is saved in the background.
  - A named copy (Save Project).
  - A saved sample (Save Sample).
  - What New Project and Load Project replace.

  The claims that work is "never overwritten" or safe through any power-off were removed.

### Troubleshooting and reference
- **When Things Go Wrong, p68:** new navigation table, grouped by problem, with page numbers.
- **Grey waveforms, p69,** split into two entries: "Parts of my waveform are greyed out" (Start/End, cross-referenced to L5's cuts table) and "My entire waveform is grey and the pad is silent" (mute, as documented).
- The "Internal or microSD" entry was folded into the storage page link.
- **Destructive steps reviewed:**
  - Loading an earlier copy warns that unsaved work is lost, and how to keep it (p65 and p75).
  - Erasing hits is distinguished from erasing a sound (p63, p73).
  - Disarming falls back to pressing SEQ RECORD once if STOP doesn't disarm.
- **Known State, p65:** steps 1 to 8 are described as changing no sound or sequence; step 9 is marked in orange, "This one can lose work".
- **Quick Reference, p63 to 64:** added knob-move recording and erasing, Knob FX Bypass, and Mute. Clarified both erase rows. The Fader row was dropped; it's still covered in troubleshooting (p70).

### Cover
- New cover: a line-art technical drawing of the top panel, in the style of the GitHub hero, bleeding off the top right with orange leader lines. Akai logo top left; the MPC Sample wordmark moved below the stripes. Panel labels are limited to those printed on the MPC and used elsewhere in the book.

## First v3 revision (before the final pass)
- Cover footer "Eight lessons. One complete track."; "Have a Play" became **Go Further**.
- L1: "Five words worth knowing" diagram, modes, and "Prove it's safe" (save and reload).
- L2: jamming versus recording, the recording workflow diagram, what quantising does and doesn't do.
- L3: length, overlap, One Shot versus Note On, Mono versus Poly.
- L4: "Pitch and length are different things" (Warp).
- L5: "Five ways to cut a sound" table.
- L6: recording sources, levels, monitoring and keeping recordings.
- L7: samples versus sequences versus arrangement.
- L8: audio export as the final step.
- New reference sections: Getting Back to a Known State, and Your Sounds and Storage. Troubleshooting rebuilt around Symptom, Cause, Fix and Prevention. Glossary additions: Arm, Extract, Mute Group, Note On / One Shot, Time Stretch.

## Build
- svgs.py:
  - New `cover_blueprint()`.
  - `levels_map()` rewritten without interval values.
  - Earlier v3 figures: `five_words_fig`, `record_flow_fig`, `storage_fig`.
- build.py registers `cover_blueprint`.
- style.css:
  - IBM Plex Mono for the cover drawing.
  - Troubleshooting navigation table and tuning table.
  - Compact Welcome callouts.
