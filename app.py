import streamlit as st
from gtts import gTTS
import random
import os

# Feedback datasets
feedback_correct = [
    "Excellent work! You've got it.",
    "Correct! Nicely done.",
    "Exactly right! Well explained.",
    "Perfect! You understand this well.",
    "Absolutely! Keep up the good effort.",
    "Indeed! Keep thinking this way.",
    "Yes! Can you expand on that?",
    "Right on target! You handled it skillfully.",
    "Exactly! Your approach is effective.",
    "Superb! You understand the concept.",
    "Correct! What else can you tell me?",
    "Absolutely! How does this relate to what we know?",
    "Good job! You're showing great understanding.",
    "Spot on! You're applying the concepts well.",
    "Right answer! Your progress is excellent.",
    "Correct! Very thorough.",
    "That's right! Any other thoughts?",
    "Precisely! You're doing wonderfully.",
    "You've nailed it! Great problem-solving.",
    "Absolutely right! Very insightful."
]

feedback_incorrect = [
    "Close, but let's take another look.",
    "Good try, but let's review.",
    "Almost there, think about it a bit more.",
    "Interesting approach, but let's consider alternatives.",
    "Nearly! Try another angle.",
    "Good thinking, but there's a bit to adjust.",
    "Common mistake, but you're very close.",
    "Solid effort! Let's go through it again.",
    "Partly right, let's clear up a few points.",
    "Keep going! You've started well.",
    "You're getting there! What patterns do you see?",
    "Not quite, but you're making good links. Let's refine them.",
    "Right concept, but let's fine-tune your answer.",
    "That's an interesting response, let's verify it.",
    "You've touched on key points, but revisit this part.",
    "Let's look at this again. Might we have missed something?",
    "So close! Think about our previous discussions.",
    "Nice attempt! What's challenging here?",
    "Good effort, but let's explore this from another perspective.",
    "Not there yet, but let's figure it out together."
]

def play_audio(feedback):
    """Convert text to speech and play audio."""
    tts = gTTS(feedback, lang='en')
    tts.save('feedback.mp3')
    st.audio('feedback.mp3', format='audio/mp3', start_time=0)
    os.remove('feedback.mp3')  # Clean up the audio file after playing

def provide_feedback(feedback_list, session_key):
    """Display and handle feedback operations for a specific list."""
    if session_key not in st.session_state or not st.session_state[session_key]:
        st.session_state[session_key] = feedback_list[:]
        random.shuffle(st.session_state[session_key])
    
    if st.session_state[session_key]:
        current_feedback = st.session_state[session_key].pop()
        st.write(current_feedback)
        play_audio(current_feedback)
    else:
        st.success("You've gone through all feedback in this category. Start over or switch categories.")

# UI setup
st.title("Feedback Audio Player")
st.write("Choose a situation to get feedback:")

col1, col2 = st.columns(2)

with col1:
    if st.button("When the answer is correct"):
        provide_feedback(feedback_correct, 'remaining_correct')
    if 'remaining_correct' in st.session_state:
        if st.button("Next Correct"):
            provide_feedback(feedback_correct, 'remaining_correct')

with col2:
    if st.button("When the answer is incorrect"):
        provide_feedback(feedback_incorrect, 'remaining_incorrect')
    if 'remaining_incorrect' in st.session_state:
        if st.button("Next Incorrect"):
            provide_feedback(feedback_incorrect, 'remaining_incorrect')
