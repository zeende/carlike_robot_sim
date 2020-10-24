int a=-10;
int b=0;
int c=0;
#define re_data  2
void setup(){
   Serial.begin(9600);
    pinMode(13, OUTPUT);//设置13号端口作为输出端口
  digitalWrite(13,HIGH);//让灯开始时亮
 }
String comdata="";
int numdata[re_data]={0};
int serial_mark = 0;

 void loop(){
  int j=0;
   Serial.print(a);
   Serial.print(",");
   Serial.print(b);
   Serial.print(",");
   Serial.println(c);
   delay(200);

   while(Serial.available()>0)//当有信号的时候
  {
    comdata +=char(Serial.read());
    delay(1);
    serial_mark = 1;
  }
  if (serial_mark==1){
    for(int i=0;i<comdata.length();i++){
      if(comdata[i]==',') j++;
      else numdata[j]=numdata[j]*10+(comdata[i]-'0');
    }
  }


    if(numdata[0]<1499)//传过来的是0
      digitalWrite(13,LOW);
    if(numdata[0]>1499)//传过来的是1
      digitalWrite(13,HIGH);
      
    comdata = "";
    serial_mark = 0;
    for(int n = 0;n<re_data;n++) numdata[n]=0;
 }
