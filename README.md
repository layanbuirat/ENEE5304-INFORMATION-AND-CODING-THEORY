# ENEE5304-INFORMATION-AND-CODING-THEORY
# 🗜️ Lempel-Ziv (LZ78) Data Compression Project

<div align="center">
  <img src="view%20result.gif" width="800" alt="Compression Demo">
</div>

## 📝 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Demo](#-demo)
- [Theoretical Background](#-theoretical-background)
- [Implementation](#-implementation)
- [Results](#-results)
- [How to Run](#-how-to-run)
- [Documentation](#-documentation)
- [Team](#-team)

## 🌟 Project Overview
Implementation of the Lempel-Ziv (LZ78) algorithm to compress random strings of symbols (a, b, c, d) with the following probabilities:

- P(a)=0.5
- P(b)=0.25 
- P(c)=0.2
- P(d)=0.05

## ✨ Key Features
Calculation of source entropy (1.6855 bits/symbol)

Dynamic dictionary construction for symbols

Achieving a compression ratio of up to 0.3569 for long strings

Performance analysis for various string lengths (20 to 5000 symbols)



## 🎥 Demo
<div align="center">
  <img src="view%20result.gif" width="800" alt="System Demo">
  <br>
  <a href="view%20result.mp4">Download Full Video (MP4)</a>
</div>

## 📚 Theoretical Background
#Entropy Formula:
H
=
−
∑
i
P
(
i
)
log
⁡
2
P
(
i
)
H=− 
i
∑
​
 P(i)log 
2
​
 P(i)
Theoretical Value: 1.6855 bits/symbol

LZ78 Mechanism:
Split the string into unique phrases

Build a dynamic dictionary

Encode each phrase as a pair (index, symbol)
## 💻 Implementation
git clone https://github.com/layanbuirat/LZ78-Compression.git
def lz78_encode(sequence):
    dictionary = {}
    encoded = []
    next_code = 1
    
    while sequence:
        # Find longest prefix in dictionary
        for l in range(len(sequence), 0, -1):
            prefix = sequence[:l]
            if prefix in dictionary.values():
                code = list(dictionary.keys())[list(dictionary.values()).index(prefix)]
                remaining = sequence[l:]
                if remaining:
                    symbol = remaining[0]
                    encoded.append((code, symbol))
                    dictionary[next_code] = prefix + symbol
                    next_code += 1
                    sequence = sequence[l+1:]
                else:
                    encoded.append((code, ''))
                    sequence = ''
                break
        else:
            symbol = sequence[0]
            encoded.append((0, symbol))
            dictionary[next_code] = symbol
            next_code += 1
            sequence = sequence[1:]
    
    return encoded, dictionary
  ## Results

Sequence Length	Encoded Bits	Compression Ratio	Bits/Symbol
20	96	0.6000	4.8000
5000	14083	0.3521	2.8166
python leyan_1211439.py
📂 Documentation
Full ReportDr. Wael Hashlamoun - Supervisor

Compressed Project Files

👥 Team
Layan Buirat(1211439) -( https://github.com/layanbuirat/ENEE5304-INFORMATION-AND-CODING-THEORY)
Dr. Wael Hashlamoun - Supervisor


<p align="center"> <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python"> <img src="https://img.shields.io/badge/License-MIT-green"> </p> ```

