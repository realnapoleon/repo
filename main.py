import pickle

choice = int(input('Press 1 to load data or 0 to start over: '))

if choice == 0:
  name1 = str(input('Enter name of lift 1: '))
  nameVal1 = float(input('Enter a value for ' + name1 + ': '))
  tracker1 = 0

  file = open('data1.txt', 'wb')
  pickle.dump(name1, file)
  pickle.dump(nameVal1, file)
  pickle.dump(tracker1, file)
  file.close()
  print('Data saved.')

  name2 = str(input('Enter name of lift 2: '))
  nameVal2 = float(input('Enter a value for ' + name2 + ': '))
  tracker2 = 0

  file = open('data2.txt', 'wb')
  pickle.dump(name2, file)
  pickle.dump(nameVal2, file)
  pickle.dump(tracker2, file)
  file.close()
  print('Data saved.')

  name3 = str(input('Enter name of lift 3: '))
  nameVal3 = float(input('Enter a value for ' + name3 + ': '))
  tracker3 = 0

  file = open('data3.txt', 'wb')
  pickle.dump(name3, file)
  pickle.dump(nameVal3, file)
  pickle.dump(tracker3, file)
  file.close()
  print('Data saved.')

  name4 = str(input('Enter name of lift 4: '))
  nameVal4 = float(input('Enter a value for ' + name4 + ': '))
  tracker4 = 0

  file = open('data4.txt', 'wb')
  pickle.dump(name4, file)
  pickle.dump(nameVal4, file)
  pickle.dump(tracker4, file)
  file.close()
  print('Data saved.')

  name5 = str(input('Enter name of lift 5: '))
  nameVal5 = float(input('Enter a value for ' + name5 + ': '))
  tracker5 = 0

  file = open('data5.txt', 'wb')
  pickle.dump(name5, file)
  pickle.dump(nameVal5, file)
  pickle.dump(tracker5, file)
  file.close()
  print('Data saved.')

  name6 = str(input('Enter name of lift 6: '))
  nameVal6 = float(input('Enter a value for ' + name6 + ': '))
  tracker6 = 0

  file = open('data6.txt', 'wb')
  pickle.dump(name6, file)
  pickle.dump(nameVal6, file)
  pickle.dump(tracker6, file)
  file.close()
  print('Data saved.')

