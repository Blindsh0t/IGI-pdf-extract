## About
Extract info from IGI's pdf certificate. Currently working with two types of certificate, ideally would like to add a lot of features.

## Project
1. Gets all PDF from a folder
2. Reads them one by one and gets important fields
3. Saves in 'Master' csv


## Types of Certificate it works with
> Type 1
![Report: Type 1](resources/example_cert1.png)

> Type 2
![Report: Type 2](resources/example_cert2.png)

## Requirements
- pip install `PyPDF2=1.26.0`

## Unfulfilled 
- [ ] Faced problems when report format was updated in 2021
- [ ] Even in Type 1, not all length of fields were consistent; which messes up data extraction & uniformity
- [ ] Should have used list indexs to get the data
- [ ] Manually replaced / changed data to get required fields