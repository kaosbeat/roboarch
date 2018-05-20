import oscP5.*;

OscP5 control;
float x= 0;
float y = 0;
float z,distance,xpos,ypos;
String col = "yellow";
float probevalue = 512;

void settings() {
  size(1280, 720, P3D);
  PJOGL.profile=1;
}


void setup() {
  frameRate(30);
    control = new OscP5(this, 1238);  ///morses output port
      background(0);
  noStroke();
}


void draw() {
    //float xpos = map(x, -0.4727309048175812, 0.4922410547733307, 0, width );
    //float ypos = map(y, -0.24367988109588623, 0.22952084243297577, 0 ,height);
    //println(x,y);

    float xpos = map(x, -1, 1, 0, width );
    float ypos = map(y, -1, 1, 0 ,height);
    //float size = 5;
    float fill = 120;
    //float fill = probevalue/4;
    float size = probevalue/20;
    fill(255);
    rect(20,620,50,1024/20);
    rect(20,700,50,650);
    fill(0, 102, 153);
    textSize(20);
    text(int(probevalue), 25, 720);
    fill(255,0,0);
    rect(20,620,50,size);
    if (col.equals("yellow")) {
      //println(xpos,ypos,probevalue);
      fill(0,255,255,fill);
    }
    else if (col.equals("blue")) {
      fill(255,0,255,fill);
    }
    else if (col.equals("red")) {
      fill(25,23,255,fill);
    }
    else if (col.equals("green")) {
      fill(215,223,5,fill);
    }
    else if (probevalue >= 512){
      fill(255,0,0);
      size = 5;
    }
    
    ellipse(xpos,ypos,size,size);
    
}


void oscEvent(OscMessage theOscMessage) {
  //println ("msg received");
  if (theOscMessage.checkAddrPattern("/probe/x") == true) {
    //println(theOscMessage);
    x = theOscMessage.get(0).floatValue();
  }
  if (theOscMessage.checkAddrPattern("/probe/y") == true) {
    //println(theOscMessage);
    y = theOscMessage.get(0).floatValue();
  }
  if (theOscMessage.checkAddrPattern("/probe/z") == true) {
    //println(theOscMessage);
    z = theOscMessage.get(0).floatValue();
  }
  if (theOscMessage.checkAddrPattern("/probe/distance") == true) {
    //println(theOscMessage);
    distance = theOscMessage.get(0).floatValue();
  }
  if (theOscMessage.checkAddrPattern("/probe/value") == true) {
    //println(theOscMessage);
    probevalue = theOscMessage.get(0).floatValue();
    println(probevalue);
  }
  if (theOscMessage.checkAddrPattern("/probe/color") == true) {
    //println(theOscMessage);
    col = theOscMessage.get(0).stringValue();
  }
}