elif choice == 1:
  file = open('data1.txt', 'rb')
  name1 = pickle.load(file)
  nameVal1 = pickle.load(file)
  tracker1 = pickle.load(file)
  file.close()

  progression1 = 5

  file = open('data2.txt', 'rb')
  name2 = pickle.load(file)
  nameVal2 = pickle.load(file)
  tracker2 = pickle.load(file)
  file.close()

  progression2 = 5

  file = open('data3.txt', 'rb')
  name3 = pickle.load(file)
  nameVal3 = pickle.load(file)
  tracker3 = pickle.load(file)
  file.close()

  progression3 = 5

  file = open('data4.txt', 'rb')
  name4 = pickle.load(file)
  nameVal4 = pickle.load(file)
  tracker4 = pickle.load(file)
  file.close()

  progression4 = 5

  file = open('data5.txt', 'rb')
  name5 = pickle.load(file)
  nameVal5 = pickle.load(file)
  tracker5 = pickle.load(file)
  file.close()

  progression5 = 5

  file = open('data6.txt', 'rb')
  name6 = pickle.load(file)
  nameVal6 = pickle.load(file)
  tracker6 = pickle.load(file)
  file.close()

  progression6 = 5

  skip = int(input('Press 1 to log an attempt for ' + name1 + ' or 2 to skip: '))

  if skip == 1:
    print(name1 + ' is ', + nameVal1)
    a1 = int(input('attempt 1. Press 1 if successful or 2 if not: '))
    if a1 == 1:
      counter = 1
    else:
      counter = 0

    a2 = int(input('attempt 2. Press 1 if successful or 2 if not: '))
    if a2 == 1:
      counter = counter + 1

    a3 = int(input('attempt 3. Press 1 if successful or 2 if not: '))
    if a3 == 1:
      counter = counter + 1

    if counter > 2:
      tracker1 = 0
      nameVal1 = nameVal1 + progression1

      file = open('data1.txt', 'wb')
      pickle.dump(name1, file)
      pickle.dump(nameVal1, file)
      pickle.dump(tracker1, file)
      file.close()

      print('Good. Try again next time with ', + nameVal1)

    elif counter < 3:
      tracker1 = tracker1 + 1

      file = open('data1.txt', 'wb')
      pickle.dump(name1, file)
      pickle.dump(nameVal1, file)
      pickle.dump(tracker1, file)
      file.close()

      if tracker1 == 3:
        tracker1 = 1
        nameVal1 = nameVal1 * 0.9

        file = open('data1.txt', 'wb')
        pickle.dump(name1, file)
        pickle.dump(nameVal1, file)
        pickle.dump(tracker1, file)
        file.close()

      print('Try again next time with ', + nameVal1)
  else:
    pass

  skip = int(input('Press 1 to log an attempt for ' + name2 + ' or 2 to skip: '))

  if skip == 1:
    print(name2 + ' is ', + nameVal2)
    a1 = int(input('attempt 1. Press 1 if successful or 2 if not: '))
    if a1 == 1:
      counter = 1
    else:
      counter = 0

    a2 = int(input('attempt 2. Press 1 if successful or 2 if not: '))
    if a2 == 1:
      counter = counter + 1

    a3 = int(input('attempt 3. Press 1 if successful or 2 if not: '))
    if a3 == 1:
      counter = counter + 1

    if counter > 2:
      tracker2 = 0
      nameVal2 = nameVal2 + progression2

      file = open('data2.txt', 'wb')
      pickle.dump(name2, file)
      pickle.dump(nameVal2, file)
      pickle.dump(tracker2, file)
      file.close()

      print('Good. Try again next time with ', + nameVal2)

    elif counter < 3:
      tracker2 = tracker2 + 1

      file = open('data2.txt', 'wb')
      pickle.dump(name2, file)
      pickle.dump(nameVal2, file)
      pickle.dump(tracker2, file)
      file.close()

      if tracker2 == 3:
        tracker2 = 1
        nameVal2 = nameVal2 * 0.9

        file = open('data2.txt', 'wb')
        pickle.dump(name2, file)
        pickle.dump(nameVal2, file)
        pickle.dump(tracker2, file)
        file.close()

      print('Try again next time with ', + nameVal2)
  else:
    pass

  skip = int(input('Press 1 to log an attempt for ' + name3 + ' or 2 to skip: '))

  if skip == 1:
    print(name3 + ' is ', + nameVal3)
    a1 = int(input('attempt 1. Press 1 if successful or 2 if not: '))
    if a1 == 1:
      counter = 1
    else:
      counter = 0

    a2 = int(input('attempt 2. Press 1 if successful or 2 if not: '))
    if a2 == 1:
      counter = counter + 1

    a3 = int(input('attempt 3. Press 1 if successful or 2 if not: '))
    if a3 == 1:
      counter = counter + 1

    if counter > 2:
      tracker3 = 0
      nameVal3 = nameVal3 + progression3

      file = open('data3.txt', 'wb')
      pickle.dump(name3, file)
      pickle.dump(nameVal3, file)
      pickle.dump(tracker3, file)
      file.close()

      print('Good. Try again next time with ', + nameVal3)

    elif counter < 3:
      tracker3 = tracker3 + 1

      file = open('data3.txt', 'wb')
      pickle.dump(name3, file)
      pickle.dump(nameVal3, file)
      pickle.dump(tracker3, file)
      file.close()

      if tracker3 == 3:
        tracker3 = 1
        nameVal3 = nameVal3 * 0.9

        file = open('data3.txt', 'wb')
        pickle.dump(name3, file)
        pickle.dump(nameVal3, file)
        pickle.dump(tracker3, file)
        file.close()

      print('Try again next time with ', + nameVal3)
  else:
    pass

  skip = int(input('Press 1 to log an attempt for ' + name4 + ' or 2 to skip: '))

  if skip == 1:
    print(name4 + ' is ', + nameVal4)
    a1 = int(input('attempt 1. Press 1 if successful or 2 if not: '))
    if a1 == 1:
      counter = 1
    else:
      counter = 0

    a2 = int(input('attempt 2. Press 1 if successful or 2 if not: '))
    if a2 == 1:
      counter = counter + 1

    a3 = int(input('attempt 3. Press 1 if successful or 2 if not: '))
    if a3 == 1:
      counter = counter + 1

    if counter > 2:
      tracker4 = 0
      nameVal4 = nameVal4 + progression4

      file = open('data4.txt', 'wb')
      pickle.dump(name4, file)
      pickle.dump(nameVal4, file)
      pickle.dump(tracker4, file)
      file.close()

      print('Good. Try again next time with ', + nameVal4)

    elif counter < 3:
      tracker4 = tracker4 + 1

      file = open('data4.txt', 'wb')
      pickle.dump(name4, file)
      pickle.dump(nameVal4, file)
      pickle.dump(tracker4, file)
      file.close()

      if tracker4 == 3:
        tracker4 = 1
        nameVal4 = nameVal4 * 0.9

        file = open('data4.txt', 'wb')
        pickle.dump(name4, file)
        pickle.dump(nameVal4, file)
        pickle.dump(tracker4, file)
        file.close()

      print('Try again next time with ', + nameVal4)
  else:
    pass

  skip = int(input('Press 1 to log an attempt for ' + name5 + ' or 2 to skip: '))

  if skip == 1:
    print(name5 + ' is ', + nameVal5)
    a1 = int(input('attempt 1. Press 1 if successful or 2 if not: '))
    if a1 == 1:
      counter = 1
    else:
      counter = 0

    a2 = int(input('attempt 2. Press 1 if successful or 2 if not: '))
    if a2 == 1:
      counter = counter + 1

    a3 = int(input('attempt 3. Press 1 if successful or 2 if not: '))
    if a3 == 1:
      counter = counter + 1

    if counter > 2:
      tracker5 = 0
      nameVal5 = nameVal5 + progression5

      file = open('data5.txt', 'wb')
      pickle.dump(name5, file)
      pickle.dump(nameVal5, file)
      pickle.dump(tracker5, file)
      file.close()

      print('Good. Try again next time with ', + nameVal5)

    elif counter < 3:
      tracker5 = tracker5 + 1

      file = open('data5.txt', 'wb')
      pickle.dump(name5, file)
      pickle.dump(nameVal5, file)
      pickle.dump(tracker5, file)
      file.close()

      if tracker5 == 3:
        tracker5 = 1
        nameVal5 = nameVal5 * 0.9

        file = open('data5.txt', 'wb')
        pickle.dump(name5, file)
        pickle.dump(nameVal5, file)
        pickle.dump(tracker5, file)
        file.close()

      print('Try again next time with ', + nameVal5)
  else:
    pass

  skip = int(input('Press 1 to log an attempt for ' + name6 + ' or 2 to skip: '))

  if skip == 1:
    print(name6 + ' is ', + nameVal6)
    a1 = int(input('attempt 1. Press 1 if successful or 2 if not: '))
    if a1 == 1:
      counter = 1
    else:
      counter = 0

    a2 = int(input('attempt 2. Press 1 if successful or 2 if not: '))
    if a2 == 1:
      counter = counter + 1

    a3 = int(input('attempt 3. Press 1 if successful or 2 if not: '))
    if a3 == 1:
      counter = counter + 1

    if counter > 2:
      tracker6 = 0
      nameVal6 = nameVal6 + progression6

      file = open('data6.txt', 'wb')
      pickle.dump(name6, file)
      pickle.dump(nameVal6, file)
      pickle.dump(tracker6, file)
      file.close()

      print('Good. Try again next time with ', + nameVal6)

    elif counter < 3:
      tracker6 = tracker6 + 1

      file = open('data6.txt', 'wb')
      pickle.dump(name6, file)
      pickle.dump(nameVal6, file)
      pickle.dump(tracker6, file)
      file.close()

      if tracker6 == 3:
        tracker6 = 1
        nameVal6 = nameVal6 * 0.9

        file = open('data6.txt', 'wb')
        pickle.dump(name6, file)
        pickle.dump(nameVal6, file)
        pickle.dump(tracker6, file)
        file.close()

      print('Try again next time with ', + nameVal6)
  else:
    pass

  
