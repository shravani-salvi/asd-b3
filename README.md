jenkins login : admin - 65f9d1185c3041028d968c5ec8b8b557/shravani48
aws password : Han_Jisung_1409 shravanisalvi28@gmail.com

git:
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

docker:
docker --version
docker info
cd "C:\Users\Shravani Salvi"
mkdir ecommerce-docker
cd ecommerce-docker
mkdir site
notepad site\index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Green Basket - Home</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Green Basket</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="products.html">Products</a>
        </nav>
    </header>
    <main>
        <h2>Welcome to Green Basket</h2>
        <p>Everyday essentials, delivered simply.</p>
        <a class="button" href="products.html">Shop products</a>
    </main>
    <footer>DevOps Docker practical</footer>
</body>
</html>
notepad site\products.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Green Basket - Products</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Our Products</h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="products.html">Products</a>
        </nav>
    </header>
    <main>
        <h2>Featured products</h2>
        <article><h3>Organic Compost</h3><p>Rs. 199</p></article>
        <article><h3>Reusable Bottle</h3><p>Rs. 299</p></article>
        <article><h3>Cotton Tote</h3><p>Rs. 149</p></article>
        <p>Demo catalogue - no real checkout</p>
    </main>
    <footer>DevOps Docker practical</footer>
</body>
</html>
notepad site\style.css

body {
    font-family: Arial, sans-serif;
    margin: 0;
    color: #20352a;
    background: #f5faf5;
}
header, footer {
    background: #1d563b;
    color: white;
    padding: 18px 7%;
}
nav a {
    color: white;
    margin-right: 18px;
    text-decoration: none;
}
main {
    padding: 35px 7%;
    min-height: 55vh;
}
article {
    display: inline-block;
    background: white;
    margin: 8px;
    padding: 20px;
    border-radius: 8px;
}
.button {
    display: inline-block;
    background: #1d563b;
    color: white;
    padding: 10px 16px;
    border-radius: 5px;
    text-decoration: none;
}
notepad Dockerfile

FROM nginx:alpine
COPY site/ /usr/share/nginx/html/
EXPOSE 80
docker build -t green-basket:1.0 .
docker images
docker run -d --name green-basket -p 8080:80 green-basket:1.0
docker ps
ren Dockerfile.txt Dockerfile
docker rm green-basket

ansible:
sudo apt update
sudo apt install -y ansible
ansible --version
mkdir -p ~/ansible-practical
cd ~/ansible-practical
cat > inventory.ini <<'EOF'
[local]
localhost ansible_connection=local
EOF
ansible -i inventory.ini local -m ping
nano setup.yml
---
- name: Configure localhost for DevOps practical
  hosts: local
  become: true
  tasks:
    - name: Ensure curl is installed
      ansible.builtin.apt:
        name: curl
        state: present
        update_cache: true
     - name: Create demonstration directory
       ansible.builtin.file:
         path: /opt/ansible-practical
         state: directory
         mode: "0755"
     - name: Write configuration file
       ansible.builtin.copy:
         dest: /opt/ansible-practical/info.txt
         content: |
           Managed by Ansible.
           Host: localhost
           Purpose: DevOps practical examination.
         owner: root
         group: root
         mode: "0644"
ctrl+O enter ctrl+X
ansible-playbook -i inventory.ini setup.yml --syntax-check
ansible-playbook -i inventory.ini setup.yml --ask-become-pass
cat /opt/ansible-practical/info.txt

airflow:
wsl
sudo apt update
sudo apt install -y python3.14-venv
mkdir -p "/mnt/c/Users/Shravani Salvi/airflow"
cd "/mnt/c/Users/Shravani Salvi/airflow"
python3.14 -m venv .venv
source .venv/bin/activate
export AIRFLOW_VERSION=3.2.0
export PYTHON_VERSION=3.14
python -m pip install --upgrade pip
python -m pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
airflow version
nano ~/airflow/airflow.cfg
in [api] change port=8080 to 8081
airflow standalone
2nd wsl terminal
cd "/mnt/c/Users/Shravani Salvi/airflow"
source .venv/bin/activate
airflow config get-value core dags_folder
mkdir -p ~/airflow/dags
nano ~/airflow/dags/print_datetime_dag.py
code:
import pendulum
from datetime import datetime
from zoneinfo import ZoneInfo
from airflow.sdk import dag, task

@dag(
    dag_id="print_datetime_every_wednesday",
    schedule="30 9 * * 3",
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Kolkata"),
    catchup=False,
    tags=["practical"],
)
def print_datetime_dag():
    @task
    def print_date_time():
        current_time = datetime.now(ZoneInfo("Asia/Kolkata"))
        print("Current Date and Time (IST):", current_time.strftime("%d-%m-%Y %H:%M:%S"))

    print_date_time()

print_datetime_dag()
Open http://localhost:8081
cat /home/shravani/airflow/simple_auth_manager_passwords.json.generated for password
ls -la /home/shravani/airflow/
