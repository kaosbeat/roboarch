import oscP5.*;

OscP5 control;
float x= 0;
float y = 0;
float z,distance,xpos,ypos;
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
  noStroke();
}


void draw() {
    //float xpos = map(x, -0.4727309048175812, 0.4922410547733307, 0, width );
    //float ypos = map(y, -0.24367988109588623, 0.22952084243297577, 0 ,height);
    //println(x,y);
    float xpos = map(x, -1, 1, 0, width );
    float ypos = map(y, -1, 1, 0 ,height);
    
    float size= probevalue/20;
    if (col.equals("yellow")) {
      //println(xpos,ypos,probevalue);
      fill(0,255,255,probevalue/4);
    }
    else if (col.equals("blue")) {
      fill(255,0,255,probevalue/4);
    }
    else if (col.equals("red")) {
      fill(25,23,255,probevalue/4);
    }
    else if (col.equals("green")) {
      fill(215,223,5,probevalue/4);
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