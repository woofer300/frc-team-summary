# frc-team-summary
Command line program that summarizes a FRC team's season

Want to try it out? Follow these steps.
1. Install poetry from https://python-poetry.org/docs/#installation
2. Clone this project
3. In the project folder, execute the following commands:
```
poetry shell
poetry install
```
4. Execute the script
```
python main.py
```
Note that you will have to paste in a TBA API key. If you don't have one yet, you can generate one at following link: https://www.thebluealliance.com/account/login?next=http%3A%2F%2Fwww.thebluealliance.com%2Faccount
Sign in using your email, then click "Add New Key" in the "Read API Keys" section. Copy the key.

If you want to avoid having to paste your key into the program every time you run it, you can paste your key into the auth_key variable on line 4 in main.py.

When you're done, you can exit the poetry shell with the following command:
```
exit
```