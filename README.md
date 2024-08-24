1. Linux Ubuntu Commands 

	1. Update and Upgrade the System:
		
 			sudo apt update
			sudo apt upgrade

	2. Install Essential Software:

			sudo apt install build-essential
			sudo apt install curl wget git htop vim nano

	4. Add Repositories and Install Drivers:
		
  			sudo add-apt-repository ppa:repository-name
			sudo apt update

		Install proprietary drivers:

   			sudo ubuntu-drivers autoinstall

	4. Configure System Settings:

			sudo timedatectl set-timezone [your-timezone]
		Check and configure locale:

   			sudo dpkg-reconfigure locales

	6. Enhance System Security:

			sudo ufw enable
			sudo ufw status

		Install ClamAV (optional):

   			sudo apt install clamav clamtk
			sudo systemctl start clamav-freshclam

	6. Install and Configure Git:
		
  			git config --global user.name "Your Name"
			git config --global user.email "your.email@example.com"
		Generate SSH keys:

   			ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
			eval "$(ssh-agent -s)"
			ssh-add ~/.ssh/id_rsa
			cat ~/.ssh/id_rsa.pub

	7. Install and Manage Software

			sudo apt install snapd
		Install Flatpak:

   			sudo apt install flatpak
			flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

	9. Install Docker (if needed)

	
  			sudo apt install docker.io
			sudo systemctl start docker
			sudo systemctl enable docker
			sudo usermod -aG docker $USER

	10. Set Up System Monitoring
	Install system monitoring tools:
		
  			sudo apt install htop glances
		Run htop:

   			htop

	11. Automate Tasks with Cron
			
   			crontab -e
		List cron jobs:

			crontab -l

	12. Configure GRUB for Dual-Boot
		
  			sudo update-grub

	13. Create a System Snapshot (with Timeshift)
		Install Timeshift:
		
  			sudo apt install timeshift

		Run Timeshift:

			sudo timeshift-launcher

	13. Backup and Restore Configuration
		
 			git init
			git add .bashrc .vimrc
			git commit -m "Initial backup of dotfiles"
			git remote add origin [repository-url]
			git push -u origin master

	14. Reboot the System
		
  			sudo reboot
	
	15. Apps From Store 
		(a) VLC 
		(b) VS Code
		

3. Python          =	

   			sudo apt update

   			sudo apt install python3
			
			sudo apt install python3-pip
			
			sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
			
			sudo pip3 install virtualenv

2. Webdriver Link  = https://googlechromelabs.github.io/chrome-for-testing/
   
3. selenium
   		pip install selenium
   		pip install webdriver-manager
   		
