# Random address data generator
Python script to generate random address data. Currently only Dutch naming conventions. Using this to create tests for an address/personal info normalising  tool.

> **If you're reading this, it is probably not useable yet.**

generatedata.com did not seem to cut it for my use case as the data was not going to be representative of actual Dutch address data, as I want to make my program check addresses and postal codes.

## A note on representativeness
Even assuming only wanting to get Dutch data, the names that it generates are from Wikipedia lists. Therefore, some first names are gonna be old and many of them not representative of people with different cultural backgrounds. Last names are mostly from a top 100 Wikipedia list and a short top list of Flemish last names.


## A note on things in general
I am still learning. This will probably be bad.

## Requirements
- Python (made with 3 in mind, would probably work with 2)
- Pandas

## How it works
It randomly generates entries with data in CSVs that I put together. I hope to make this more accurate over time.

## To-do

- [x] Basic name generation
- [ ] Basic address generation
- [ ] Accept command line args
- [ ] Creating different formats
- [ ] Make data representative of CRMs that do not correct data put in by users

