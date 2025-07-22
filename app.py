import os
import uuid
import requests
import json
import random
import re
from pydub import AudioSegment
import gradio as gr
import speech_recognition as sr

def log_step(msg):
    print(f"[EVAL_READING] {msg}")

def convert_to_wav(input_path, output_path=None):
    if output_path is None:
        output_path = os.path.join("uploads", f"converted_{uuid.uuid4()}.wav")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    log_step(f"Converting audio from {input_path} to WAV format")
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="wav")
        log_step(f"Audio successfully converted to {output_path}")
        return output_path
    except Exception as e:
        error_msg = f"Failed to convert audio: {e}"
        log_step(f"ERROR in audio conversion: {error_msg}")
        raise RuntimeError(error_msg)

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language='en-US')
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"

def generate_reading_passage(topic):
    """
    Generate a reading passage with graduated difficulty levels
    """
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    if not DEEPSEEK_API_KEY:
        raise EnvironmentError("Missing DEEPSEEK_API_KEY in environment.")

    prompt = f"""
    Create a reading passage about "{topic}" with graduated difficulty levels. The passage should have 4 paragraphs:
    
    1. First paragraph: A1-A2 level (beginner) - Simple sentences, basic vocabulary, present tense
    2. Second paragraph: B1 level (intermediate) - More complex sentences, varied vocabulary
    3. Third paragraph: B2 level (upper-intermediate) - Complex grammar, academic vocabulary
    4. Fourth paragraph: C1-C2 level (advanced) - Sophisticated language, complex ideas
    
    Each paragraph should be 60-80 words and build upon the previous one while maintaining coherence.
    The topic should be engaging and educational.
    
    IMPORTANT: Write ONLY the paragraphs without any level headings or labels. Just provide the 4 paragraphs separated by line breaks.
    """

    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
            json={
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an expert English language teacher who creates reading materials for language learners at different proficiency levels."
                    },
                    {
                        "role": "user",
                        "content": prompt.strip()
                    }
                ],
                "temperature": random.uniform(0.9, 1),
                "max_tokens": 800
            }
        )

        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"].strip()
        
        return f"Error generating passage: Status {response.status_code}"

    except Exception as e:
        return f"Error generating passage: {str(e)}"

def evaluate_reading_performance(original_text, transcript_input):
    """
    Evaluate reading performance based on original text and spoken transcript
    """
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    if not DEEPSEEK_API_KEY:
        raise EnvironmentError("Missing DEEPSEEK_API_KEY in environment.")

    prompt = f"""
    You are an expert English reading and pronunciation tutor evaluating a learner's reading performance based on CEFR standards. 

    The learner was given the following text to read aloud:
    ---
    {original_text}
    ---

    This is the auto-generated transcript of what they actually said (no punctuation):
    ---
    {transcript_input}
    ---

    Please evaluate their reading performance and return a JSON response with:
    1. "accuracy_score": Score out of 100 for how accurately they read the text
    2. "pronunciation_score": Score out of 100 for pronunciation quality
    3. "fluency_score": Score out of 100 for reading fluency and rhythm
    4. "comprehension_level": Estimated level (A1-C2) based on which parts they read well
    5. "pronunciation_errors": List of specific pronunciation issues identified
    6. "missed_words": Words from original text that were skipped or mispronounced
    7. "reading_pace": Assessment of reading speed (too fast/slow/appropriate)
    8. "strengths": What the learner did well in their reading
    9. "improvement_areas": Specific areas that need work
    10. "practice_tips": Actionable advice for improving reading skills
    11. "motivational_comment": Encouraging feedback to boost confidence

    Compare the original text with the transcript to identify:
    - Word accuracy and pronunciation
    - Fluency and natural rhythm
    - Handling of different difficulty levels in the text

    Respond in clean JSON format only.
    """

    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
            json={
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a certified English reading tutor specializing in pronunciation and fluency assessment. You provide constructive, encouraging feedback."
                    },
                    {
                        "role": "user",
                        "content": prompt.strip()
                    }
                ],
                "temperature": random.uniform(0.9, 1),
                "max_tokens": 1500
            }
        )

        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                content = data["choices"][0]["message"]["content"]
                clean_json_text = re.sub(r"```json|```", "", content).strip()

                try:
                    return json.loads(clean_json_text)
                except json.JSONDecodeError as decode_err:
                    return {
                        "accuracy_score": 0,
                        "pronunciation_score": 0,
                        "fluency_score": 0,
                        "comprehension_level": "Unknown",
                        "pronunciation_errors": [],
                        "missed_words": [],
                        "reading_pace": "Unknown",
                        "strengths": "N/A",
                        "improvement_areas": "N/A",
                        "practice_tips": [f"Invalid JSON format: {str(decode_err)}"],
                        "motivational_comment": "Keep practicing!"
                    }
        else:
            return {
                "accuracy_score": 0,
                "pronunciation_score": 0,
                "fluency_score": 0,
                "comprehension_level": "Unknown",
                "pronunciation_errors": [],
                "missed_words": [],
                "reading_pace": "Unknown",
                "strengths": "N/A",
                "improvement_areas": "N/A",
                "practice_tips": [f"API Error: {response.status_code}"],
                "motivational_comment": "Keep practicing!"
            }

    except Exception as e:
        return {
            "accuracy_score": 0,
            "pronunciation_score": 0,
            "fluency_score": 0,
            "comprehension_level": "Unknown",
            "pronunciation_errors": [],
            "missed_words": [],
            "reading_pace": "Unknown",
            "strengths": "N/A",
            "improvement_areas": "N/A",
            "practice_tips": [f"Exception occurred: {str(e)}"],
            "motivational_comment": "Keep practicing!"
        }

