# 0 day at Los Pollos

## Introduction

Welcome to the "0 day at Los Pollos" CTF. This challenge takes place in the famous Los Pollos Hermanos restaurant and includes several stages of exploiting security vulnerabilities, including access control flaws, privileged account access, and buffer overflows.

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
    sudo giti clone https://github.com/HeaZzY/0_day_at_Los_Pollos.git
    ```
   
4. **Switch directory**
   ```bash
   cd 0_day_at_Los_Pollos
   ```
   
5. **Build the docker**
   ```bash
   sudo docker-compose build
   ```
   
6. **Start the docker**
   ```bash
   sudo docker-compose up
   ```

   
