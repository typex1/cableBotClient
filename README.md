typical approach to test motor movement:

test movement with 1 second Thread.sleep() between each step (keep in mind that this method counts im mm, not in motor steps

calculation between motor steps and millimeters is done here:

utils.Calibration:
   public final static double stepsPerMM = 1000.0/145.0; //i.e. 6.9 steps per millimeter of thread length

➜  python git:(master) ✗ ./moveXYMM.py raspi 3 0 1000
Url is http://192.168.1.114:8080/cableBot/moveMM/3/0/0/1000
