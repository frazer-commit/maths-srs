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

- [x] **v1.0 Basic Structure**
  - [x] Paper class
  - [x] Pair (Quesiton Paper + Markscheme) class

- [x] **v1.1 Question generation**
  - [x] Question template
  - [x] 2 Initial questions
    - [x] Question generation
    - [x] Answer generation

- [x] **v1.2 Classificaiton**
  - [x] Registry for question
  - [x] JSON settings
  - [x] Writing to CSV

- [ ] **v1.3 First Spaced Repetition**
  - [ ] Timestamp for due dates of questions
  - [ ] More questions
  - [ ] Day generation
  - [ ] Spaced Repetition Algorithm

- [ ] **v1.4 Other**
  - [ ] tkinter interface for marking
  - [ ] Dependency heirarchies in algorithm

## AI Note

All code was written by **myself**. Generative AI was used **solely** for code suggestions and bug finding.
