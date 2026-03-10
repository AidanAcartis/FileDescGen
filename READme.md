# 📂 File Description Training Model

## 🎯 Goal

This project is an **experimental prototype** designed to train a model that generates human-like descriptions from a file name.  
The aim is to eventually integrate this model into a software tool for file management or analysis.

The workflow includes multiple steps: collecting filenames, extracting file properties, generating synthetic descriptions, building a clean dataset, and training a fine-tuned model.

---

## 🏗 Project Structure

```

File_Desc_Training_Model/
│
├── dataset/
│   ├── file_desc_data/          # Final dataset of filenames and descriptions in JSONL format
│   └── file-description.py      # Script to prepare the final training dataset
│
├── Notebook_Training/
│   └── File_desc_full_fine_tune.ipynb  # Notebook for model fine-tuning
│
└── README.md                    # Project documentation

````

---

## 📑 Step 1 – Extract File Properties

**Location:** `Get_data_process/Get_Files/get_files_proprities.py`

This script converts raw filename entries into a structured JSON format:

* Splits each entry into **filename**, **extension**, **directory**, and **application**  
* Outputs the structured data into `Files_list.jsonl`

Example output:

```json
{"id": "0", "filename": "extract_window_events", "extension": "sh", "directory": "Collect_file", "application": "Visual Studio Code"}
````

---

## 📚 Step 4 – Build Final Dataset

**Location:** `dataset/file-description.py`

This script selects only the relevant fields (**filename** and **description**) and prepares the final training dataset in JSONL format.

* Input: `response.jsonl`
* Output: `file_description.jsonl`

Example entry in the final dataset:

```json
{"id": "0", "filename": "extract_window_events", "file_desc": "This is a shell script (.sh) named extract_window_events.sh located in the Collect_file directory. It likely extracts window-related events from a system or application and can be opened and edited using Visual Studio Code."}
```

---

## 🧑‍💻 Step 5 – Model Training

**Location:** `Notebook_Training/File_desc_full_fine_tune.ipynb`

This notebook fine-tunes a language model (e.g., Flan-T5) on the `file_description.jsonl` dataset.

* **Input:** filename (with context such as extension, directory, application)
* **Output:** natural language description of the file

The training process includes:

1. Loading and preprocessing the dataset
2. Fine-tuning the model (PEFT or full fine-tuning)
3. Evaluating with metrics like ROUGE
4. Comparing with baseline and base models

---

## ✅ Summary of Workflow

1. **Extract properties** → structured JSON (`get_files_proprities.py`)
2. **Generate descriptions** → AI-generated explanations (`scrap_description.py`)
3. **Build final dataset** → clean JSONL (`file-description.py`)
4. **Train model** → fine-tuned model to describe files (`File_desc_full_fine_tune.ipynb`)

