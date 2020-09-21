#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	ALIGNMENT = 10
	TAX_RATE = 0.15

	sum = 0.0
	for item in data:
		cost = item[INDEX_QUANTITY] * item[INDEX_PRICE]
		sum += cost
	taxes = sum * TAX_RATE
	total = sum + taxes
	return f"{name}" "\n" \
	       f"SOUS TOTAL {sum : >{ALIGNMENT}.2f} $" "\n" \
	       f"TAXES      {taxes : >{ALIGNMENT}.2f} $" "\n" \
	       f"TOTAL      {total : >{ALIGNMENT}.2f} $" "\n"


def format_number(number, num_decimal_digits):
	decimal_part = abs(number) % 1.0
	whole_part = int(abs(number))

	result = f"{decimal_part:.{num_decimal_digits}f}"[1:]
	while whole_part >= 1000:
		result = f" {whole_part % 1000 :0>3}{result}"
		whole_part //= 1000
	result = f"{'-' if number < 0 else ''}{whole_part}{result}"

	return result

def get_triangle(num_rows):
	border_char = "+"
	triangle_char = "A"

	triangle_width = 1 + (num_rows - 1) * 2
	border_row = border_char * (triangle_width + 2)

	result = border_row
	for i in range(num_rows):
		triangle_chars = triangle_char * (i * 2 + 1)
		result += "\n" + f"{border_char}{triangle_chars :^{triangle_width}}{border_char}"
	result += "\n" + border_row

	return result


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
