from s3v2 import * # from wafflehouse import * means the function can be used as globals (all globals in that file/lib become globals for me too) I can use wafflehouse's pancake() function just by calling pancake(x) ... if I used import wafflehouse I have access to the file/lib's functions, but not as globals, so I need to associate them with wafflehouse, so to call the pancake() function I would need to use: wafflehouse.pancake(x). General rule of thumb: use import instead of from X import * because import alone keeps my globals less cluttered and makes my code more clearly readable (as I know where the functions and variables came from that I'm referencing). More here: http://stackoverflow.com/questions/5124232/what-is-the-difference-between-import-modx-and-from-modx-import


gucci_ties = filter_col_by_string(data_from_csv, 'brandName', 'Gucci')
jcrew_ties = filter_col_by_string(data_from_csv, 'brandName', 'J.Crew') # this wasn't working because the brand name for J. Crew is "J.Crew" not "J. Crew". It seems like these sorts of errors are common when you're working with a new data_set. Isn't munging about removing formatting and otherwise making these sorts of errors less likely?

max_gucci = find_max(gucci_ties[1:], 2)
max_jcrew = find_max_min(jcrew_ties[1:], 2)


avg_gucci = find_average(gucci_ties[1:]) # if find_average assumes that the header = False, why are we slicing the list past the first row, isn't the first row actual data in this instance? ... oh, because in gucci_ties[0] is the header, and the find_average() function isn't expecting that row, so we need to skip over it. Got it. 
avg_jcrew = find_average(jcrew_ties[1:])

striped_ties = filter_col_by_string(data_from_csv, 'print', '_striped')
print_ties = filter_col_by_string(data_from_csv, 'print', '_print')
paisley_ties = filter_col_by_string(data_from_csv, 'print', '_paisley')
solid_ties = filter_col_by_string(data_from_csv, 'print', '_solid')

avg_striped = find_average(striped_ties[1:])
avg_print = find_average(print_ties[1:])
avg_paisley = find_average(paisley_ties[1:])
avg_solid = find_average(solid_ties[1:])


breakline = "-" * 10
message = "{} {} tie price is ${:03.2f}"
message2 = "{}\t\t${:03.2f}"
# print(breakline)
# print(message.format("Maximum", "Gucci", max_gucci))
# print(message.format("Maximum", "J.Crew", max_jcrew))
# print(breakline)
# print(message.format("Average", "Gucci", avg_gucci))
# print(message.format("Average", "J.Crew", avg_jcrew))
# print(breakline)
# print("Print\t\tAverage")
# print(message2.format("striped", find_average(striped_ties[1:])))
# print(message2.format("print", find_average(print_ties[1:])))
# print(message2.format("paisley", find_average(paisley_ties[1:])))
# print(message2.format("solid", find_average(solid_ties[1:])))
# print(breakline)


# print(avg_gucci) # test for myself to understand why we were slicing past the header row when using the find_average() function

# print(gucci_ties[:2]) # test for myself to understand why we were slicing past the header row when using the find_average() function

# print(gucci_ties[:2]) # this how you slice into a list to return only some of the results. In this case the first two rows. I used this originally to take a look at the jcrew_ties list. I found that we only had a header row, which meant that the list wasn't populated with data. So I looked directaly at the csv file and noticed the brand name didn't have a space between J. and Crew (i.e. "J.Crew" NOT "J. Crew")