# Convert-Units

This project will perform unit conversion to SI from their “widely used” counterparts.

## Description:
 - This project takes a non-SI unit as an input parameter e.g. `(degree/minute)` and converts it to a valid SI equivalent `(rad/s)`.
 - It also computes the multiplication factor(17 digits after the decimal point) that is involved in the SI conversion.
  ### **Code Logic**: 
  - The code first parse the input expression and fetch all the non-SI unit into a list.
  - Then it replaces the parsed unit into the SI equivalent that is defined in the local table (INPUT_TO_SI).
  - It generates the multiplication factor by replacing the parsed unit into the respective SI converted value and form an expression.
  - The expression is evaluated at a later stage to generate the multiplication factor.
  ### **Edge Cases**:
  - Checks if the input is empty. Error Code: 'Input is empty'
  - Checks for invalid arithmetic operator e.g. `-`,`+`,`%`,`**`. Error Code: 'Invalid arithmetic operator in input'
  - Check if the input unit is valid and if it present in our scope. e.g. `kilometer`, Error Code: 'kilometer is not a valid input unit'
  - Check if the expression is valid or not. e.g. `(degree/minute/)` is an invalid expression, Error Code: 'Cannot evaluate an invalid expression'

## Prerequisite: 
- Make sure **Docker** is installed.
### **Optional**: 
- Python 3.8 is installed to run smoke test using `pytest`
- install pytest using `pip install -r requirements.txt`


## Install (using Docker):

1. Once the repository is pulled from GitHub. `cd` into the `convert-units` directory using Terminal (Mac) or Power shell (Windows).

2. build the docker image
  - if you're on a mac run 
    -`make build`
  - if you're on windows run
    -`docker build . -t 5000:5000 convert-unit:latest`

3. run the docker image
  - if you're on a mac run 
    - `make run` to run in attached mode.
    - `make drun` to run in detached mode.
  - if you're on windows run
    - `docker run --rm -it -p 5000:5000 convert-unit:latest`
     - `--rm` removes the container when the process is stopped
     - `-it` enables tty so you can interact with the docker container with your terminal. To run in detached use option `-d` in place of `-it`
     - `-p 5000:5000` maps your local machine's port 5000 to the docker containers port 5000
     - `convert-unit:latest` is the image name we just created with the tag `latest` which maintain the image version

## Optional: Run automation Test (using pytest):

  ### **Coverage:**
  - We are covering 10 test cases in total.
  - Test cases for valid arithmatic operator `(t/(d-day))`.
  - `min`, `minute` are the same unit and should be treated accordingly.
  - `degree?min` treating an invalid expression.
  - square involved in SI unit `(t/(minute*hectare))` to `(kg/(s*m\u00b2))`
  - Scitific Notation in multiplication_factor.
  - Testing special characters like `°` for degree.
  ### **Steps:**
  - You should be in the root directory `convert-units`
  - Run `make test`
  - You will `PASSED` `[100%]`. This will ensure all the test cases passed.

## Executing the Webservice in any browser:

  - Type `http://localhost:5000/units/si?units=(degree/minute)` hit Enter.
  - Check response:
    ```Python
    {
      "multiplication_factor":0.00029088820866572,
      "unit_name":"(rad/s)"
    }
    ```
