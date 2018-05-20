import oscP5.*;

OscP5 control;
float x,y,z,distance,xpos,ypos;
String col;
float probevalue;

void settings() {
  size(1280, 720, P3D);
  PJOGL.profile=1;
}


void setup() {
  frameRate(30);
    control = new OscP5(this, 1238);  ///morses output port
      background(0);
  
}


void draw() {
    float xpos = width + x*2000;
    float ypos = height + y*2000;
    float size= probevalue/50;
    if (col.equals("yellow")) {
      //println(xpos,ypos,col);
      fill(0,255,255,123);
    }
    else if (col.equals("blue")) {
      fill(255,0,255,123);
    }
    else if (col.equals("red")) {
      fill(25,23,255,123);
    }
    else if (col.equals("green")) {
      fill(215,223,5,123);
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