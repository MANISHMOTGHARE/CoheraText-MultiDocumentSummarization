# CoheraText – Multi-Document Abstractive Text Summarization

**Author:** Prof. Manish Motghare

CoheraText is a state-of-the-art multi-document abstractive summarization model designed for generating coherent, factually accurate, and concise summaries from clusters of related news articles. The model leverages hierarchical attention, memory augmentation, and global contextualization, and is extensively evaluated on the IndoSumm dataset—the largest manually curated Indian news summarization dataset to date.

---

## Key Features

- **Hierarchical Attention**: Multi-level transformer attention at sentence, document, and cluster levels for deep context modeling.
- **Memory Augmentation**: External memory module to enhance factual consistency and enable effective cross-document reasoning.
- **Cross-Document Semantic Alignment**: Aligns information and resolves redundancy across multiple news sources within a cluster.
- **Global Contextualization**: Maintains discourse flow and narrative structure across documents for high-quality abstractive summaries.
- **Composite Training Objectives**: Joint optimization for generation quality, coverage, and factual accuracy (cross-entropy, coverage, and factual loss).
- **Human-Centric Evaluation**: Annotation, training, and model selection guided by large-scale human-written references and expert annotators.
- **Transferability**: Demonstrated generalization across both Indian and international news benchmarks (CNN/DailyMail, XSum, Multi-News, WikiSum).
- **Open and Reproducible**: All code, model checkpoints, and the IndoSumm dataset are released for the research community under an open license.

## Repository Structure

CoheraText/
├── data/ # Data directory
│ ├── raw/ # Raw news data from multiple Indian newspapers
│ └── processed/ # Cleaned, tokenized, clustered data for train/val/test
├── src/ # Source code for models and utility layers
│ ├── model/ # Model architectures: CoheraText, baselines, utility layers
│ ├── preprocessing/ # Data preprocessing scripts: cleaning, deduplication, tokenization
│ ├── training/ # Training scripts, fine-tuning, early stopping routines
│ └── evaluation/ # Scripts for ROUGE, BERTScore, human metrics, ablation, etc.
├── deployment/ # Scripts for inference, REST API, or web app integration
├── notebooks/ # Jupyter notebooks for experiments, visualization, and analysis
├── scripts/ # Helper scripts: data checks, reproducibility, etc.
├── tests/ # Unit and regression tests
├── docs/ # Documentation: usage, API reference, diagrams
├── requirements.txt # Python dependencies for running the project
├── README.md # Project overview, features, installation, and usage guide
└── LICENSE # License file (e.g., CC BY 4.0)

##Public Datasets Used for Benchmarking

We compare our models and approaches against the following public abstractive summarization datasets:

CNN/DailyMail, XSum, Multi-News, WikiSum, Multi-Xscience, NewSHead, Newsroom, WikiHow, Gigaword, Reddit TIFU, BookSum, NYT Annotated Corpus, BillSum, BigPatent, LCSTS, SAMSum, WikiLingua, MLSUM, Opinosis, Webis-TLDR-17, Polish Summaries Corpus (PSC), AESLC, SCITLDR, MATINF, WikiSummary, XL-Sum, Wikipedia Current Events Portal (WCEP), PeerSum, ConvoSumm, DUC 2004, TAC 2011, KALIMAT Multipurpose Arabic Corpus, RedSum, WCEP-10, NewsSumm (IndoSumm), Global Voices, Shmoop Corpus, FINDSum, AMR Bank, DialogSum, SciTLDR, arXiv Summarization Dataset, GLGE, BookSum, M3LS, OpenDebateEvidence, PlainFact, Proto Summ, Webis-Snippet-20, CASS, How2, CorpusTCC, NarraSum, WITS, DMQA, MLSUM, MultiLing Pilot 2011

