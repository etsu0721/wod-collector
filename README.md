# WoD Collector

## Word of the Day (WoD) data pipeline into an Anki deck
WoD Collector is a data pipeline ingesting a word of the day and adding it to an Anki deck. A scraper automatically collects word of the day data daily from [wordnik](https://www.wordnik.com/word-of-the-day) via a cron job calling a shell script that calls a Python scaper script, which does the heavy lifting. 

* [ ] Hop on the pipe end (link to Anki deck).

## Tools
* **Python** for web data extraction, data processing
* [**Anki**](https://apps.ankiweb.net) as a free and open-source flashcard program using spaced repetition, a technique from cognitive science for fast and long-lasting memorization [(“Anki (Software)”, Wikipedia)](en.wikipedia.org/wiki/Anki_(software))
* **cron** to schedule a time each day for the pipeline to do its thing

## Contributors
* Eli Sutton, elisutton0721@gmail.com
