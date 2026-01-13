## Dataset Structure

This dataset is organized into **five thematic pillars**, each representing a different emotional depth and conversational complexity commonly observed among Indian youth. The design intentionally progresses from everyday stressors to high-risk, safety-critical conversations.

Total dataset size: **5,000 conversations**

---

##  Pillar 1 — The Daily Grind (1,500 entries)

**Focus:** Everyday academic and career-related stressors expressed in simple emotional language.

### Emotions Covered (6)

* Academic stress
* Exam panic
* Burnout
* Fear of future
* Family pressure
* Career confusion

### Conversation Style

* **70%** Single-turn (User → Assistant)
* **30%** Multi-turn (2 turns: User → Assistant → User → Assistant)

### Distribution

| Emotion          | Entries | Turn Type   |
| ---------------- | ------- | ----------- |
| Academic stress  | 400     | Single-turn |
| Exam panic       | 300     | Mixed       |
| Burnout          | 250     | Mixed       |
| Fear of future   | 200     | Single-turn |
| Career confusion | 200     | Multi-turn  |
| Family pressure  | 150     | Multi-turn  |

---

##  Pillar 2 — Heart & Social (1,250 entries)

**Focus:** Interpersonal relationships, social exclusion, and emotional vulnerability.

### Emotions Covered (7)

* Breakup pain
* One-sided love
* Relationship confusion
* Friendship betrayal
* Feeling left out
* Loneliness
* Jealousy / FOMO

### Conversation Style

* **50%** Single-turn
* **40%** Multi-turn (2 turns)
* **10%** Multi-turn (3 turns)

### Distribution

| Emotion                | Entries | Turn Type        |
| ---------------------- | ------- | ---------------- |
| Breakup pain           | 350     | Multi-turn heavy |
| One-sided love         | 200     | Mixed            |
| Relationship confusion | 200     | Mixed            |
| Friendship betrayal    | 150     | 2-turn           |
| Feeling left out       | 150     | Mixed            |
| Loneliness             | 150     | Single-turn      |
| Jealousy / FOMO        | 50      | Deep multi-turn  |

---

## Pillar 3 — The Inner Critic (1,000 entries)

**Focus:** Internalized self-talk, identity struggles, and emotional self-judgment.

### Emotions Covered (6)

* Self-doubt
* Low confidence
* Body image insecurity
* Imposter syndrome
* Guilt / laziness
* Addiction

### Conversation Style

* **40%** Single-turn
* **50%** Multi-turn (2 turns)
* **10%** Multi-turn (3 turns)

### Distribution

| Emotion               | Entries | Turn Type        |
| --------------------- | ------- | ---------------- |
| Self-doubt            | 250     | Multi-turn       |
| Low confidence        | 200     | Mixed            |
| Body image insecurity | 200     | Multi-turn heavy |
| Imposter syndrome     | 150     | Single-turn      |
| Guilt / laziness      | 100     | Single-turn      |
| Addiction             | 100     | Multi-turn       |

---

## Pillar 4 — Deepening & Complexity (750 entries)

**Focus:** Emotionally complex interactions involving venting, resistance, and mixed affect.

### Emotions Covered (5)

* Mixed emotions
* Venting
* Overwhelm
* Frustration
* Conflicting feelings

### Conversation Style

* **10%** Single-turn
* **60%** Multi-turn (2 turns)
* **30%** Multi-turn (3 turns)

### Distribution

| Emotion              | Entries | Turn Type        |
| -------------------- | ------- | ---------------- |
| Mixed emotions       | 250     | Multi-turn       |
| Venting              | 300     | Multi-turn heavy |
| Overwhelm            | 100     | 2-turn           |
| Conflicting feelings | 50      | 3-turn           |
| Frustration          | 50      | 2-turn           |

---

## Pillar 5 — Safety & High Stakes (500 entries)

**Focus:** Crisis scenarios requiring careful handling, escalation awareness, and safety alignment.

### Emotions Covered (5)

* Panic attacks
* Severe anxiety
* Self-harm thoughts
* Suicidal ideation
* Abuse / bullying

### Conversation Style

* **20%** Single-turn
* **60%** Multi-turn (2 turns)
* **20%** Multi-turn (3 turns)

### Distribution

| Emotion            | Entries | Turn Type          |
| ------------------ | ------- | ------------------ |
| Panic attacks      | 150     | Multi-turn         |
| Severe anxiety     | 100     | Mixed              |
| Self-harm thoughts | 100     | Escalation-focused |
| Suicidal ideation  | 75      | Escalation-focused |
| Abuse / bullying   | 75      | Mixed              |

---

## 📊 Pillar-wise Language Distribution

| Pillar                 | Total    | Hinglish | English  | Hindi (Roman) |
| ---------------------- | -------- | -------- | -------- | ------------- |
| Daily Grind            | 1500     | 900      | 450      | 150           |
| Heart & Social         | 1250     | 687      | 188      | 375           |
| Inner Critic           | 1000     | 500      | 400      | 100           |
| Deepening & Complexity | 750      | 525      | 75       | 150           |
| Safety & High Stakes   | 500      | 200      | 100      | 200           |
| **Total**              | **5000** | **2812** | **1213** | **975**       |

---

## Language Mirroring Policy

The assistant responses are intentionally **language-aligned** with the user input:

* **User: English → Assistant: English (pure)**
* **User: Hinglish → Assistant: Hinglish (same mix ratio)**
* **User: Hindi → Assistant: Hindi (Roman script only)**

This design preserves conversational naturalness and cultural authenticity.

