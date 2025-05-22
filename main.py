import streamlit as st
from agents.tutor_agent import TutorAgent

# Persist the Tutor Agent across runs using Streamlit session_state
if "tutor" not in st.session_state:
    st.session_state.tutor = TutorAgent()
tutor = st.session_state.tutor

# Streamlit UI
st.set_page_config(page_title="AI Tutor Agent", layout="centered")
st.title("📚 AI Tutor Agent")
st.markdown("Ask a question related to Math, Physics, or Chemistry.")

# User input
query = st.text_input("🔍 Type your question here")

# Button to trigger query
if st.button("Ask"):
    if query.strip() != "":
        with st.spinner("Thinking..."):
            answer = tutor.handle_query(query)
        st.success("✅ Answer:")
        st.write(answer)

        # Bonus: Show conversation history
        with st.expander("🧠 Conversation Context (Bonus)"):
            st.text(st.session_state.tutor.memory.get_context())
    else:
        st.warning("Please enter a valid question.")
