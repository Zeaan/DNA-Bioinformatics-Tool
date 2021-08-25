import streamlit as st
import pandas as pd
import altair as alt

st.title("DNA Bioinformatics Tool")
st.header("Developed by Zeaan Pithawala")

sample_input = ">Sample FASTA Sequence\nATGCATGCCGTAGA\nGTTCGTGCAGTAGT\nATACATCCTCTAGC"
st.write("Enter DNA Sequence to get valuable insights")
sequence = st.text_area("Paste FASTA Sequence here",sample_input,height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)
st.write("The input provided is")
st.write(sequence)

Acount = 0
Tcount = 0
Gcount = 0
Ccount = 0
flag = True
for i in sequence:
    if i not in 'ATGCatgc':
        flag = False
        st.write("The sequence is wrong")
        st.write(i,"cannot be in DNA Sequence")
        st.write("Please paste correct FASTA Sequence")
if flag:
    for i in sequence:
        if i == "A":
            Acount = Acount+1
        elif i == "T":
            Tcount = Tcount+1
        elif i == "G":
            Gcount = Gcount+1
        else:
            Ccount = Ccount+1
    
    st.write("Number of A:",Acount,"Number of C:",Ccount,"Number of G:",Gcount,"Number of T:",Tcount)
    
    # Made a dictionary from which Data Frame can be constructed
    d = {'A':Acount, 'C':Ccount, 'G':Gcount, 'T':Tcount}
    df = pd.DataFrame.from_dict(d,orient='index')
    df = df.rename({0: 'COUNT'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns = {'index':'NUCLEOTIDE'})
    
    p = alt.Chart(df).mark_bar().encode(
        # Axes of the bar graph
        x='NUCLEOTIDE',
        y='COUNT'
    )
    p = p.properties(
        # Controls the width of bar
        width=alt.Step(80)
    )
    st.write(p)

st.write("If you want to know more about me, visit my Website or LinkedIn and feel free to connect with me!")
st.write("Website- https://zeaan.github.io/website/")
st.write("LinkedIn- https://www.linkedin.com/in/zeaan-pithawala/")