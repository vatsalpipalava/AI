Domains
name=string
address=string
age=integer
title=string
author=string
publisher=symbol

Predicates
author (name, address, age)
publisher (name, address)
book (title, author, publisher)

Clauses
author ("Vidhi","Surat",20).
author ("Preet","Mumbai",21).
author ("Parth","Mumbai",21).

publisher ("Honey", "Baroda").
publisher ("Liza", "Rajkot").
publisher ("Krishna", "Ahmedabad").

book ("Secrets", "Preet", "Honey").
book ("Warmth", "Vidhi", "Liza").
book ("lies", "Parth", "Krishna").