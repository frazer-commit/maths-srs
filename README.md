# Maths SRS

Daily worksheet and markscheme generator for maths questions using spaced repetition to prevent forgeting concepts.

## Getting started

### Prerequisites
* Python 3.10+

### Installation

1. Clone the repo:
  ```bash
  git clone https://github.com/frazer-commit/maths-srs
  cd maths-srs
  ```

2. Create a virtual environment
  * macOS / Linux:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
  * Windows:
    ```cmd
    python -m venv .venv
    .venv/Scripts/activate
    ```

3. Inststall dependencies
  ```bash
  pip install -r requirements.txt
  ```

4. Unfinished

## Roadmap

- [ ] **v1.0 Basic Structure**
  - [ ] Markscheme class
  - [ ] Pair (Quesiton Paper + Markscheme) class

- [ ] **v1.1 Question generation**
  - [ ] Question template
  - [ ] 2 Initial questions (addition, multiplication)
    - [ ] Question generation in Matplotlib
    - [ ] Answer generation in Matplotlib

- [ ] **v1.2 Classificaiton**
  - [ ] Registry for question
  - [ ] JSON settings
  - [ ] Pandas timestamp saving
  - [ ] Writing to CSV

- [ ] **v1.3 First Spaced Repetition**
  - [ ] Ease factor for questions
  - [ ] Day generation
  - [ ] Concept heirarchies

## AI Note

All code was written by **myself**. Generative AI was used **soley** for code suggestions and bug finding.
