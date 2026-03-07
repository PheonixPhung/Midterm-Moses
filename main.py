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

  print ("-----")
  print ("Your journey to Egypt was difficult. You are faced with Pharaoh. You have stated, 'Let my people go! The God of Israel has demanded that you free his people!' Pharaoh denied.")
  print ("You can either stand your ground, risking death, or leave, to go home where your children and wife are. Shall you 'stand' or 'comfort'?")
  answer = input("Enter your decision:")

  if answer == "stand":
    print ("Pharaoh attempts to intimidate you with the magic of his Pagan 'gods'. However, God prevails, his power devouring the power of the 'snakes'. You have faced Pharaoh, now you shall exact God's will.")

  elif answer == "comfort":
    print ("Pharoah's slaves escorted you out and took you away. You go home to your wife and kids, your wife embraced you. God, however, did not. His will shall be done, just not through you.")
    print("Your story has ended. Would you like to restart?")
    restart = input("(yes/no): ")
    if restart != "yes":
      break
