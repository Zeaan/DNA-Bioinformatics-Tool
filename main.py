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
    
    # To write complementary mRNA
    complementarity = {"A": "U", "C":"G", "G":"C", "T":"A"}
    complementary_RNA = ''
    for i in sequence:
        complementary_RNA = complementary_RNA+complementarity[i]
    st.write("The complementary mRNA Strand would be")
    st.write(complementary_RNA)

    # To find out the codons
    codons = []
    codon = ''
    for i in range(len(complementary_RNA)-1):
        if ((i+1)%3)==0:
            codon = complementary_RNA[i-2:i+1]
            codons.append(codon)
    st.write("The codons are")
    codon_sequence = ''
    for i in codons:
        codon_sequence = codon_sequence+" - "+i
    st.write(codon_sequence)

    # To find out the amino acids corresponding to codons
    amino_acids = {
        "Phe" : ["UUU","UUC"],
        "Leu" : ["UUA","UUG","CUU","CUA","CUG","CUC"],
        "Ile" : ["AUU","AUC","AUA"],
        "Met" : ["AUG"],
        "Val" : ["GUU","GUC","GUA","GUG"],
        "Ser" : ["UCU","UCA","UCG","UCC","AGU","AGC"],
        "Pro" : ["CCU","CCA","CCG","CCC"],
        "Thr" : ["ACU","ACA","ACC","ACG"],
        "Ala" : ["GCU","GCA","GCC","GCG"],
        "Tyr" : ["UAU","UAC"],
        "His" : ["CAU","CAC"],
        "Gln" : ["CAA","CAG"],
        "Asn" : ["AAU","AAC"],
        "Lys" : ["AAA","AAG"],
        "Asp" : ["GAU","GAC"],
        "Glu" : ["GAA","GAG"],
        "Cys" : ["UGU","UGC"],
        "Trp" : ["UGG"],
        "Arg" : ["CGU","CGA","CGG","CGC","AGA","AGG"],
        "Gly" : ["GGU","GGG","GGA","GGC"], 
        "Stop Codon" : ["UAA","UAG","UGA"]
    }
    amino_acid_sequence = ''
    for i in codons:
        for j in amino_acids:
            for k in amino_acids[j]:
                if i==k:
                    amino_acid_sequence = amino_acid_sequence+" - "+j
    st.write("The amino acid sequence is")
    st.write(amino_acid_sequence)

st.write("If you want to know more about me, visit my Website or LinkedIn and feel free to connect with me!")
st.write("Website- https://zeaan.github.io/website/")
st.write("LinkedIn- https://www.linkedin.com/in/zeaan-pithawala/")
