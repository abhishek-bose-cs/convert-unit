""" unit conversion to SI unit
- This project takes non-SI unit as an input parameter e.g. `(degree/minute)` and convert to a
valid SI equivalent `(rad/s)`.
- It also compute the mutiplication factor that is involved in the SI conversion.
- **Code Logic**:
    - The code first parse the input expression and fetch all the non SI unit into a list.
    - Then it replace the parsed unit into the SI equivalent thet is defined in local table.
    - It generate the mutiplication factor by replacing the parsed unit into the respective SI
    converted value and form an expression.
    - The expression is evaluated at a later stage to generate the multiplication factor.
- **Edge Cases**:
    - Checks if the input is empty. Error Code: 'Input is empty'
    - Checks for invalid arithmatic operator e.g. `-`,`+`,`%`,`**`. Error Code: 'Invalid
    arithmatic operator in input'
    - Check if the input unit is valid and if it present in our scope. e.g. `kilometer`,
    Error Code: 'kilometer is not a valid input unit'
    - Check if the expression is valid or not. e.g. `(degree/minute/)` is an invalid expression,
    Error Code: 'Cannot evaluate an invalid expression'
-**Time Complexity**:
    - The code hase a liner time complexity O(n) where n is the number of character in the
    input string.
"""

import math
import re

PI = math.pi # Constant for Pi

INVALID_OPR_REG_EX = r'\+|\-|\%|\^|\*\*'
PARSE_UNIT_REG_EX = r'\w+|°|\"|\''

""" Valid input to SI
 This local table converts minute into seconds which is represent by 's' """
INPUT_TO_SI = {
    'minute'     : 's',
    'hour'       : 's',
    'day'        : 's',
    'degree'     : 'rad',
    'arcminute'  : 'rad',
    'arcsecond'  : 'rad',
    'hectare'    : 'm\u00b2',
    'litre'      : 'm\u00b3',
    'tonne'      : 'kg',
    'min'        : 's',
    'h'          : 's',
    'd'          : 's',
    '°'          : 'rad',
    "'"          : 'rad',
    '"'          : 'rad',
    'ha'         : 'm\u00b2',
    'L'          : 'm\u00b2',
    't'          : 'kg'
}

""" Input unit to SI Conversion """
INPUT_TO_SI_MULTPLICATION_FACTOR = {
    'minute'     : 60,
    'hour'       : 3600,
    'day'        : 86400,
    'degree'     : PI/180,
    'arcminute'  : PI/10800,
    'arcsecond'  : PI/648000,
    'hectare'    : 10000,
    'litre'      : 0.001,
    'tonne'      : 1000,
    'min'        : 60,
    'h'          : 3600,
    'd'          : 86400,
    '°'          : PI/180,
    "'"          : PI/10800,
    '"'          : PI/648000,
    'ha'         : 10000,
    'L'          : 0.001,
    't'          : 1000
}

class ConvertUnit:
    """ Class to convert unit to SI """
    def __init__(self, input_str):
        self.response = {}
        self.input = input_str.strip()

    def convert(self):
        """ Function to validate input and unit conversion"""
        is_invalid_operator = self.validate_opr()
        if is_invalid_operator:
            return is_invalid_operator
        parsed_unit_list = self.input_to_unit_list()
        if len(parsed_unit_list) == 0:
            return self.generate_error('Invalid input')
        try:
            si_unit = self.convert_to_si(parsed_unit_list)
        except KeyError as error:
            return self.generate_error(f'{error} is not a valid input unit')
        try:
            mult_exp = self.convert_to_mul_factor(parsed_unit_list)
        except Exception as error:  # pylint: disable=broad-except
            return self.generate_error('Cannot evaluate an invalid expression')
        return self.generate_response(si_unit, mult_exp)

    def convert_to_si(self, str_list):
        """ Generate an equivalent SI expression """
        si_unit = self.input
        for unit in str_list:
            si_unit = self.build_expression(unit, INPUT_TO_SI[unit], si_unit)
        return si_unit

    def convert_to_mul_factor(self, str_list):
        """ Calculate the multiplication factor"""
        mul_exp = self.input
        for unit in str_list:
            mul_exp = self.build_expression(unit, \
                str(INPUT_TO_SI_MULTPLICATION_FACTOR[unit]), mul_exp)
        return eval(mul_exp)  # pylint: disable=eval-used

    def generate_error(self, error):
        """ Error Handler """
        self.response['error'] = error
        return self.response

    def input_to_unit_list(self):
        """ Convert all the input unit into list """
        parsed_unit_list = re.findall(PARSE_UNIT_REG_EX, self.input)
        return parsed_unit_list

    def format_factor(self, factor):  # pylint: disable=no-self-use
        """ Format the multiplication factor"""
        return float("{:.17f}".format(factor))

    def generate_response(self, si_unit, mult_exp):
        """ generate the response json """
        self.response['unit_name'] = si_unit
        self.response['multiplication_factor'] = self.format_factor(mult_exp)
        return self.response

    def validate_opr(self):
        """ Check if input is null or invalid operation e.g. add, sub. """
        invalid_opr = re.findall(INVALID_OPR_REG_EX, self.input)
        if len(self.input) == 0:
            return self.generate_error('Input is empty')
        if invalid_opr:
            return self.generate_error('Invalid arithmatic operator in input')
        return False

    def build_expression(self, unit, si_equivalent, expression):   # pylint: disable=no-self-use
        """ replace word to word to generate SI expression """
        if unit in ['°', '\'', '\"']:
            after_expression = expression.replace(unit, si_equivalent)
        else:
            word_to_word_reg_ex = rf"\b(?=\w){unit}\b(?!\w)"
            after_expression = re.sub(word_to_word_reg_ex, si_equivalent, expression)
        return after_expression
