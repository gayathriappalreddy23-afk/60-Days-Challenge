import re

text = "Python is a Programming language.It is easy to learn and understand."
result = re.match("Python", text)
print("Text:", text)
print("\n\nMatching: ")
print("\nMatching 'Python' at start:", "Found standard match ->", result.group() if result else "No match")
result2 = re.match("Programming", text)
print("\nMatching 'Programming' at start:", "Found standard match ->", result2.group() if result2 else "No match")

print("\n\nSearching: ")
result3 = re.search("Programming", text)
print("\nSearching for 'Programming':", "Found substring match ->", result3.group() if result3 else "No match")
result4 = re.search("learn", text)
print("\nSearching for 'learn':", "Found substring match ->", result4.group() if result4 else "No match")

print("\n\nFindall : ")
st = "Cat bat mat rat children"
res = re.findall("at", st)
print("\nFindall 'at' occurrences:", res)

print("\n\nFindIter 'at' positions:")
for i in re.finditer("at", st):
    print("\nIndex starting at:", i.start(), "| Value extracted:", i.group())
    
st2 = "Today is Sunday"
print("Original text:", st2)
result5 = re.sub("Sunday", "Monday", st2)
print("\n\nSub replaced text output:", result5)

st3 = "Apple,Banana,Mango,Grapes"
result6 = re.split(",", st3)
print("\n\nSplit data array list output:", result6)

pattern = re.compile(r"\d+")
result7 = pattern.findall("Age 20 Roll 101")
print("\n\nCompile pattern reusing array lookup output:", result7)


print("\n\n--- Pattern concept: Any character except newline (cat.) ---")
pattern2 = r"cat."
match1 = re.match(pattern2, "cats")
print("Matching 'cat.' against 'cats':", "Match Confirmed ->", match1.group() if match1 else "No match")
match2 = re.match(pattern2, "cat is walking")
print("Matching 'cat.' against 'cat is walking':", "Match Confirmed ->", match2.group() if match2 else "No match")
match3 = re.match(pattern2, "cat")
print("Matching 'cat.' against 'cat':", "Match Confirmed ->", match3.group() if match3 else "No match")
match4 = re.match(pattern2, "t")
print("Matching 'cat.' against 't':", "Match Confirmed ->", match4.group() if match4 else "No match")


print("\n\n--- Pattern concept: Start of string (^The) ---")
pattern3 = r"^The"
match5 = re.match(pattern3, "The end is near")
print("Matching '^The' against 'The end is near':", "Match Confirmed ->", match5.group() if match5 else "No match")
match6 = re.match(pattern3, "Today is the holiday")
print("Matching '^The' against 'Today is the holiday':", "Match Confirmed ->", match6.group() if match6 else "No match")


print("\n\n--- Pattern concept: 0 or more times (ca*) ---")
pattern4 = r"ca*"
match7 = re.match(pattern4, "ca")
print("Matching 'ca*' against 'ca':", "Match Confirmed ->", match7.group() if match7 else "No match")
match8 = re.match(pattern4, "cat")
print("Matching 'ca*' against 'cat':", "Match Confirmed ->", match8.group() if match8 else "No match")
match9 = re.match(pattern4, "cats")
print("Matching 'ca*' against 'cats':", "Match Confirmed ->", match9.group() if match9 else "No match")
match10 = re.match(pattern4, "catts")
print("Matching 'ca*' against 'catts':", "Match Confirmed ->", match10.group() if match10 else "No match")
match11 = re.match(pattern4, "The end is cat")
print("Matching 'ca*' against 'The end is cat':", "Match Confirmed ->", match11.group() if match11 else "No match")


