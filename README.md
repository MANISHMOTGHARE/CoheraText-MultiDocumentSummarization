# CoheraText – Multi-Document Abstractive Text Summarization

**Author:** Prof. Manish Motghare

CoheraText is a state-of-the-art multi-document abstractive summarization model designed for generating coherent, factually accurate, and concise summaries from clusters of related news articles. The model leverages hierarchical attention, memory augmentation, and global contextualization, and is extensively evaluated on the IndoSumm dataset—the largest manually curated Indian news summarization dataset to date.

---

## Key Features

- **Hierarchical Attention:** Multi-level attention at sentence, document, and cluster granularity  
- **Memory Augmentation:** External memory module for factual consistency and cross-document reasoning  
- **Advanced Positional Encodings:** For robust long-context fusion  
- **Global Contextualization:** Maintains discourse structure across documents  
- **Transferability:** Generalizes across Indian and international news benchmarks  
- **Human-Centric Evaluation:** Model development guided by human annotator preferences  

---

## Repository Structure

CoheraText/
├── data/
│ ├── raw/ # Raw data collected from news sources
│ ├── processed/ # Processed data ready for model training
├── src/
│ ├── model/ # Model definition files (architecture, layers)
│ ├── preprocessing/ # Scripts for data cleaning and preparation
│ ├── training/ # Training scripts and configs
│ ├── evaluation/ # Scripts for evaluation and metric computation
│ ├── deployment/ # Deployment scripts (API, web-app, etc.)
├── notebooks/ # Jupyter notebooks for experiments and analysis
├── scripts/ # Utility scripts
├── tests/ # Unit and integration test cases
├── docs/ # Project documentation
├── requirements.txt # Python dependencies
├── README.md # This file
└── LICENSE # License for the project
