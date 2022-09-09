import time

class TrafficLight:
    light = None
    a_count = 0

    def running(self):
        if self.light == None or self.light == "Green":
            self.light = "Red"
            print("The red traffic light is on.\n")
            print("Stop and wait until the traffic light turns green!\n")
            time.sleep(7)

        if self.light == "Red":
            self.light = "Yellow"
            print("The yellow traffic light is on.\n")
            print("Wait until the traffic light turns green, get ready to cross the road.\n")
            time.sleep(2)

        if self.light == "Yellow":
            self.light = "Green"
            print("The green traffic light is on.\n")
            print("he traffic light turned green. You can move!\n")
            time.sleep(10)

        if self.a_count == 10:
            print("What grief! The traffic light is broken!")
            return
        self.a_count = self.a_count + 1
        self.running()

traffic_light = TrafficLight()
traffic_light.running()
