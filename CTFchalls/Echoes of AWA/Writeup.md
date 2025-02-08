## Echoes of AWA

## Description – 
Four explorers discovered an ancient cryptographic system called 'awa.' In their quest, they uncovered unique encryption patterns unlike anything seen before. Every step forward reveals new layers of puzzles to solve. 
Investigators must now crack the 'awa' logic to unveil the encrypted flag.
Victory belongs to those who understand the intricacies of the 'awa' logic and can crack the final encrypted flag.
Embrace the challenge, unlock the secrets of the past, and prove your cryptographic skills.

## Solution – 
By looking to the description, we can see awa is being used several times
Upon looking at the web I got to know that AWA is a bubble-based esoteric programming language
So, let’s move on to the question, we have been given 2 files one contains the encrypted text and the other gives the encryption script using which the flag was encrypted

![Screenshot 2024-09-21 151952](https://github.com/user-attachments/assets/7565f9d8-e5c9-4395-8f7d-b1bba437689b)
![Screenshot 2024-09-21 152022](https://github.com/user-attachments/assets/8728db5f-54ab-4e46-92d5-3b6b6b7fe89e)


After looking the code carefully, I understand that it defines an encryption process for a flag using a custom 'awa' encoding scheme and appends an additional message (“msg2”), which is hex encoded. 
•	The “awa_map” dictionary maps binary digits ('0', '1', '2', '3') to custom 'awa' patterns used for encoding
•	“Encrypt_with_msg2” takes a flag and a shift value to create an encrypted flag by shifting ASCII values and converting each character to its binary form, which is then reversed and encoded using “awa_map”.
•	After encoding the flag, it appends “msg2”, which is a fixed message that is hex encoded.
•	The “extract_msg_msg2” function splits the encrypted message from the appended hex-encoded “msg” and decodes back to its original form.
•	The final encrypted flag and the encoded message are printed.
Now, we can see three fields have been set to question mark 
1)	Flag
2)	Msg2
3)	Shift Value
So, just write the decryption code and replace the question mark with what have been given

![Screenshot 2024-09-21 154915](https://github.com/user-attachments/assets/a9b29e74-e4b9-4398-b172-2e5de6ac66c7)
![Screenshot 2024-09-21 155103](https://github.com/user-attachments/assets/9096340a-0958-49eb-a3fe-bde234d0340b)

After running this code we got an error,
![Screenshot 2024-09-21 155122](https://github.com/user-attachments/assets/88c96f31-ed39-4012-9633-7569c765a881)

Now we must get the shift value, so let’s just check the description again
If you look at the first letter of each sentence, it will give you something like,
F
I
V
E
Which gives us the shift value hint as 5
Let’s just put and see if we can get the flag out of it

![Screenshot 2024-09-21 154930](https://github.com/user-attachments/assets/55c7afcb-119b-40e3-92b4-4b6a797fef21)
![Screenshot 2024-09-21 155427](https://github.com/user-attachments/assets/076828a4-44d9-4693-9217-a612e538f69d)

Congrats!!! We get the flag 

# Flag – HTB{N07_4ll_Cryp70_15_UnBr34k4bl3}
# Author – Dhruv Gupta
