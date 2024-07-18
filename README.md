# Los_Pwnnos_Hermanos

## Introduction

Welcome to the "Los_Pwnnos_Hermanos" CTF. This challenge takes place in the famous Los Pollos Hermanos restaurant and includes several stages of exploiting security vulnerabilities, including access control flaws, privileged account access, and buffer overflows.

## Write up
The write up available here : https://leptitpentester.com/ctf/pollos/pollos2.html
You can choose for English or French version

## Prerequisites

Before starting, make sure you have the following installed on your Debian virtual machine:

- Docker
- Git

## Installing Docker

If Docker is not already installed on your machine, follow the steps below to install it.

1. **Update the system:**

    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```

2. **Install necessary dependencies:**

    ```bash
    sudo apt-get install docker git docker-compose
    ```

3. **git clone the CTF**
   ```bash
    sudo giti clone https://github.com/HeaZzY/Los_Pwnnos_Hermanos.git
    ```
   
4. **Switch directory**
   ```bash
   cd Los_Pwnnos_Hermanos
   ```
   
5. **Build the docker**
   ```bash
   sudo docker-compose build
   ```
   
6. **Start the docker**
   ```bash
   sudo docker-compose up
   ```

Good CTF !

   
