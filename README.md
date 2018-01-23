notes on cableBotClient

REST methods:
------------

$ find . -type f -exec grep -H RequestMethod {} \;

# Line-POST:
./line/LineController.java:     @RequestMapping(method=RequestMethod.POST, value = "/lines")
./line/LineController.java:     @RequestMapping(method=RequestMethod.POST, value = "/linesURL/{id}/{x1}/{y1}/{z1}/{x2}/{y2}/{z2}/{servo}")

# Line-PUT:
./line/LineController.java:     @RequestMapping(method=RequestMethod.PUT, value = "/lines/{id}")

#Line-DELETE:
./line/LineController.java:     @RequestMapping(method=RequestMethod.DELETE, value = "/lines/{id}")
./line/LineController.java:     @RequestMapping(method=RequestMethod.DELETE, value = "/linesClear")

# Motor-POST:
./motor/MotorController.java:import org.springframework.web.bind.annotation.RequestMethod;
./motor/MotorController.java:   @RequestMapping(method=RequestMethod.POST, value = "/moveMM/{x}/{y}/{z}")
