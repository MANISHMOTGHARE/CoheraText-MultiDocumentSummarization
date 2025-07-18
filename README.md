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
├── data/                      # Data directory
│   ├── raw/                   # Raw news data collected from multiple sources
│   ├── processed/             # Cleaned, tokenized, and clustered data for training/validation/testing
├── src/                       # Source code
│   ├── model/                 # Model architectures (CoheraText, baselines, utility layers)
│   ├── preprocessing/         # Data preprocessing scripts (cleaning, deduplication, tokenization)
│   ├── training/              # Training scripts, fine-tuning, and early stopping routines
│   ├── evaluation/            # Evaluation scripts for ROUGE, BERTScore, human metrics, etc.
│   ├── deployment/            # Scripts for inference, REST API, or web app integration
├── notebooks/                 # Jupyter notebooks for experiments, visualization, and analysis
├── scripts/                   # Helper and utility scripts (data checks, reproducibility, etc.)
├── tests/                     # Unit, integration, and regression test cases
├── docs/                      # Documentation (usage, API reference, paper, diagrams)
├── requirements.txt           # Python dependencies required for the project
├── README.md                  # Project overview and instructions (this file)
└── LICENSE                    # License for open-source distribution
