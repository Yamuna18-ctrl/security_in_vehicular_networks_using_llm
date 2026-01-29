# Security In Vehicular Networks Using LLM
LLM-Based V2V Semantic Security System

This project implements a real-time semantic security framework for Vehicle-to-Vehicle (V2V) communication. It detects fake or semantically inconsistent messages by validating physical plausibility using vehicle dynamics and explainable LLM-based reasoning.

Features

Real-time V2V message simulation using NGSIM traffic data
Semantic validation of speed and acceleration
Binary classification: Real / Fake messages
LLM-based explainable reasoning
Interactive security dashboard

Dataset

Source: NGSIM (I-294 traffic dataset)
Size: 10 lakh+ vehicle records
Usage: Dynamically sampled for real-time simulation

Technologies

Python (Flask)
HTML, CSS, JavaScript
HuggingFace Transformers (DistilGPT-2)
Chart.js

Run
pip install flask transformers
python app.p

Novelty

Semantic-level security using physics-aware validation and explainable LLM reasoning — no traditional ML training required.
