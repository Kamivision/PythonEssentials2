# From Section 2.4

# Objectives
# improving the student's skills in operating with strings;
# using strings to represent non-text data.

# Scenario
# You've surely seen a seven-segment display.

# It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

# Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

# Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

# Note: the number 8 shows all the LED lights on.

# Your code has to display any non-negative integer number entered by the user.

# Tip: using a list containing patterns of all ten digits may be very helpful.
lights = { 
          '0': ('###', '# #', '# #', '# #', '###'),
          '1': ('  #', '  #', '  #', '  #', '  #'),
          '2': ('###', '  #', '###', '#  ', '###'),
          '3': ('###', '  #', '###', '  #', '###'),
          '4': ('# #', '# #', '###', '  #', '  #'),
          '5': ('###', '#  ', '###', '  #', '###'),
          '6': ('###', '#  ', '###', '# #', '###'),
          '7': ('###', '  #', '  #', '  #', '  #'),
          '8': ('###', '# #', '###', '# #', '###'),
          '9': ('###', '# #', '###', '  #', '###'),
          '.': ('   ', '   ', '   ', '   ', '  #'),
          }
# print(digits[0] + digits[2])

def led_display(number):
  num = str(number)
  #convert to list of 5 tuples based on given number
  digits = [lights[d] for d in num]
  # print(digits)
  for i in range(5):
      print("  ".join(segment[i] for segment in digits))
  return   

led_display(int(input("Enter the number you wish to display: ")))
  

# digits = [ '1111110',  	# 0
# 	   '0110000',	# 1
# 	   '1101101',	# 2
# 	   '1111001',	# 3
# 	   '0110011',	# 4
# 	   '1011011',	# 5
# 	   '1011111',	# 6
# 	   '1110000',	# 7
# 	   '1111111',	# 8
# 	   '1111011',	# 9
# 	   ]


# def led_number(num):
#     # Write the function here.


# led_number(int(input("Enter the number you wish to display: ")))
