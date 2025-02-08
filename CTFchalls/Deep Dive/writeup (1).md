## Deep Dive

## Description
In the world of digital forensics, sometimes the most crucial evidence is not immediately visible. Investigators must delve deep into the file, searching for clues that elude the eye and uncover the truth hidden beneath layers of complexity. As you dig through the data, the challenge is to reveal what lies beneath the surface and piece together the story that has been obscured.

## Solution
We have been given with an excel file
Let's start by inspecting the Excel Workbook. If we open it with a dedicated program, we get one sheet named "Deeee" saying "Deep Dive - hidden almost out of view, waiting to be discovered.
![Screenshot 2024-09-21 164403](https://github.com/user-attachments/assets/6ad0676e-3121-493d-8941-6050ff5517ad)

We can right-click and select "Unhide" to view hidden sheets:
![Screenshot 2024-09-21 164559](https://github.com/user-attachments/assets/1559aa55-9a75-4406-b6a3-16a05c4dffbf)
![Screenshot 2024-09-21 164606](https://github.com/user-attachments/assets/d5fd1930-017c-4a9d-865e-465822693757)

Sheet2 says:
![Screenshot 2024-09-21 165104](https://github.com/user-attachments/assets/81b16799-7060-4c79-976b-817fe08740ea)

And Sheet3:
![Screenshot 2024-09-21 165443](https://github.com/user-attachments/assets/01568f23-09dd-40ce-8b76-5787a41195b3)

Excel files are just zip archives. We can extract them and look inside.
![Screenshot 2024-09-21 165755](https://github.com/user-attachments/assets/6ff97655-f890-4ea1-a888-a5c81016ea40)
![Screenshot 2024-09-21 165818](https://github.com/user-attachments/assets/e06a67a6-fc7d-403a-9c08-eb8728b86bc0)

Upon looking at the worksheet we can see there is one more sheet in the sharedstrings.xml file which says:
![Screenshot 2024-09-21 170107](https://github.com/user-attachments/assets/797b8594-c156-4e74-adf4-884552df37b7)

Each row is contained within a row element with the row number as the r attribute. Are there duplicates?
![Screenshot 2024-09-21 170501](https://github.com/user-attachments/assets/63071992-c76f-4565-9e22-e2f6eab5aa97)

Output:
![Screenshot 2024-09-21 171137](https://github.com/user-attachments/assets/0a0a3a30-ba50-439e-906d-a544231a0fb2)

Indeed, we have a few rows that appear twice. What's special about them?

Let’s do this for all the sheets we have
![Screenshot 2024-09-21 171511](https://github.com/user-attachments/assets/32beeecc-d58c-4fbe-9e3c-c8080f18b17e)
![Screenshot 2024-09-21 221104](https://github.com/user-attachments/assets/5d06fea1-5c96-4701-8703-f53b7a70fa28)

Now we got the hidden rows lets check what we have in that row

Row 408 says:
![Screenshot 2024-09-21 221517](https://github.com/user-attachments/assets/5e97d10e-279d-4ce0-88ee-2294bd810fc5)

Which is HARDWORK is the key to success

So, after checking basic vulnerabilities in excel I got to know about FORMULA INJECTION

We can just replace the data with hardwork in each of the hidden row
![Screenshot 2024-09-21 221544](https://github.com/user-attachments/assets/f54147dc-4794-4c68-ad6e-519a69700f8e)
![Screenshot 2024-09-21 221549](https://github.com/user-attachments/assets/4c413109-5119-443a-9f5a-66768dd22422)

After doing for all we the get the flag boom!!!

# Flag - HTB{n3v3r_g1v3_up_4lw4y5_4_h1dd3n_k3y}

# Author – Dhruv Gupta


