# AI Text Detector

Welcome to the AI Text Detector project! This repository contains the source code for an AI-generated text detector developed using machine learning techniques. The project is part of a design project for the Gold CREST award.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In the age of AI-generated content, distinguishing between human-written and machine-generated text has become increasingly important. This project aims to address this challenge by leveraging advanced machine learning algorithms to detect AI-generated text with high accuracy. Whether you're a researcher, developer, or just curious about AI, this project offers valuable insights and tools for text detection.

## Features

- **AI-Powered Detection**: Fine-tuning the RoBERTa model to differentiate between human and AI-generated text.
- **Jupyter Notebooks**: Interactive notebooks for data exploration, model training, and evaluation.
- **Comprehensive Dataset**: Includes a diverse dataset of human and AI-generated text samples.
- **Scalable Architecture**: Designed to handle large-scale text data efficiently.

## Project Structure

```
AI_Text_Detector/
├── data/                   # Directory containing datasets
├── models/                 # Directory containing trained models
├── notebooks/              # Jupyter notebooks for experiments and analysis
├── src/                    # Source code directory
│   ├── data_preprocessing.py  # Data preprocessing scripts
│   ├── model_training.py      # Model training scripts
│   ├── text_detection.py      # Text detection scripts
│   └── utils.py               # Utility functions
├── requirements.txt        # Python dependencies
└── README.md               # Project README
```

## Installation

To install and run the AI Text Detector, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/moosemorse/AI_Text_Detector.git
    cd AI_Text_Detector
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start using the AI Text Detector, you can explore the Jupyter notebooks in the `notebooks` directory. These notebooks provide step-by-step instructions for data preprocessing, model training, and text detection.

1. Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```

2. Open and run the notebooks in the `notebooks` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
