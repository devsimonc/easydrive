def sonicCheck(self):
        while ja=="true":
            time.sleep(0.333)
            GPIO.output(self.config["trigger"], True)
            time.sleep(0.00001)
            GPIO.output(self.config["trigger"], False)
            start = time.time()
            while GPIO.input(self.config["echo"])==0:
                start = time.time()
            while GPIO.input(self.config["echo"])==1:
                stop = time.time()
            elapsed = stop-start
            measure = int((elapsed * 34300)/2)
            self.lastRead = measure
            if len(mess)==5:
                mess.pop(0)
            mess.append(measure)
            print(mess)
            mid = int(sum(mess) / len(mess))
            if int(self.boundary) > mid:
                print(self.boundary)
                print(mid)
                print("Bremsen")
                self.Triggered = True
            else:
                self.Triggered = False