def generate_passage_only(topic):
    """Generate reading passage for given topic"""
    log_step(f"Generating passage for topic: {topic}")
    
    if not topic.strip():
        return "Please enter a topic first!"
    
    passage = generate_reading_passage(topic)
    log_step("Passage generated successfully")
    return passage

def evaluate_reading_only(passage_text, audio_file):
    """Evaluate reading performance"""
    if not passage_text.strip():
        return json.dumps({
            "error": "Please generate a reading passage first!"
        }, indent=2)
    
    if audio_file is None:
        return json.dumps({
            "error": "Please upload an audio recording!"
        }, indent=2)
    
    log_step("Starting reading evaluation...")
    
    # Convert audio and transcribe
    wav_path = convert_to_wav(audio_file)
    transcript = transcribe_audio(wav_path)
    log_step(f"Transcript: {transcript}")
    
    # Evaluate performance
    result = evaluate_reading_performance(passage_text, transcript)
    log_step("Evaluation completed")
    
    return json.dumps(result, indent=2, ensure_ascii=False)

# Create the step-by-step interface
with gr.Blocks(title="English Reading Evaluation System") as iface:
    gr.Markdown("# 📚 English Reading Evaluation System")
    
    # Step 1: Topic Input
    gr.Markdown("## Step 1: Enter Topic")
    topic_input = gr.Textbox(
        label="Enter a topic for your reading passage",
        placeholder="e.g., Climate Change, Technology, Travel, History, Science...",
        value=""
    )
    
    generate_btn = gr.Button("🎯 Generate Reading Passage", variant="primary")
    
    # Step 2: Generated Passage
    gr.Markdown("## Step 2: Generated Reading Passage")
    passage_display = gr.Textbox(
        label="Your Reading Passage",
        lines=15,
        max_lines=20,
        interactive=False,
        placeholder="Your reading passage will appear here after clicking 'Generate Reading Passage'..."
    )
    
    # Step 3: Audio Recording
    gr.Markdown("## Step 3: Record Your Reading")
    audio_input = gr.Audio(
        type="filepath",
        label="🎙️ Record yourself reading the passage aloud"
    )
    
    evaluate_btn = gr.Button("📊 Evaluate My Reading", variant="primary")
    
    # Step 4: Evaluation Results
    gr.Markdown("## Step 4: Your Evaluation Results")
    evaluation_output = gr.Code(
        label="📋 Reading Evaluation Results",
        language="json",
        interactive=False
    )
    
    # Connect the functions
    generate_btn.click(
        fn=generate_passage_only,
        inputs=topic_input,
        outputs=passage_display
    )
    
    evaluate_btn.click(
        fn=evaluate_reading_only,
        inputs=[passage_display, audio_input],
        outputs=evaluation_output
    )

if __name__ == "__main__":
    iface.launch()