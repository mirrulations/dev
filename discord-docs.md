Discord Documentation
==========================

# Discord Roles Documentation

## Overall Introduction
- Discord servers are composed of Categories which contain text channels and voice channels. Text channels and voice channels can also exist outside of a category. 
- A category can have set permissions that can enable or restrict various things.
- When someone first joins the discord, they won't be able to see any of the team Categories until they select a team in **#team-selection**

## Creating Roles
To create a role in Discord:
1. Navigate Server Settings in the drop-down menu on the top left (click on the server name).
2. Click on **Roles** in the left sidebar.
3. Click **Create Role**, name it, and customize the permissions.

## Assigning Roles
- Go to **Server Settings > Members** and assign a role to a user.
- Alternative, go to **Server Settings > Roles > Select View Members with a specific role > Add Members**


##  Overall Permission and Hierarchy Info
Roles define user permissions within the server. Higher roles in the hierarchy override lower ones.
- A higher up role in the list will take priority over all roles below. 
- For example, Role A is above Role B. Role B doesn't allow messages to be sent. Role A allows messages to be sent. Someone with both of these roles will be allowed to send messages due to the hierarchy system of the roles.


## Notes: 
- It's always best to practice the principle of least privilege with discord roles. 
- Giving someone the 'Administrator' permission is <mark>dangerous</mark>, it allows them to do anything except for deleting the server. Make sure if you give it to someone, you want them to be able to do anything in the server.
- All changes within the server can be seen in the **Audit Log** in the Server Settings. 


# Mirrulations Server
- There exists a role for each of the three teams: 'Data Transformation and Enabling Technologies', 'Data Product', 'API and User Experience'
- Each team has their own respective category, though all teams can see the categories of each teams.
- All roles that are grey colored in the role list are there for convienence. So when people from multiple teams can be group into something like 'Sprint1 Performance' so that @'ing, or pinging, groups is easier.
- For future use, the **Ops** role has already been set with permissions needed to manage the server. 

# Carl-bot
- Carl-bot can be used for many things, however he has only been used for the inital reaction roles setup when people first joined the server (instructions below).
- Whenever using bot commands, it's good practive to do commands in isolated channels meant for them such as the one named **#bot-commands**

### Creating a reaction role message
- You would only do this if anything with the teams is changed such as team names or the amount of teams overall.
- Go to **#bot-commands**, and use the slash command **/reactionrole setup**, Carl-bot will then guide you through the process of setting up the message 
- note, you can edit a currently existing reactionrole message by using the slash command **/reactionrole edit**, though depending on the change it's most likely easier to just delete the original reaction message and make a new one.

