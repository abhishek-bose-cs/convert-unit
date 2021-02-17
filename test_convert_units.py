""" Unit Test unit conversion to SI 
- We are covering 10 test cases in total.
- Test cases for valid arithmatic operator `(t/(d-day))`.
- `min`, `minute` are the same unit and should be treated accordingly.
- `degree?min` treating an invalid expression.
- square involved in SI unit `(t/(minute*hectare))` to `(kg/(s*m\u00b2))`
- Scitific Notation in multiplication_factor.
"""

import unittest
from convert_unit.convert_unit import ConvertUnit

TEST_CASE = [
    {
        "input" : '(degree/minute)',
        "output":
        {
            "multiplication_factor": 0.00029088820866572, 
            "unit_name": "(rad/s)"
        }
    },
    {
        "input" : 'degree',
        "output":
        {
            "multiplication_factor": 0.0174532925199433, 
            "unit_name": "rad"
        }
    },
    {
        "input" : 'min/minute',
        "output":
        {
            "multiplication_factor": 1.0, 
            "unit_name": "s/s"
        }
    },
    {
        "input" : '(degree/(minute*hectare))',
        "output":
        {
            "multiplication_factor": 2.908882087e-08, 
            "unit_name": "(rad/(s*m\u00b2))"
        }
    },
    {
        "input" : 'ha*°',
        "output":
        {
            "multiplication_factor": 174.53292519943295, 
            "unit_name": "m\u00b2*rad"
        }
    },
    {
        "input" : 'min',
        "output":
        {
            "multiplication_factor": 60.0, 
            "unit_name": "s"
        }
    },
    {
        "input" : '(t/(minute*hectare))',
        "output":
        {
            "multiplication_factor":0.00166666666666667,
            "unit_name":"(kg/(s*m\u00b2))"
        }
    },
    {
        "input" : 'rad',
        "output":
        {
            "error": "'rad' is not a valid input unit"
        }
    },
    {
        "input" : 'degree?min',
        "output":
        {
            "error": "Cannot evaluate an invalid expression"
        }
    },
    {
        "input" : '(t/(d-day))',
        "output":
        {
            "error":"Invalid arithmatic operator in input"
        }
    }
]

def test_convert_units(app, client):
    """ test_function for unit conversion to SI """
    for test in TEST_CASE:
        resp = client.get(
            '/units/si?units='+test['input']
        )
        assert resp.get_json() == test['output']
        assert resp.status_code ==200
