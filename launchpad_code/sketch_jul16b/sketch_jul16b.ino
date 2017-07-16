#define led RED_LED
boolean flag1,flag2;
int val;
void setup()
{
    Serial.begin(9600);
    pinMode(led, OUTPUT);
}
void loop()
{
    if(Serial.available())
    {
        val = Serial.read();
        Serial.println(val);
        if(val == 48) { // a is pressed
            flag1 = true;
        }
        else if(val == 49) { // b is pressed
            flag1 = false;
        }
    }

    if(flag1) {
        digitalWrite(led, HIGH);
    }
    else{
        digitalWrite(led, LOW);}
}