print("\n\n--- Pattern concept: 1 or more times (ca+t) ---")
pattern4_plus = r"ca+t"
match12 = re.match(pattern4_plus, "ca")
print("Matching 'ca+t' against 'ca':", "Match Confirmed ->", match12.group() if match12 else "No match")
match13 = re.match(pattern4_plus, "cat")
print("Matching 'ca+t' against 'cat':", "Match Confirmed ->", match13.group() if match13 else "No match")
match14 = re.match(pattern4_plus, "cats")
print("Matching 'ca+t' against 'cats':", "Match Confirmed ->", match14.group() if match14 else "No match")
match15 = re.match(pattern4_plus, "catts")
print("Matching 'ca+t' against 'catts':", "Match Confirmed ->", match15.group() if match15 else "No match")
match16 = re.match(pattern4_plus, "ct")
print("Matching 'ca+t' against 'ct':", "Match Confirmed ->", match16.group() if match16 else "No match")


print("\n\n--- Pattern concept: End of string (end$) ---")
pattern_end = r"end$"
search1 = re.search(pattern_end, "This is the end")
print("Searching 'end$' in 'This is the end':", "Substring found at end ->", search1.group() if search1 else "No match")
search2 = re.search(pattern_end, "The end is near.")
print("Searching 'end$' in 'The end is near.':", "Substring found at end ->", search2.group() if search2 else "No match")


print("\n\n--- Pattern concept: 0 or 1 time optional (cats?) ---")
pattern_opt = r"cats?"
match17 = re.match(pattern_opt, "cat")
print("Matching 'cats?' against 'cat':", "Match Confirmed ->", match17.group() if match17 else "No match")
match18 = re.match(pattern_opt, "cats")
print("Matching 'cats?' against 'cats':", "Match Confirmed ->", match18.group() if match18 else "No match")
match19 = re.match(pattern_opt, "catss")
print("Matching 'cats?' against 'catss':", "Match Confirmed ->", match19.group() if match19 else "No match")


print("\n\n--- Pattern concept: Two consecutive digits (\\d\\d) ---")
pattern_digits = r"\d\d"
match20 = re.match(pattern_digits, "42")
print("Matching '\\d\\d' against '42':", "Match Confirmed ->", match20.group() if match20 else "No match")
match21 = re.match(pattern_digits, "7A")
print("Matching '\\d\\d' against '7A':", "Match Confirmed ->", match21.group() if match21 else "No match")


print("\n\n--- Pattern concept: Non-digits (\\D) ---")
pattern_nondigit = r"\D"
match22 = re.match(pattern_nondigit, "A")
print("Matching '\\D' against 'A':", "Match Confirmed ->", match22.group() if match22 else "No match")
match23 = re.match(pattern_nondigit, "5")
print("Matching '\\D' against '5':", "Match Confirmed ->", match23.group() if match23 else "No match")
match24 = re.match(pattern_nondigit, "_")
print("Matching '\\D' against '_':", "Match Confirmed ->", match24.group() if match24 else "No match")
match25 = re.match(pattern_nondigit, ".")
print("Matching '\\D' against '.':", "Match Confirmed ->", match25.group() if match25 else "No match")


print("\n\n--- Pattern concept: Word characters (\\w) ---")
pattern_word = r"\w"
match26 = re.match(pattern_word, "x")
print("Matching '\\w' against 'x':", "Match Confirmed ->", match26.group() if match26 else "No match")
match27 = re.match(pattern_word, "_")
print("Matching '\\w' against '_':", "Match Confirmed ->", match27.group() if match27 else "No match")
match28 = re.match(pattern_word, "!")
print("Matching '\\w' against '!':", "Match Confirmed ->", match28.group() if match28 else "No match")


print("\n\n--- Pattern concept: Non-word characters (\\W) ---")
pattern_nonword = r"\W"
match29 = re.match(pattern_nonword, "!")
print("Matching '\\W' against '!':", "Match Confirmed ->", match29.group() if match29 else "No match")
match30 = re.match(pattern_nonword, "m")
print("Matching '\\W' against 'm':", "Match Confirmed ->", match30.group() if match30 else "No match")


print("\n\n--- Pattern concept: Whitespace (apple\\sorange) ---")
pattern_space = r"apple\sorange"
match31 = re.match(pattern_space, "apple orange")
print("Matching 'apple\\sorange' against 'apple orange':", "Match Confirmed ->", match31.group() if match31 else "No match")
match32 = re.match(pattern_space, "appleorange")
print("Matching 'apple\\sorange' against 'appleorange':", "Match Confirmed ->", match32.group() if match32 else "No match")


