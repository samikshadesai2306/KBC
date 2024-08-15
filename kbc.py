questions = [
  [
    "What is DBMS?", "database management", "system database management", "management database system",
    "database maangement syatem", "None", 4
  ],
  [
    "What is a relation in RDBMS?", "key", "Table", "Row",
    "Data type", "None", 2
  ],
  [
    " What is an RDBMS?", "Database that stores data elements that are not linked", "Database that accesses data elements that are not linked", "Database that stores and allows access to data elements that are linked",
    "None of the mentioned", "None", 3
  ],
  [
    "Does RDBMS have ACID properties?", "Follows ACID properties", "Doesn’t follow ACID properties", "Depends on the data stored in the database",
    "Can’t say", "None", 3
  ],
  [
    "Which of the following constraints RDBS doesn’t check before creating the tables?", " Not null", "Primary keys", "Data Structure",
    "Data integrity", "None", 3
  ],
  [
    "Which of the following commands do we use to delete a relation (RDBMS) from a database?", "delete table RDBMS", "drop table RDBMS", "delete from RDBMS",
    "drop relation RDBMS", "None", 2
  ],
  [
    "________ deletes a data item from a database.", "Insert(RDBMS)", "Drop(RDBMS)", "Drop(RDBMS)",
    "None of abow", "None", 3
  ],
  [
    ". ________ is a predicate that we expect the database to always satisfy", "Reason", "Mandate", "Assertion",
    "Verify", "None", 3
  ],
  [
    "Which of the following is a good database management practice?", "Adding redundant attributes", "Not specifying primary keys", " Removing redundant attributes",
    "None of the mentioned", "None", 3
  ],
  [
    "Which of the following information does the database system catalog store?", " Number of blocks", "Size of a tuple of a relation", " Number of tuples",
    "All of the mentioned", "None", 4
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):

  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")