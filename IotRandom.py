from Cryptodome.Cipher import AES
from sense_hat import SenseHat
import numpy as np

class Random: #initialise the random object
    __Seed = None#initialises the seed value
    def __init__(self):#init function
        self.__Seed = self.getReading()#gets a reading from the sensor, sets as the initial seed
        newSeed = str(self.getRandom())#calculates a new seed based on the init seed and a new reading
        self.ReSeed(int(newSeed[0:16]))
        

    def getRandom(self):
        EncryptData = self.getReading()#gets a reading from the sensors
        key = self.__Seed#gets the key for the cipher (this is the seed value)
        cipher = AES.new(key,AES.MODE_CTR)#runs the cipher using the seed, in counter mode
        ByteRandom = cipher.encrypt(EncryptData)#creates random byte stream using cypher and the data read in
        Random = (int.from_bytes(ByteRandom,byteorder="little"))#converts the byte to int using order
        return Random

        

    def ReSeed(self,seed):
        self._Seed=seed# replaces the current seed with the seed passed to function 
        
    def getReading(self):# gets the readings from the astropi sensor
        sense = SenseHat()#initialises the sense hat
        sense.clear#clears anything in the buffer
        Accel = sense.get_accelerometer_raw()#gets the data from the accelorometer
        Data = np.array(list(Accel.values()))#converts to array
        Magnitude = np.linalg.norm(Data)#calculates the magnitude of the accelorometer
        Magnitude = Magnitude - np.floor(Magnitude)#removes numbers before the decimal point
        
        Reading = format(Magnitude,'.16f')#converts to floating point format
        return bytes(Reading[2:],'utf-8') # takes all values after the zero and decimal point
    
# class NumberMaker: #wip section, converts from random seed to number
#     def getNum(self,maxNum):
#         rand = Random()
#         x = rand.getRandom
        
#sense = SenseHat() #in
rand = Random()
for i in range(5000):#loops 
    a = str(rand.getRandom())#gets 
    print(a)#prints output of random
    rand.ReSeed(int(a[0:16]))#reseeds the random number generator with a new seed