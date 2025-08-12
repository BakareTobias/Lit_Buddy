import streamlit as st

def display_with_copy(content, title="Content"):
    st.write(f"**{title}:**")
    
    # Create the HTML with copy button
    copy_html = f"""
    <div style="position: relative; background: #f0f2f6; padding: 15px; border-radius: 5px; margin: 10px 0;">
        <pre style="margin: 0; white-space: pre-wrap;">{content}</pre>
        <button onclick="copyToClipboard()" style="
            position: absolute; 
            top: 10px; 
            right: 10px; 
            background: #007bff; 
            color: white; 
            border: none; 
            border-radius: 3px; 
            padding: 5px 10px; 
            cursor: pointer;
        ">📋 Copy</button>
    </div>
    
    <script>
    function copyToClipboard() {{
        navigator.clipboard.writeText(`{content}`).then(() => {{
            alert('Copied to clipboard!');
        }});
    }}
    </script>
    """
    
    st.markdown(copy_html, unsafe_allow_html=True)

