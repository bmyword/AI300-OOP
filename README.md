## AI300 Lesson 4: OOP Practice

_Worked solutions for AI300 Lesson 4
Take-Home Practice_

### Important Notes

* Worked solutions are meant as a guide. There are no correct or wrong answers in OOP, only guiding principles.
* Coding best practices are also integrated, which have been documented in comments. (e.g. input validation, abstract interfaces)
  - Don't be alarmed if some aspects have not been explicitly covered in class, as the intent to stretch and challenge students of all levels.
* How to use this codebase
  - Use it as a starting point for your future practice (and capstone)
  - Implement features incrementally on a "need-to" basis e.g. start with data loading features, and once you get to model implementation, start with `train()` and use `pass` for un-implemented methods until you get to them.
  - Strive to reproduce the implementation from scratch as far as possible. Refrain from copy-pasting code chunks unless you truly understand them! (Except `DBDataLoader` which contains [boilerplate code](https://g.co/kgs/KmVdPG) for interacting with MySQLServer)

Feel free to reach out to your instructor team if you face issues or have follow-up questions.

### Setup Instructions

1. Env setup

In the project root directory, create a file `.env` with the contents below:
```text
DB_HOST=<heicoders_hosted_db_for_AI300>
DB_NAME=playground
DB_USER=<username>
DB_PWD=<password>
```

Please reach out to the AI300 instructor team for environment secrets such as `DB_HOST`, `DB_USER`, `DB_PWD` if you wish to access the AI300 remote database hosted by Heicoders.

Alternatively, you are welcome to setup the same database on your localhost using the `create_loans_dataset.sql` script found on your eLearn.

2. Create virtual environment & install dependencies

_Note: Set your default Python Interpreter to Anaconda base environment, instead of other installed Python executables. If you're unsure how to do so, see Appendix._

Open a Terminal within Visual Studio Code and ensure you are in the project root directory.

Run the commands below to install package dependencies

```bash
pip install -r requirements.txt
```

_(Bonus: Try to do the above in a virtual environment; see Appendix)_

### Appendix

#### Set Python Default Interpreter to Anaconda Python (base)

1. Open Command Palette in Visual Studio Code (Or Ctrl/Cmd+Shift+P)
2. Type `Python: Select Interpreter` and select option
3. Select the interpeter whose path ends with `anaconda3/python.exe`


#### Create Virtual Environment

1. If you have not installed `virtualenv`, run `pip install virtualenv` in your Terminal
2. Ensure you're in your project root directory.
3. To create a new virtual environment called `venv`
```bash
virtualenv venv
```
4. To activate virtual environment, run the appropriate command
- `source venv/bin/activate` on macOS and Linux
- `source venv/Scripts/activate` on Windows (using Git Bash Terminal)
- `venv\Scripts\activate` on Windows (using Command Prompt)
5. Once activated, you will notice that your terminal prompt is prefixed with `(venv)`, which indicates you are now working within the virtual environment. Congrats!
