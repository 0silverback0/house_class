#!/usr/bin/env python3

class House:
    """ defines a house and common actions performed """
    def __init__(self, address, type, bedrooms, bathrooms):
        self.address = address
        self.type = type
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.locked = True
        self.occupied = False
        self.code = ''
        self.alarm = True

    def __repr__(self):
        """ Returns a more clear representation of the House object """
        return f'House, address:{self.address}, type:{self.type}, bedrooms:{self.bedrooms}, bathrooms{self.bathrooms}'

    def move_in(self):
        """ allows user to move into a home if not occupied """
        self.code = input('Enter your alarm code')
        if not self.occupied:
            self.occupied = True
            return 'congrats on your new home'
        else:
            return 'you live here'

    def move_out(self):
        """ allows a user to move out of a home if occupied """
        if self.occupied:
            self.occupied = False
            return 'nice knowing ya'
        else:
            return 'you dont live here'

    def unlock(self):
        """ unlocks the home if locked or alerts user if door is open """
        #alarm_off = self.toggle_alarm(self.alarm)
        if self.toggle_alarm(self.alarm) == False:
            self.locked = False
            return 'Unlocked Alarm Off'
        else:
            return "Door is Open. Alarm is Off"

    def lock(self):
        """ locks the home or alerts user the door is locked """
        alarm_on = self.toggle_alarm(self.alarm)
        if alarm_on == True:
            self.locked = True
            return 'Locked Alarm on'
        else:
            return 'Door is Locked. Alarm On'

    def toggle_alarm(self, alarm_state):
        """ turn alarm on and off if passcode is correct """
        attempts = 0
        entered_code = input('Enter passcode')
        # if alarm is on and code matches turn alarm off
        if alarm_state == True and entered_code == self.code:
            self.alarm = False
            return self.alarm
        # if alarm is off and code matches turn alarm on
        elif alarm_state == False and entered_code == self.code:
            self.alarm  = True
            return self.alarm
        # if code doesnt match retry
        elif entered_code != self.code:
            while entered_code != self.code:
                attempts += 1
                retry = input(f'Try again you have {3 - attempts} attempts left: ')
        # if code then matches and alarm is on turn it off
                if retry == self.code and self.alarm == True:
                    self.alarm = False
                    return self.alarm
        # if code then matches and alarm is off turn it on
                if retry == self.code and self.alarm == False:
                    self.alarm = True
                    return self.alarm
        # if the code doesnt match and you had 3 attempts alarm state remains the same
                if retry != self.code and attempts >= 3:
                    self.alarm = alarm_state
                    return self.alarm 

            




home = House('123 maple street', 'family', 3, 2.5)

