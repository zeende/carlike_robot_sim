void setup(){
  Serial.begin(9600);
  pinMode(13, OUTPUT);//设置13号端口作为输出端口
  digitalWrite(13,HIGH);//让灯开始时亮
}
char var;
void loop(){
  while(Serial.available()>0)//当有信号的时候
  {
    var=Serial.read();
    if(var=='0')//传过来的是0
      digitalWrite(13,LOW);
if(var=='1')//传过来的是1
digitalWrite(13,HIGH);
  }
}
