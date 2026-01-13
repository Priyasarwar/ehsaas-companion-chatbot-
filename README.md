# Ehsaas: Empathetic Conversational AI for Indian Youth

**Ehsaas** (Hindi/Urdu for 'Feelings') is a research-driven project developing a **multilingual (Hinglish/English)** conversational framework tailored for the emotional support of Indian youth (ages 18–25). 

---

##  Project Overview
Most emotional support agents are English-centric and follow Western therapeutic norms. **Ehsaas** bridges this gap by focusing on:
* **Code-Mixed NLP:** Handling natural Hinglish/Roman Hindi dialogue.
* **Cultural Grounding:** Addressing specific Indian youth stressors (academic pressure, family expectations).
* **Responsible AI:** A non-clinical, empathy-first approach that prioritizes listening over diagnosis.

##  Dataset Contribution
The core of this project is a curated dataset of **5,000 conversational turns** designed for fine-tuning Large Language Models (LLMs).
* **Language Mix:** 60% Hinglish (Roman), 30% English, 10% Roman Hindi.
* **5 Pillars of Support:** Daily Grind (Academics), Social/Heart (Relationships), Inner Critic (Self-doubt), Complexity (Venting), and Safety (Crisis markers).

## Technical Roadmap (Work in Progress)
currently executing the following research pipeline:
1. **Dataset Synthesis:** Constrained prompting using LLMs to generate culturally authentic, safe, and diverse empathetic dialogues.
2. **Model Fine-Tuning:** Performing **Supervised Fine-Tuning (SFT)** on **Gemma-2B** using **PEFT/LoRA** to adapt the model to the Ehsaas dataset.
3. **Dialogue Management:** Deploying via a modular architecture using **Voiceflow** as the dialogue manager to handle state tracking and human-in-the-loop evaluation.

