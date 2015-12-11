# Full Stack Foundations Projects
Code for projects developed for Udacity's Full Stack Foundations course.

## Project Setup and Testing
To set up and test the projects, you will need to do the following:

1. Clone the main parent repository: `git clone https://github.com/hessler/udacity-courses.git`
2. Navigate to the cloned repository directory. For example, if you cloned to your Desktop on a Mac: `cd ~/Desktop/udacity-courses/`.
3. Navigate to the proper directory:
    - Restaurant Project: `cd full_stack_foundations/vagrant/restaurant`
    - Puppy Shelter Project: `cd full_stack_foundations/vagrant/puppy_shelter`
4. Launch the Vagrant Virtual Machine: `vagrant up`
5. Once the VM is powered on, log in to it: `vagrant ssh`
6. Navigate to the `vagrant` directory: `cd /vagrant`
7. Run the desired command(s) from the Makefile for the desired project:
    - Restaurant Project:
        - Start server and initialize project: `make serve_restaurant`
        - Reset project and delete database: `make reset_restaurant`
    - Puppy Shelter Project:
        - Start server and initialize project: `make serve_puppy_sheler`
        - Reset project and delete database: `make reset_puppy_shelter`
    - General:
        - Run pylint: `make lint`
8. Once you are done testing, stop the server by typing `Ctrl + C`
9. Log out of the VM: `exit`
10. Turn off the VM: `vagrant halt`
