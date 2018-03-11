# Kiera
Deep Learning Traffic Sign Recognition System

## Description
A Deep Learning Application for Traffic Sign Recognition

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
