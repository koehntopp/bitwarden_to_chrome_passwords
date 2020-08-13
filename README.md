# Convert Bitwarden password export for upload to Google Passwords

I have been using [Bitwarden](https://www.bitwarden.com) as my password manager for quite a while now, and I can wholeheartedly recommend it. I switched from [Lastpass](https://www.lastpass.com) because I found the Bitwarden UI more easy to understand (my whole family uses Bitwarden as well) and because it gace me cross-platform synchronisation of my TOTP one-time passwords.

However, I found that my family members could not adapt as easily - there were many reasons why Bitwarden didn't work for them as well as it did for me:

* Mobile version requires master password after reboot. That is usually a very complex password, so that's bad

* When they changed passwords they would not always store the new one in Bitwarden

* Password creation UI wasn't always triggered, so they chose simple passwords

At the same time the Google Chrome team has really stepped up their game regarding the built-in password manager, and it seems they are taking a shot at replacing external password managers.

In order to try all the new functionality I needed to get my passwords from Bitwarden into Chrome. This was more difficult as I had expected, for two reasons:

* Chrome hides the "import" functionality

* The Bitwarden export is not in a format that Chrome can import directly.

Alas I had to write this converter to get my passwords over.

# Usage

1. Go to [https://vault.bitwarden.com/#/tools/export](https://vault.bitwarden.com/#/tools/export) and export your passwords in CSV format

![alt text](https://github.com/koehntopp/bitwarden_to_chrome_passwords/blob/master/Readme/bitwarden-export.png?raw=true)

2. Run **"python3 bitwarden_to_google_passwords.py <bitwarden csv>"**. This will generate a file called **"chrome_passwords.csv"** in the same directory. 

3. Type [chrome://flags/#password-import-export](chrome://flags/#password-import-export) into the address bar and enable the password import option

![alt text](https://github.com/koehntopp/bitwarden_to_chrome_passwords/blob/master/Readme/import-enabled.png?raw=true)

4. Go to the Chrome Password manager by typing [chrome://settings/passwords](chrome://settings/passwords) into the address bar and import the **"chrome_passwords.csv"** file

![alt text](https://github.com/koehntopp/bitwarden_to_chrome_passwords/blob/master/Readme/import-menu.png?raw=true)

5. There is no step 5.

# Version History

* 1.0 as of 2020-08-13 Initial version

  * Only exports itemps of type "login" with associated name, URL, user name and password
