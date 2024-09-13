from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen
import time
from kivymd.app import MDApp



from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import TouchBehavior
from kivymd.app import MDApp
from kivymd.uix.behaviors import CircularRippleBehavior, CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from jnius import autoclass, cast

# Load Android classes
Context = autoclass('android.content.Context')
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Activity = autoclass('android.app.Activity')
PackageManager = autoclass('android.content.pm.PackageManager')
CameraManager = autoclass('android.hardware.camera2.CameraManager')
KV = '''
<CircularElevationButton>
    
    
    size_hint: None, None
    size: "230dp", "230dp"
    radius: self.size[0] / 2
    shadow_radius: self.radius[0]
    md_bg_color: "blue"

    MDIcon:
        icon: "flash"
        halign: "center"
        valign: "center"
        pos_hint: {"center_x": .5, "center_y": .5}
        size: root.size
        pos: root.pos
        font_size: root.size[0] * .6
        theme_text_color: "Custom"
        text_color: "white"
<MagicButton@MagicBehavior+CircularElevationButton>

MDScreen:
    md_bg_color:"black"

    MagicButton:
        id:c1
        pos_hint: {"center_x": .5, "center_y": .6}
        elevation: 40
        shadow_softness: 23
        
        on_release: app.toggle_torch()
        
        on_release: self.twist()
    
        
        
        
        
    
        
    
'''
class CircularElevationButton(
    CommonElevationBehavior,
    CircularRippleBehavior,
    ButtonBehavior,
    MDFloatLayout,
    
):
    pass
   

class TorchApp(MDApp):
   
    def build(self):
        self.torch_on = False
        return Builder.load_string(KV)

    def toggle_torch(self):
        # Toggle the torch state
        if self.torch_on:
            self.turn_off_torch()
        else:
            self.turn_on_torch()

    def turn_on_torch(self):
        self.root.ids.c1.shadow_color = "skyblue"
        self.torch_on = True
        
        self.set_torch_mode(True)

    def turn_off_torch(self):
        self.torch_on = False
        self.root.ids.c1.shadow_color = "black"
        self.set_torch_mode(False)

    def set_torch_mode(self, state):
        # Get the camera manager and the first available camera ID
        activity = PythonActivity.mActivity
        camera_manager = activity.getSystemService(Context.CAMERA_SERVICE)
        camera_id = camera_manager.getCameraIdList()[0]

        # Set the torch mode
        camera_manager.setTorchMode(camera_id, state)
    

   

if __name__ == '__main__':
    TorchApp().run()