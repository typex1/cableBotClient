notes on cableBotClient

URL info:
LineController.java:     @RequestMapping(method=RequestMethod.POST, value = "/linesURL/{id}/{x1}/{y1}/{z1}/{x2}/{y2}/{z2}/{servo}")

$ find . -type f -exec grep -H RequestMethod {} \;
./line/LineController.java:import org.springframework.web.bind.annotation.RequestMethod;
./line/LineController.java:     @RequestMapping(method=RequestMethod.POST, value = "/lines")
./line/LineController.java:     @RequestMapping(method=RequestMethod.POST, value = "/linesURL/{id}/{x1}/{y1}/{z1}/{x2}/{y2}/{z2}/{servo}")
./line/LineController.java:     @RequestMapping(method=RequestMethod.PUT, value = "/lines/{id}")
./line/LineController.java:     @RequestMapping(method=RequestMethod.DELETE, value = "/lines/{id}")
./line/LineController.java:     @RequestMapping(method=RequestMethod.DELETE, value = "/linesClear")
./motor/MotorController.java:import org.springframework.web.bind.annotation.RequestMethod;
./motor/MotorController.java:   @RequestMapping(method=RequestMethod.POST, value = "/moveMM/{x}/{y}/{z}")
