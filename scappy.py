import pyautogui
import random
from random import uniform
from time import sleep, time
pyautogui.FAILSAFE = True



def getRandomCoordinate(position):
    top, left, width, height = position
    topLeft = [top, left]
    bottomRight = [top + width, left + height]

    x1 = topLeft[0]
    y1 = topLeft[1]
    x2 = bottomRight[0]
    y2 = bottomRight[1]

    randX = random.randint(x1, x2)
    randY = random.randint(y1, y2)

    return [randX, randY]

try:
    
    print("starting..")
    sleep(3)
    count = 0
    countTime = 0

    while True:
        lobsters = list(pyautogui.locateAllOnScreen("Lobster.png", confidence=0.99))
        R5 = 13
        foody = random.randint(38, 42)
        X = random.randint(155, 165)
        Y = random.randint(224, 234)
        moneyX = random.randint(651, 659)
        moneyY = random.randint(289, 295)
        pyautogui.moveTo(X, Y)

        sleep(uniform(1.01, 2.5))
        pyautogui.click()
        
        count = count + 1
        print("Click Counter:")
        print(count)
        countTime = countTime + 1
        print("Food Timer:")
        print(countTime)

        if R5==count:
            pyautogui.moveTo(moneyX, moneyY)
            pyautogui.click()
            pyautogui.click()
            sleep(uniform(0.01, 0.3))
            pyautogui.click()
            count = 0
            print(count)

        if countTime>foody:
            if len(lobsters) > 0:
                print("Searching food..")
                print(len(lobsters))
                x, y = getRandomCoordinate(lobsters[0])
                pyautogui.moveTo(x, y)
                pyautogui.click()
                pyautogui.click()
                pyautogui.moveTo(x, y)
                pyautogui.click()
                pyautogui.moveTo(x, y)
                pyautogui.click()
                print("yummy lobby!")
                countTime = 0
            else: 
                print("no food!")
                break

except pyautogui.FailSafeException:
    exit("Failsafe TRIGGERED")