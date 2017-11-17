Messsage Generator 0.0.1

Synopsis: THis message generator will allow you to generate anymount of message at a rate of 1000 messages per second.

Usage Syntax example: java -jar MsgGen.jar <queue_name> <message_count> [-v]

queue_name -  The name of the service bus queue. Please note that the queue will be created if it doesnt exist.

message_count - The amount of messages you will like to push to the queue.

-v - An optional switch to enable MsgGen to be verbose when sending messages.