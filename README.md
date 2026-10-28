jenkins login : admin - 65f9d1185c3041028d968c5ec8b8b557/shravani48
aws password : Han_Jisung_1409 shravanisalvi28@gmail.com
mkdir git-lab-practical1
cd git-lab-practical1
git init
git config user.name "Student Name"
git config user.email "student@example.com"
echo "Application Version: 1.0.0" > app.txt
git add app.txt
git commit -m "Initial base commit on main branch"
git checkout -b feature-update
echo "Feature Implementation: UI Dashboard Active" >> app.txt
git add app.txt
git commit -m "Add feature update to app.txt"
git checkout main
echo "Feature Implementation: Backend REST Service Active" >> app.txt
git add app.txt
git commit -m "Add backend service update on main branch"
git merge feature-update
Resolve conflict in notepad
Application Version: 1.0.0
Feature Implementation: Backend REST Service Active and UI Dashboard Active
git add app.txt
git commit -m "Resolved merge conflict between main and feature-update"
git log --oneline --graph
