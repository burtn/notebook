# Protocols

> Protocols are a set of rules which detail how data is transferred from one device to another.

+ Protocols state the **syntax**, **semantics** and **synchronization** of a communication.

*They do this by stating:*

+ How the data is represented. *(ASCII text, binary, etc)*
+ How the data is checked. *(Parity bits, etc)*
+ How to recover from errors. *(e.g. Collision detection)*
+ How the data will arrive. *(In packets, all at once, etc)*

**NB:** The way two parties communicating using a protocol behave is **completely independent of the implementation** which may be in **hardware or software** or any combination of the two.

Each party using a protocol must agree to it, this can be done by producing a technical standard.

*Aside* - programming languages are like protocols for describing the way to carry out computations.

Often many protocols are used together, for example the 'internet' consists of many protocols **layered** on each other. *e.g. Ethernet (Network layer) => IP (Internet layer) => TCP (Transport layer) => HTTP (Application layer).* When a group of protocols are used together like this they are called an **protocol suite**.

###### Other protocol examples

+ SMTP (Simple mail transfer protocol) - Transferring emails between servers e.g. Microsofts Hotmail servers to Googles GMail servers.
+ POP (Post office protocol) - For getting emails from servers, a legacy since most users now use a web based mail client.
+ HTTP (Hypertext transfer protocol, see web pages notes)
+ SSL (Secure socket layer) - A means of securing an connection over the internet.

[(bigger list)](http://en.wikipedia.org/wiki/List_of_network_protocols)

### Data representation

At a basic level all (digital) telecommunications data is a stream of 1s and 0s however some protocols are designed to work on/with text rather than binary data.

For example a protocol which is designed to send and receive images from security cameras will expect binary data (the image) whilst HTTP is text based. Text based protocols are more common in scenarios where humans write as well as read the data (partially HTML in this case). Text can be represented in a number of ways including the ASCII and Unicode systems. Different text systems are used for different purposes and dictate the way that the text is encoded. ASCII for example encodes all the letters into a digit which fits in one byte which means it cannot include more than 255 characters. This lead to other encoding means like Unicode which can fit other characters such as the Greek alphabet alongside the Latin one by using more bits.

### Error checking

In any communications network there exists a large chance that an error will occur during transmission. To ensure that data is transferred reliably through unreliable means error checking and correction are used.

Parity bits are one such error checking method.
A parity bit (sometimes check bit) is a bit added to the end of a binary string to indicate whether the number of 1s in the string are even or odd. There are two types of parity bit, odd or even. Using even parity the parity bit is set to 1 when the number of 1s is odd thereby making the number of 1s even. Using odd parity a 1 is added if the number of 1s is even, this makes the number odd.

### Error recovery/collision detection

Collisions occur when two devices try to signal on a communications medium at the same time. To deal with such collisions carrier sense multiple access with collision detection (CSMA/CD) is used. CSMA/CD is a media access control mechanism. In Ethernet networks CSMA/CD takes place like this:

1. Device attempts to transmit signal when medium (i.e. the cable) is clear.
2. If a collision is detected a signal is sent and picked up by the sender.
3. The sender sends a jam signal. (this prevents transmission of all signals in the network area)
4. The sender waits a random period of time before starting again from 1.