print("\n\n--- Pattern concept: Non-whitespace (\\S) ---")
pattern_nonspace = r"\S"
match33 = re.match(pattern_nonspace, "H")
print("Matching '\\S' against 'H':", "Match Confirmed ->", match33.group() if match33 else "No match")
match34 = re.match(pattern_nonspace, " ")
print("Matching '\\S' against ' ':", "Match Confirmed ->", match34.group() if match34 else "No match")


print("\n\n--- Pattern concept: Any single character listed ([cr]at) ---")
pattern_set = r"[cr]at"
match35 = re.match(pattern_set, "cat")
print("Matching '[cr]at' against 'cat':", "Match Confirmed ->", match35.group() if match35 else "No match")
match36 = re.match(pattern_set, "rat")
print("Matching '[cr]at' against 'rat':", "Match Confirmed ->", match36.group() if match36 else "No match")
match37 = re.match(pattern_set, "bat")
print("Matching '[cr]at' against 'bat':", "Match Confirmed ->", match37.group() if match37 else "No match")


print("\n\n--- Pattern concept: Negated list ([^bc]at) ---")
pattern_negset = r"[^bc]at"
match38 = re.match(pattern_negset, "hat")
print("Matching '[^bc]at' against 'hat':", "Match Confirmed ->", match38.group() if match38 else "No match")
match39 = re.match(pattern_negset, "cat")
print("Matching '[^bc]at' against 'cat':", "Match Confirmed ->", match39.group() if match39 else "No match")


print("\n\n--- Pattern concept: Exact repetitions (^\\d{3}$) ---")
pattern_exact = r"^\d{3}$"
match40 = re.match(pattern_exact, "123")
print("Matching '^\\d{3}$' against '123':", "Match Confirmed ->", match40.group() if match40 else "No match")
match41 = re.match(pattern_exact, "1234")
print("Matching '^\\d{3}$' against '1234':", "Match Confirmed ->", match41.group() if match41 else "No match")


print("\n\n--- Pattern concept: Repeating range (^A{2,4}$) ---")
pattern_range = r"^A{2,4}$"
match42 = re.match(pattern_range, "AAA")
print("Matching '^A{2,4}$' against 'AAA':", "Match Confirmed ->", match42.group() if match42 else "No match")
match43 = re.match(pattern_range, "AAAAA")
print("Matching '^A{2,4}$' against 'AAAAA':", "Match Confirmed ->", match43.group() if match43 else "No match")


print("\n\n--- Pattern concept: Targeted string analysis ---")
email = "student123@gmail.com"
email_pattern = r"^student"
match44 = re.match(email_pattern, email)
print("Regex Expression string targeted:", email_pattern)


#output
Text: Python is a Programming language.It is easy to learn and understand.


Matching: 

Matching 'Python' at start: Found standard match -> Python

Matching 'Programming' at start: Found standard match -> No match


Searching: 

Searching for 'Programming': Found substring match -> Programming

Searching for 'learn': Found substring match -> learn


Findall : 

Findall 'at' occurrences: ['at', 'at', 'at', 'at']


FindIter 'at' positions:

Index starting at: 1 | Value extracted: at

Index starting at: 5 | Value extracted: at

Index starting at: 9 | Value extracted: at

Index starting at: 13 | Value extracted: at
Original text: Today is Sunday


Sub replaced text output: Today is Monday


Split data array list output: ['Apple', 'Banana', 'Mango', 'Grapes']


Compile pattern reusing array lookup output: ['20', '101']


--- Pattern concept: Any character except newline (cat.) ---
Matching 'cat.' against 'cats': Match Confirmed -> cats
Matching 'cat.' against 'cat is walking': Match Confirmed -> cat 
Matching 'cat.' against 'cat': Match Confirmed -> No match
Matching 'cat.' against 't': Match Confirmed -> No match


