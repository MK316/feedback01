import streamlit as st
from gtts import gTTS
import random
import os

# Feedback datasets
feedback_correct = [
    "Well done! You’ve grasped this concept nicely.",
    "Correct! You're on the right track.",
    "Exactly right! You explained that clearly.",
    "Perfect response! You really understand this.",
    "Absolutely! Great effort on this.",
    "Indeed! Keep up this great thinking.",
    "Yes! Can you explore this idea further?",
    "Right on target! You handled this topic well.",
    "Exactly what I was looking for! Your approach worked well.",
    "Superb understanding! You've really got the hang of this.",
    "Correct! What other examples can you think of?",
    "Absolutely! How do you think this relates to our other lessons?",
    "Nice work! You’re showing you know this well.",
    "Spot on! You’re applying what we learned effectively.",
    "Correct! You’re making excellent progress.",
    "That's right! What would be the next step?",
    "Precisely! Can you apply this concept in another context?",
    "You nailed it! Great job solving this one.",
    "Absolutely right! That shows deep understanding.",
    "Excellent insight! You've thought this through well."
]

feedback_incorrect = [
    "Almost there, but let’s review this part again.",
    "A good try, but let’s go over it one more time.",
    "You're close! Let's try to think it through once more.",
    "An interesting approach, but let’s consider a different angle.",
    "Nearly there! What if you look at it this way instead?",
    "You’ve got some of it, but let's tweak your answer a bit.",
    "That’s a common mistake, but you’re getting close. Let’s try again.",
    "You've put in a good effort! Let’s try another way to solve it.",
    "Partly correct, but let's clear up a few misunderstandings.",
    "Keep working on it! You started off well. Let’s refine your thinking.",
    "You’re making progress! What pattern do you see here?",
    "Not quite, but you’re linking some good ideas. Let's refine them.",
    "You’re on the right track, but let’s sharpen your response.",
    "That’s an interesting response, but let’s check its accuracy.",
    "You’ve highlighted the key points, but revisit this section again.",
    "Let’s revisit this concept. Do you remember what we discussed last week?",
    "Very close! Consider what we learned in the previous chapter.",
    "Nice effort! What's challenging about this problem?",
    "Good effort, but let's look at this from another perspective.",
    "Not there yet, but let's figure it out together."
]


def play_audio(feedback, audio_placeholder):
    """Convert text to speech and play audio."""
    tts = gTTS(feedback, lang='en')
    tts.save('feedback.mp3')
    audio_placeholder.audio('feedback.mp3', format='audio/mp3', start_time=0)
    os.remove('feedback.mp3')  # Clean up the audio file after playing

def provide_feedback(feedback_list, session_key, text_placeholder, audio_placeholder):
    """Display and handle feedback operations for a specific list."""
    # Initialize feedback list if not already in session state
    if session_key not in st.session_state or not st.session_state[session_key]:
        st.session_state[session_key] = feedback_list[:]
        random.shuffle(st.session_state[session_key])

    # Pop feedback text and play audio if there are items in the list
    if st.session_state[session_key]:
        current_feedback = st.session_state[session_key].pop()
        text_placeholder.text(current_feedback)  # Update the text placeholder
        play_audio(current_feedback, audio_placeholder)
    else:
        text_placeholder.success("You've gone through all feedback in this category.")
        audio_placeholder.empty()  # Clear the audio placeholder

# UI setup
st.title("Feedback Audio Player")

# Split into two columns for Correct and Incorrect Feedback
col1, col2 = st.columns(2)

with col1:
    st.subheader("😍 Correct Feedback")
    text_placeholder1 = st.empty()  # Placeholder for correct feedback text
    audio_placeholder1 = st.empty()  # Placeholder for correct feedback audio
    if st.button("Next Correct Feedback"):
        provide_feedback(feedback_correct, 'remaining_correct', text_placeholder1, audio_placeholder1)

with col2:
    st.subheader("😅Incorrect Feedback")
    text_placeholder2 = st.empty()  # Placeholder for incorrect feedback text
    audio_placeholder2 = st.empty()  # Placeholder for incorrect feedback audio
    if st.button("Next Incorrect Feedback"):
        provide_feedback(feedback_incorrect, 'remaining_incorrect', text_placeholder2, audio_placeholder2)
