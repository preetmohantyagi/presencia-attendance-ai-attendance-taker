import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:var(--snap-card); border-left: 8px solid var(--snap-accent); padding:25px; border-radius: 20px; border: 1px solid var(--snap-border); margin-bottom:20px;">
        <h3 style="margin:0; color: var(--snap-text-heading); font-size: 1.5rem ">{name}</h3>
        <p style="color:var(--snap-text-muted); margin:10px 0;">Code : <span style="background:var(--snap-primary-light); color:var(--snap-primary); padding:2px 8px; border-radius:5px;">{code} </span> | Section : {section}</p>
        
        """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: var(--snap-accent-tint); padding:5px 12px; border-radius:12px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()