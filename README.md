# Kiera
Deep Learning Traffic Sign Recognition System

## Description
A Deep Learning Application for Traffic Sign Recognition

### Prerequisites
 - Python 3.6+
 - Ubuntu 16.04LTS
 - Virtual Environment for Python with pip
   - <a href="https://conda.io/docs/user-guide/install/download.html">Anaconda</a>
   - `virtualenv`, `pyvenv`
 - Network Access for getting dependencies
   
   
### Setup Instructions 
 - Clone Repo
   - `git clone https://github.com/rachit-ranjan16/Kiera.git`
 - Activate Virtual Environment
 - Install RabbitMQ
   - `sudo apt-get -y -q install rabbitmq-server`
 - Get project dependencies in place 
   - `cd Kiera`
   - `python setup.py develop`
 - Start up Django(Dev Mode)
   - `python manage.py runserver 0.0.0.0:8080`
 - Start up Celery(Dev Mode)
   - `celery -A Kiera worker -l info`
 
 
    
## Design Documentation
### Deep Neural Network
- Layer 1 Input Conv
    - kernel 5x5
    - stride 1x1
    - reLU activation 
- Layer 2 Conv
    - kernel 5x5 
    - stride 1x1
    - reLU activation
- Layer 3 MaxPooling 
    - pooling size 2x2 
    - dropout 0.25 
- Layer 4 Conv 
    - kernel 5x5
    - stride 1x1
    - reLU activation 
- Layer 5 Conv 
    - kernel 5x5
    - stride 1x1
    - reLU activation 
- Layer 6 MaxPooling 
    - pooling size 2x2 
    - dropout 0.25 
- Layer 7 Flatten 
- Layer 8 Fully Connected 
    - dropout 0.25
    - relU activation 
- Layer 9 Output 
    - SoftMax Classification 


### Microservice Architecture 
#### Component Diagram
![Could not display. Check design/ComponentDiag.png](/design/ComponentDiag.png?raw=true "Component Diagram")
#### Sequence Diagram
![Could not display. Check design/SequenceDiag.png](/design/SequenceDiag.png?raw=true "Sequence Diagram")
