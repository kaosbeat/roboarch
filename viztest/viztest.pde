import oscP5.*;

OscP5 control;

void settings() {
  size(1280, 720, P3D);
  PJOGL.profile=1;
}


void setup() {
  frameRate(30);
    control = new OscP5(this, 1238);  ///morses output port
}


void draw() {
    background(255);
    
}


void oscEvent(OscMessage theOscMessage) {
  if (theOscMessage.checkAddrPattern("/probe/data") == true) {
    println(theOscMessage.get(0).intValue());
    
  }
}