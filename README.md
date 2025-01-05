# Support Ticket Keyword Extractor

This is a short project that I took on to practice data interpretation and visualization. The program analyzes a hypothetical dataset of Fly Delta support tickets, extracts keywords and key phrases from the ticket descriptions (utilizing the RAKE algorithm (https://pypi.org/project/rake-nltk/)), ranks them, and exports the scored exerpts to a spreadsheet.

## Run Locally

Make sure that the latest version of Python is installed
> [!NOTE]
> 3.13.1 is the most recent Python version that has been tested with this program

Clone or download the project onto a desired location on your machine

```bash
  git clone https://github.com/GarySheppard/Support-Ticket-Keyword-Extractor.git
```

Open the command prompt on your machine (simply type "CMD" in your computer's search bar to find it) and navigate to the directory that you chose for the project using the "cd" command

```bash
  cd C:/path/to/project
```

> [!IMPORTANT]
> Make sure that the directory used in the "C:/path/to/project" path is the folder that holds all the project's files

Enter the following command to install all dependencies:

```bash
  pip install -r requirements.txt
```

Run the Python script, noting the "Support Ticket Keywords" spreadsheet that it generates
