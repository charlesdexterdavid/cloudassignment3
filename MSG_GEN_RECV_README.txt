# Messsage Generator and Receive 0.0.1

### Synopsis: The application works in two parts: 

  1. A message genrator: the message generator will allow you to generate any amount of messages at a rate specified to be pushed to a specified queue on Azure Service Bus. limitations are due to the machine specifications.
  
  2. A message receiver: The receive will allow the retrieval and storages of messages from an Azure Service Bus queue at a rate specifed. Limitations are due to the machine specifications 

USING THE JAR FILE:

Usage Syntax format for generating messages (using the MsgGenRecv.jar file): java -jar MsgGenRecv.jar send_messages <queue_name> <message_count> <message_send_rate> [<verbose_switch>]

queue_name -  The name of the service bus queue. Please note that the queue will be created if it doesnt exist.

message_count - A number which represents the amount of messages you will like to push to the queue.

message_send_rate - A number which represents the rate at which messages will be sent per second.

-v - An OPTONAL switch to enable the generator to be verbose when sending messages.

Usage Syntax format for receiving messages (using the MsgGenRecv.jar file): java -jar MsgGenRecv.jar receive_messages <queue_name> <message_recv_rate> [<verbose_switch>]

queue_name -  The name of the service bus queue.

message_recv_rate - A number which represents the amount of messages that should be pulled concurrently from the queue.

-v - An OPTONAL switch to enable the generator to be verbose when sending messages.


USING THE msg_gen_recv.sh script

IMPORTANT: Please note that the MsgGenRecv.jar file should be in the same directory as the as the msg_gen_recv.sh file;

Usage Syntax format for generating messages (using the msg_gen_recv.sh file): /bin/bash msg_gen_recv.sh send_messages <queue_name> <message_count> <message_send_rate> [<verbose_switch>]

Usage Syntax format for generating messages (using the msg_gen_recv.sh file): /bin/bash msg_gen_recv.sh receive_messages <queue_name> <message_recv_rate> [<verbose_switch>]






