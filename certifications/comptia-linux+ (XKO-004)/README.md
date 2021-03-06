# COMPTIA LINUX+ (XKO-004) CERTIFICATION

## Introduction
Set up your lab environment:
* Install [VirtualBox](https://www.virtualbox.org/manual/ch02.html) on local machine.
* Install [CentOS 8](https://linuxhint.com/install_centos8_virtualbox/) or [7]() on VirtualBox.
* Install [Ubuntu](https://brb.nci.nih.gov/seqtools/installUbuntu.html) on VirtualBox.

### 1.0 Hardware and System Configuration 21%

1.1 System Hardware: Linux Boot Process
   
   * Firmware: Excecute code in the BIOS/UEFI; firmware execute bootloader (grub2) code on drive.
   * Bootloader: Bootloader reads its configuration file; executes the kernel.
   * Kernel: Kernel loads the RAMDisk into RAM.
   * Initialization: systemd is started.
   
1.2 Disk Systems:

   * See the article by [Nevana Pavlicic](https://phoenixnap.com/kb/linux-create-partition) for more information.

### 2.0 System Operation and Maintenance 26%

2.1 Manage Users and Software:

2.2 Files: Create, Modify and Redirect

   * Install **tree** gives us a graphical visualization of files structure in a given folder.
     ```
     sudo apt  install tree
     ```
   * Use **locate** command to find files.
     ```
     sudo apt install mlocate
     locate file_name
     ```
   * This command below will show files and folders that have `usr` and `passwd` only:
     ```
     locate --regex '^/usr.*passwd$'
     ```
   * You can use archieve/compress files in linux: see this [link](https://linuxize.com/post/how-to-zip-files-and-directories-in-linux/).

2.3 Server Infrastructure and Services

   * To see the cron job folders, use this command: 
     ```
     ls -d /etc/cron.*
     ```
   * [Systemd](https://wiki.archlinux.org/title/Systemd-networkd)
   * To see the calendar, use `cal`.
   * To see the calendar for any year type `cal the_year_you_want`.
   * To see all services:
     ```
     systemctl list-unit-files -at service
     ```
   * To see the systems that are running:
     ```
     systemctl list-units -t service --state running
     ```
   * To check the status of any service:
     ```
     systemctl status service_name
     ```
 *Click on **q** to quit.*

### 3.0 Security 19%

3.1 File Security

3.2 System Security

3.3 Generate **ssh key pair**, use this [link](https://www.ssh.com/academy/ssh/keygen).

### 4.0 Linux Troubleshooting and Diagnostic 20%

4.1 System Logging

4.2 System Monitoring

4.3


### 5.0 Automation and Scripting 14%

5.1 Version Control

5.2 Automation and Scripting

# Sources:

1. https://www.linkedin.com/learning/
2. https://www.virtualbox.org/manual/ch02.htm
3. https://laptop.ninja/how-to-setup-centos-in-virtualbox/
4. https://brb.nci.nih.gov/seqtools/installUbuntu.html
