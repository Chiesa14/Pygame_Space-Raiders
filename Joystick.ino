//input pins

//analog
int JSx = A0;
int JSy = A2;

//digital
int JSpin = 9;

//read JS position values
int JSxVal;
int JSyVal;
int JSVal;

// delay(ms)
int dt = 50;

void setup() {
    // put your setup code here, to run once:

    pinMode(JSx,INPUT);
    pinMode(JSy,INPUT);
    digitalWrite(JSpin,HIGH);
    Serial.begin(9600);
    
}
void loop() {
    // put your main code here, to run repeatedly:

    JSxVal = analogRead(JSx);
    JSyVal = analogRead(JSy);
    JSVal = digitalRead(JSpin);
    
    delay(dt);


    //JSx coor
    Serial.print(JSxVal);
    Serial.print(" ");
    Serial.print(JSyVal);
    Serial.print(" ");
    Serial.println(JSVal);

    //JSy coor
}
