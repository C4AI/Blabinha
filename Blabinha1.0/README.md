# Blabinha 1.0

Its first version (Blabinha 1.0) was implemented as a game in a social robot. Built using imperative programming in Java, its artificial intelligence was limited to text-to-speech and speech-to-text services available on the Robios robot (https://www.humanrobotics.ai/).

## How to run - connection with Robios

- Set your keys and IDs:

        
        public static final String apiKey = "APIKEY";

        public static final String robotId = "ID";

- If you are using it via **Avatar/Tablet** use this code for connection :
    

        public static Robios robios;
        static {
            try {
                robios = RobiosApi.get(apiKey, RobiosConfig.forCloud(robotId));
            } catch (RobiosException e) {
                throw new RuntimeException(e);
            }
        }

- If you are using it with **Robios Go**. First set the ROBOT_ADDRESS:

        private static final String ROBOT_ADDRESS = "ADDRESS";

    Then use this code for the connection

        public static Robios robios;      
        static {
            try {
                RobiosConfig config = new RobiosConfig();
                config.setRobotAddress(ROBOT_ADDRESS);
                config.setRobotId(robotId);
                robios = RobiosApi.get(apiKey, config);
            } catch (RobiosException e) {
            throw new RuntimeException(e);
            }
        }


## How to run - IDE

To simplify the process of dealing with the libs we recommend the use of a specific IDE for JAVA like IntelliJ IDEA