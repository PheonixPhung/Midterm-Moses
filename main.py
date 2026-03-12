while True:

  print ("Welcome to the Possibilities of Moses")
  print ("The bush in front of your feet is burning with flames, yet it's still alive.")
  print ("A voice calls from the burning bush. 'Moses! Moses! Here am I. I am the God of thy father and all those before. I have heard the sorrow of my people. I am calling you to be their saviour.'")
  print ("What shall you do, Moses? Shall you 'flee' or 'follow'")
  answer = input("Enter your decision:")

  if answer == "follow":
    print("You are unsure, yet you stay in the sight of the Lord. For He reassures you, He chose you for a reason, even with all your flaws.")

  elif answer == "flee":
    print("You have run far into the desert. Your name is not heard, and your blessings are taken. Further shall you stray, and your bones and figs rot. Stray Ending")
    print("Your story has ended. Would you like to restart?")
    restart = input("(yes/no): ")
    if restart != "yes":
      break
    else:
      continue


  print ("Your journey to Egypt was difficult. You are faced with Pharaoh. You have stated, 'Let my people go! The God of Israel has demanded that you free his people!' Pharaoh denied.")
  print ("You can either stand your ground, risking death, or leave, to go home where your children and wife are. Shall you 'stand' or 'comfort'?")
  answer = input("Enter your decision:")

  if answer == "stand":
    print ("Pharaoh attempts to intimidate you with the magic of his Pagan 'gods'. However, God prevails.")

  elif answer == "comfort":
    print ("Pharaoh's servants escorted you out and took you away. You go home to your wife and kids.")
    print("Your story has ended. Would you like to restart?")
    restart = input("(yes/no): ")
    if restart != "yes":
      break
    else:
      continue


  print ("Pharaoh has hardened his heart against God and the Israelites.")

  print ("The Nile has turned to blood.")
  print ("Shall you show them 'mercy' or 'continue'?")
  answer = input("Enter your decision:")

  if answer == "continue":
    print ("You proceed with God's will.")

  elif answer == "mercy":
    print ("There is no rest for the wicked.")
    print("Your story has ended. Would you like to restart?")
    restart = input("(yes/no): ")
    if restart != "yes":
      break
    else:
      continue


  print ("The second plague begins. Frogs cover Egypt.")
  print ("Will your 'mercy' prevail or shall you let them 'suffer'?")
  answer = input("Enter your decision:")

  if answer == "mercy":
    print ("You ask God for mercy.")

  elif answer == "suffer":
    print ("The plagues continue.")


  print ("Lice and flies plague Egypt.")

  print ("Pharaoh says your people can go if God stops the plagues.")
  print ("Do you 'believe' him or 'proceed'?")
  answer = input("Enter your decision:")

  if answer == "believe":
    print ("Pharaoh lied.")

  elif answer == "proceed":
    print ("Disease spreads among livestock.")


  print ("God commands you to spread ashes across Egypt.")
  print ("Boils break out on the Egyptians.")

  print ("God has assigned you another task. Announce the plagues.")

  plagues = ["Hail", "Locust", "Darkness"]
  for x in plagues:
    print(x)


  print ("The Egyptians cry out for mercy.")
  print ("Do they deserve 'mercy' or shall you 'proceed'?")
  answer = input("Enter your decision:")

  if answer == "proceed":
    print ("The final plague begins.")

  elif answer == "mercy":
    print ("You leave God's will.")


  print ("Mark the doors with lamb's blood.")

  print ("The angel of death passes through Egypt.")

  deaths = ["Cry of the Babies", "Wail of the Parents", "Weep people of Egypt"]
  for x in deaths:
    print(x)


  print ("Pharaoh tells the Israelites to leave Egypt.")

  print ("But Pharaoh changes his mind and chases you.")

  print ("Do you 'persevere' or 'go'?")
  answer = input("Enter your decision:")

  if answer == "persevere":
    print ("You trust God.")

  elif answer == "go":
    print ("You abandon leadership.")


  print ("Moses! Hold out your staff!")
  answer = input("Do as God commands:")

  if answer == "hold":
    print ("The Red Sea parts.")


  print ("The sea collapses on the Egyptians.")
  print ("Praise the Lord of the Hebrews!")

  print("Your story has ended. Would you like to restart?")
  restart = input("(yes/no): ")

  if restart != "yes":
    break
