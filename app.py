import streamlit as st
import json
from sbox_loader import load_dataset

st.set_page_config(
    page_title="S-box Analyzer",
    layout="wide"
)

st.title("AES S-box Analyzer")

@st.cache_data
def load_data():
    return load_dataset()

dataset = load_data()
sbox_ids = list(dataset.keys())

mode = st.sidebar.radio(
    "Mode",
    ["Dataset", "Direct S-box"]
)

if mode == "Dataset":
    sbox_id = st.sidebar.selectbox("Select S-box", sbox_ids)
    entry = dataset[sbox_id]

    st.subheader(entry["name"])

    st.markdown("### Metrics")
    cols = st.columns(5)
    for i, (k, v) in enumerate(entry["metrics"].items()):
        cols[i % 5].metric(k, round(v, 6) if isinstance(v, float) else v)

    with st.expander("S-box (hex)"):
        table = [
            f"{entry['sbox'][i*16 + j]:02X}"
            for i in range(16)
            for j in range(16)
        ]
        for i in range(16):
            st.text(" ".join(table[i*16:(i+1)*16]))

elif mode == "Direct S-box":
    raw = st.text_area("Paste 256 integers (comma-separated)")
    if st.button("Analyze"):
        sbox = [int(x) for x in raw.split(",")]
        if len(set(sbox)) != 256:
            st.error("Not bijective")
            st.stop()

        st.warning("Metric recomputation disabled for cloud safety")