--- Pattern concept: Start of string (^The) ---
Matching '^The' against 'The end is near': Match Confirmed -> The
Matching '^The' against 'Today is the holiday': Match Confirmed -> No match


--- Pattern concept: 0 or more times (ca*) ---
Matching 'ca*' against 'ca': Match Confirmed -> ca
Matching 'ca*' against 'cat': Match Confirmed -> ca
Matching 'ca*' against 'cats': Match Confirmed -> ca
Matching 'ca*' against 'catts': Match Confirmed -> ca
Matching 'ca*' against 'The end is cat': Match Confirmed -> No match


--- Pattern concept: 1 or more times (ca+t) ---
Matching 'ca+t' against 'ca': Match Confirmed -> No match
Matching 'ca+t' against 'cat': Match Confirmed -> cat
Matching 'ca+t' against 'cats': Match Confirmed -> cat
Matching 'ca+t' against 'catts': Match Confirmed -> cat
Matching 'ca+t' against 'ct': Match Confirmed -> No match


--- Pattern concept: End of string (end$) ---
Searching 'end$' in 'This is the end': Substring found at end -> end
Searching 'end$' in 'The end is near.': Substring found at end -> No match


--- Pattern concept: 0 or 1 time optional (cats?) ---
Matching 'cats?' against 'cat': Match Confirmed -> cat
Matching 'cats?' against 'cats': Match Confirmed -> cats
Matching 'cats?' against 'catss': Match Confirmed -> cats


--- Pattern concept: Two consecutive digits (\d\d) ---
Matching '\d\d' against '42': Match Confirmed -> 42
Matching '\d\d' against '7A': Match Confirmed -> No match


--- Pattern concept: Non-digits (\D) ---
Matching '\D' against 'A': Match Confirmed -> A
Matching '\D' against '5': Match Confirmed -> No match
Matching '\D' against '_': Match Confirmed -> _
Matching '\D' against '.': Match Confirmed -> .


--- Pattern concept: Word characters (\w) ---
Matching '\w' against 'x': Match Confirmed -> x
Matching '\w' against '_': Match Confirmed -> _
Matching '\w' against '!': Match Confirmed -> No match


--- Pattern concept: Non-word characters (\W) ---
Matching '\W' against '!': Match Confirmed -> !
Matching '\W' against 'm': Match Confirmed -> No match


--- Pattern concept: Whitespace (apple\sorange) ---
Matching 'apple\sorange' against 'apple orange': Match Confirmed -> apple orange
Matching 'apple\sorange' against 'appleorange': Match Confirmed -> No match


--- Pattern concept: Non-whitespace (\S) ---
Matching '\S' against 'H': Match Confirmed -> H
Matching '\S' against ' ': Match Confirmed -> No match


--- Pattern concept: Any single character listed ([cr]at) ---
Matching '[cr]at' against 'cat': Match Confirmed -> cat
Matching '[cr]at' against 'rat': Match Confirmed -> rat
Matching '[cr]at' against 'bat': Match Confirmed -> No match


--- Pattern concept: Negated list ([^bc]at) ---
Matching '[^bc]at' against 'hat': Match Confirmed -> hat
Matching '[^bc]at' against 'cat': Match Confirmed -> No match


--- Pattern concept: Exact repetitions (^\d{3}$) ---
Matching '^\d{3}$' against '123': Match Confirmed -> 123
Matching '^\d{3}$' against '1234': Match Confirmed -> No match


--- Pattern concept: Repeating range (^A{2,4}$) ---
Matching '^A{2,4}$' against 'AAA': Match Confirmed -> AAA
Matching '^A{2,4}$' against 'AAAAA': Match Confirmed -> No match


--- Pattern concept: Targeted string analysis ---
Regex Expression string targeted: ^student
Evaluating pattern match output against variable: Match Confirmed -> student

=== Code Execution Successful ===
print("Evaluating pattern match output against variable:", "Match Confirmed ->", match44.group() if match44 else "No match")
