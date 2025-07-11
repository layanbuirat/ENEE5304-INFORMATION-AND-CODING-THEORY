﻿# ENEE5304-INFORMATION-AND-CODING-THEORY
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
تنفيذ خوارزمية Lempel-Ziv (LZ78) لضغط سلاسل عشوائية من الرموز (a, b, c, d) مع الاحتمالات:
- P(a)=0.5
- P(b)=0.25 
- P(c)=0.2
- P(d)=0.05

## ✨ Key Features
- حساب إنتروبيا المصدر (1.6855 bits/symbol)
- بناء قاموس ديناميكي للرموز
- تحقيق نسبة ضغط تصل إلى 0.3569 لسلاسل طويلة
- تحليل أداء الخوارزمية لمختلف أطوال السلاسل (20 إلى 5000 رمز)

## 🎥 Demo
<div align="center">
  <img src="view%20result.gif" width="800" alt="System Demo">
  <br>
  <a href="view%20result.mp4">Download Full Video (MP4)</a>
</div>

## 📚 Theoretical Background
### معادلة الإنتروبيا:
\[ H = -\sum_{i}P(i)\log_{2}P(i) \]
**القيمة النظرية:** 1.6855 bits/symbol

### آلية عمل LZ78:
1. تقسيم السلسلة إلى عبارات فريدة
2. بناء قاموس ديناميكي
3. ترميز كل عبارة كزوج (مؤشر، رمز)

## 💻 Implementation
```python
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
📊 Results
Sequence Length	Encoded Bits	Compression Ratio	Bits/Symbol
20	96	0.6000	4.8000
5000	14083	0.3521	2.8166
🚀 How to Run
استنساخ المستودع:
git clone https://github.com/layanbuirat/LZ78-Compression.git
تشغيل الكود:

python leyan_1211439.py
📂 Documentation
Full Report

Compressed Project Files

👥 Team
ليان بعيرات (1211439) -( https://github.com/layanbuirat/ENEE5304-INFORMATION-AND-CODING-THEORY)

الدكتور وائل حشلمون - المشرف

<p align="center"> <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python"> <img src="https://img.shields.io/badge/License-MIT-green"> </p> ```
