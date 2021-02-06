import kivy
import sqlite3
from kivy.config import Config
from kivymd.uix.card import MDCardSwipe
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.uix.button import Button,ButtonBehavior

#def connect_to_database(self):
#def create_table(cursor):
#	cursor.execute("""
#	CREATE TABLE product(
#	ID INTEGER PRIMARY KEY AUTOINCREMENT,
#	name text not null,
#	age int not null,
#	mobile int not null
#	)
#	""")
		
from kivy.lang import Builder
Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import F kivy.factory.Factory
#:import Factory kivy.factory.Factory

<<MainWid>MainWid>:
	canvas:
		Color:
			rgb:1,1,1
		Rectangle:
			size:self.size
			pos:self.pos
<<StartWid>StartWid>:
	FloatLayout:
		canvas:
			Rectangle:
				size:self.size
				pos:self.pos
				#source:'crm.jpg'
		
		MDToolbar:
			title:'Login_Screen'
			md_bg_color: get_color_from_hex('7f00ff')
			pos_hint:{'x':.0,'y':.915}
		MDLabel:
		    text: "Techa Log"
		    halign:'center'
		    font_style:'H5'
		    color:get_color_from_hex('7f00ff')
		    pos_hint:{'x':.0,'y':-.4}
		Image:
			source:'lock.png'
			size_hint:.4,.5
			pos_hint:{'x':.0,'y':.3}
			
		MDTextField:
    		hint_text: "User Name"
    		pos_hint:{'x':.5,'y':.6}
    		size_hint_x:.5
    		color_mode:'custom'
    		line_color_focus:get_color_from_hex('7f00ff')
    	MDTextField:
    		hint_text: "Password"
    		pos_hint:{'x':.5,'y':.5}
    		size_hint_x:.5
    		icon_right: 'eye-off'
    		color_mode:'custom'
    		line_color_focus:get_color_from_hex('7f00ff')
    	MDFillRoundFlatButton:
    		text:'login'
    		pos_hint:{'x':.5,'y':.42}
    		size_hint_x:.3
    		md_bg_color: get_color_from_hex('7f00ff')
    		#on_release:root.create_database()
    		on_release:
    			root.options()
    	
<<Options>Options>:
	FloatLayout:
		canvas:
			Color:
				rgb:get_color_from_hex('7f00ff')
			Rectangle:
				size:self.size
				pos:self.pos
		MDToolbar:
			title:'Institute'
			left_action_items: [["menu", lambda x: x]]
			right_action_items: [["help-circle-outline", lambda x:x]]
			md_bg_color: get_color_from_hex('7f00ff')
			pos_hint:{'x':.0,'y':.915}
		FloatLayout:
			pos_hint:{'x':.0,'y':.0}
			size_hint:1,.8
			canvas.before:
                Color:
                    rgba:get_color_from_hex('#ffffff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[90,90,0,0]
			ImageButton:
				source:'student.png'
				font_color:0,0,0,1
				size_hint_y:.2
				size_hint_x:.2
				pos_hint:{'x':.2,'y':.7}
				back_color:(0,0,0,.2)
				on_press:
					root.create_database()
					root.direction='left'
				
			ImageButton:
				source:'sports.png'
				size_hint_y:.2
				size_hint_x:.2
				pos_hint:{'x':.6,'y':.7}
				back_color:(0,0,0,.2)
				
			ImageButton:
				source:'transport.png'
				size_hint_y:.2
				size_hint_x:.2
				pos_hint:{'x':.2,'y':.5}
				back_color:(0,0,0,.2)
				
			ImageButton:
				source:'teacher.png'
				size_hint_y:.2
				size_hint_x:.2
				pos_hint:{'x':.6,'y':.5}
				back_color:(0,0,0,.2)
				
			ImageButton:
				source:'search.png'
				size_hint_y:.2
				size_hint_x:.2
				pos_hint:{'x':.2,'y':.3}
				back_color:(0,0,0,.2)
			ImageButton:
				source:'fee.png'
				size_hint_y:.2
				size_hint_x:.2
				pos_hint:{'x':.6,'y':.3}
				back_color:(0,0,0,.2)
		             
		FloatLayout:
			pos_hint:{'x':0.050,'y':.010}
			size_hint:.900,.1
			canvas.before:
				Color:
					rgba:get_color_from_hex('7f00ff')
				RoundedRectangle:
					size:self.size
					pos:self.pos
					radius:[30,]
			ImageButton:
				source:'cross.png'
				size_hint:.3,.3
				pos_hint:{'x':.0,'y':.3}
				on_release:app.stop()
			ImageButton:
				source:'home.png'
				size_hint:.3,.3
				pos_hint:{'x':.35,'y':.3}
			ImageButton:
				source:'back1.png'
				size_hint:.3,.3
				pos_hint:{'x':.7,'y':.3}
				on_release:root.start()
   
			
			
<<DataBaseWid>DataBaseWid>:
	FloatLayout:
		canvas:
			Color:
				rgb:get_color_from_hex('fbfbf8')
			Rectangle:
				size:self.size
				pos:self.pos
		MDToolbar:
			title:'Students_Detail'
			left_action_items: [["menu", lambda x: x]]
			right_action_items: [["help-circle-outline", lambda x:x]]
			md_bg_color: get_color_from_hex('7f00ff')
			pos_hint:{'x':.0,'y':.915}
		MDTextField:
    		hint_text: "Search"
    		pos_hint:{'x':.1,'y':.81}
    		size_hint_x:.8
    		icon_right: 'magnify'
    		color_mode:'custom'
    		line_color_focus:get_color_from_hex('7f00ff')
			
		ScrollView:
			size_hint:1,.66
			pos_hint:{'x':.0,'y':.14}
			GridLayout:
				id:container
				cols:2
				height:self.minimum_height
				row_default_height:280
				size_hint_y:None

		FloatLayout:
			pos_hint:{'x':0.050,'y':.010}
			size_hint:.900,.1
			canvas.before:
				Color:
					rgba:get_color_from_hex('7f00ff')
				RoundedRectangle:
					size:self.size
					pos:self.pos
					radius:[30,]
			ImageButton:
				source:'cross.png'
				size_hint:.3,.3
				pos_hint:{'x':.0,'y':.3}
				on_release:app.stop()
				border:30,30,30,30
			ImageButton:
				source:'home.png'
				size_hint:.3,.3
				pos_hint:{'x':.35,'y':.3}
			ImageButton:
				source:'back1.png'
				size_hint:.3,.3
				pos_hint:{'x':.7,'y':.3}
				on_release:
					root.options()
					root.direction='up'
		MDFloatingActionButton:
			icon: "plus"
			pos_hint:{'x':.82,'y':.15}
			#theme_text_color: "Custom"
			text_color:get_color_from_hex('#ffffff')
			md_bg_color:get_color_from_hex('7f00ff')
			on_release:root.create_new_product()
		
<<LeftLabel@Label>LeftLabel@Label>:
	text_size:self.size
	halign:'left'<
<DataWid>DataWid>:
	data:''
	data_id:''
	r2:''
	r3:''
	r4:''
	FloatLayout:
		MDCard:
			focus_behavior:True
        	ripple_behavior: True
			#focus_behavior: True
	        orientation: "vertical"
	        padding: "4dp"
	        size_hint: None, None
	        size: "163dp", "130dp"
	        pos_hint: {"center_x": .5, "center_y": .5}
	        MDLabel:
	        	orientation:'vertical'
	            text: root.r2
	            theme_text_color: "Secondary"
	            size_hint_y: None
	            height: self.texture_size[1]
	        MDSeparator:
	            height: "1dp"
			MDLabel:
	            text: root.r3
	        MDLabel:
	            text: root.r4
		MDIconButton:
			icon:'account-edit'
			pos_hint:{'x':.75,'y':.7}
			on_press:root.update_data(root.data_id)
		MDIconButton:
			icon:"account-remove"
			pos_hint:{'x':.75,'y':.4}
			on_release:root.delete_data()	
		

<<InsertDataWid>InsertDataWid>:
	FloatLayout:
		canvas:
			Color:
				rgb:get_color_from_hex('7f00ff')
			Rectangle:
				size:self.size
				pos:self.pos
		MDToolbar:
			title:'Add_User'
			left_action_items: [["menu", lambda x: x]]
			right_action_items: [["help-circle-outline", lambda x:x]]
			md_bg_color: get_color_from_hex('7f00ff')
			pos_hint:{'x':.0,'y':.915}
		FloatLayout:
			pos_hint:{'x':.0,'y':.0}
			size_hint:1,.8
			canvas.before:
                Color:
                    rgba:get_color_from_hex('#ffffff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[90,90,0,0]
			MDTextField:
				id:ti_name
				pos_hint:{'x':.2,'y':.8}
				size_hint_x:.7
				hint_text:'User_Name'
				color_mode:'custom'
				line_color_focus:get_color_from_hex('7f00ff')
			MDTextField:
				id:ti_age
				pos_hint:{'x':.2,'y':.7}
				hint_text:'Age'
				size_hint_x:.7
				color_mode:'custom'
				line_color_focus:get_color_from_hex('7f00ff')
			MDTextField:
			    id:ti_mobile
			    pos_hint:{'x':.2,'y':.6}
			    hint_text:'Mobile_No'
			    size_hint_x:.7
			    color_mode:'custom'
			    line_color_focus:get_color_from_hex('7f00ff')
			MDFillRoundFlatButton:
			    text:'Save'
			    pos_hint:{'x':.4,'y':.5}
			    on_release:root.insert_data()
			    md_bg_color:get_color_from_hex('7f00ff')
		             
		FloatLayout:
			pos_hint:{'x':0.050,'y':.010}
			size_hint:.900,.1
			canvas.before:
				Color:
					rgba:get_color_from_hex('7f00ff')
				RoundedRectangle:
					size:self.size
					pos:self.pos
					radius:[30,]
			ImageButton:
				source:'cross.png'
				size_hint:.3,.3
				pos_hint:{'x':.0,'y':.3}
				on_release:app.stop()
			ImageButton:
				source:'home.png'
				size_hint:.3,.3
				pos_hint:{'x':.35,'y':.3}
				on_release:root.options()
			ImageButton:
				source:'back1.png'
				size_hint:.3,.3
				pos_hint:{'x':.7,'y':.3}
				on_release:root.back_to_dbw()
<<UpdateDataWid>UpdateDataWid>:
	FloatLayout:
		FloatLayout:
			pos_hint:{'x':0.050,'y':.010}
			size_hint:.900,.1
			canvas.before:
				Color:
					rgba:get_color_from_hex('7f00ff')
				RoundedRectangle:
					size:self.size
					pos:self.pos
					radius:[30,]
			ImageButton:
				source:'cross.png'
				size_hint:.3,.3
				pos_hint:{'x':.0,'y':.3}
				on_release:app.stop()
			ImageButton:
				source:'home.png'
				size_hint:.3,.3
				pos_hint:{'x':.35,'y':.3}
				on_release:root.options()
			ImageButton:
				source:'back1.png'
				size_hint:.3,.3
				pos_hint:{'x':.7,'y':.3}
				on_release:root.back_to_dbw()
""")

class MainWid(ScreenManager):
	def _init_(self,**kwarg):
		super(MainWid,self)._init_()
		self.StartWid=StartWid(self)
		self.Options=Options(self)
		self.DataBaseWid=DataBaseWid(self)
		self.InsertDataWid=InsertDataWid(self)
		self.UpdateDataWid=BoxLayout()
		
		
		wid=Screen(name='start')
		wid.add_widget(self.StartWid)
		self.add_widget(wid)
		wid=Screen(name='options')
		wid.add_widget(self.Options)
		self.add_widget(wid)
		wid=Screen(name='database')
		wid.add_widget(self.DataBaseWid)
		self.add_widget(wid)
		wid=Screen(name='insertdata')
		wid.add_widget(self.InsertDataWid)
		self.add_widget(wid)
		
		wid=Screen(name='updatedata')
		wid.add_widget(self.UpdateDataWid)
		self.add_widget(wid)
		
		self.goto_start()
		
	def goto_start(self):
		self.current='start'
		
	def goto_options(self):
		self.current='options'
		
	def goto_database(self):
		self.DataBaseWid.check_memory()
		self.current='database'
		
	def goto_insertdata(self):
		self.InsertDataWid.clear_widgets()
		wid=InsertDataWid(self)
		self.InsertDataWid.add_widget(wid)
		self.current='insertdata'
	
	def goto_updatedata(self,data_id):
		self.UpdateDataWid.clear_widgets()
		wid=UpdateDataWid(self,data_id)
		self.UpdateDataWid.add_widget(wid)
		self.current='updatedata'
	
	
class StartWid(BoxLayout):
	def _init_(self,mainwid,**kwargs):
		super(StartWid,self)._init_()
		self.mainwid=mainwid
	def options(self):
		self.mainwid.goto_options()
		
class DataBaseWid(BoxLayout,Screen):
	def _init_(self,mainwid,**kwargs):
		super(DataBaseWid,self)._init_()
		self.mainwid=mainwid
	def check_memory(self):
		self.ids.container.clear_widgets()
		con=sqlite3.connect('new.db')
		cursor=con.cursor()
		cursor.execute("""SELECT * from product""")
		row = cursor.fetchall()
		for i in row:
			wid=DataWid(self.mainwid)
			r1=str(i[0])+'\n'
			r2=str(i[1])+'\n'
			r3=str(i[2])+'\n'
			r4=str(i[3])
			wid.data_id=str(i[0])
			wid.r2=str(i[1])
			wid.r3=str(i[2])
			wid.r4=str(i[3])
			wid.data=r1+r2+r3+r4
			self.ids.container.add_widget(wid)
			con.close()
	def create_new_product(self):
		self.mainwid.goto_insertdata()
	def options(self):
		self.mainwid.goto_options()

class InsertDataWid(BoxLayout):
	def _init_(self,mainwid,**kwargs):
		super(InsertDataWid,self)._init_()
		self.mainwid=mainwid
	def insert_data(self):
		con=sqlite3.connect('new.db')
		cursor=con.cursor()
		d1=self.ids.ti_name.text
		d2=self.ids.ti_age.text
		d3=self.ids.ti_mobile.text
		cursor.execute("""INSERT INTO product (name,age,mobile)VALUES(?,?,?)""" , (d1,d2,d3))
		con.commit()
		con.close()
		self.mainwid.goto_database()
	def back_to_dbw(self):
		self.mainwid.goto_database()
	def options(self):
		self.mainwid.goto_options()

class Options(BoxLayout,Screen):
	def _init_(self,mainwid,**kwargs):
		super(Options,self)._init_()
		self.mainwid=mainwid
	def create_database(self):
		self.mainwid.goto_database()
	def start(self):
		self.mainwid.goto_start()
		
class UpdateDataWid(BoxLayout):
	def _init_(self,mainwid,data_id,**kwargs):
		super(UpdateDataWid,self)._init_()
		self.mainwid=mainwid
		self.data_id=data_id
		self.check_memory()
	def check_memory(self):
		pass
	def update_data(self):
		pass
	def delete_data(self):
		con=sqlite3.connect('new.db')
		cur=con.cursor()
		cur.execute('delete from product where ID='+self.data_id)
		con.commit()
		con.close()
		self.mainwid.goto_database()
	def back_to_dbw(self):
		self.mainwid.goto_database()
		
		
class DataWid(BoxLayout):
	def _init_(self,mainwid,**kwargs):
		super(DataWid,self)._init_()
		self.mainwid=mainwid
	def delete_data(self):
		con=sqlite3.connect('new.db')
		cur=con.cursor()
		cur.execute('delete from product where ID='+self.data_id)
		con.commit()
		con.close()
		self.mainwid.goto_database()
	def update_data(self,data_id):
		self.mainwid.goto_updatedata(data_id)


class NewDataButton(Button):
	def _init_(self,mainwid,**kwargs):
		super(NewDataButton,self)._init_()
		self.mainwid=mainwid
	def create_new_product(self):
		self.mainwid.goto_insertdata()

class ImageButton(ButtonBehavior,Image):
	pass
	
class mainapp(MDApp):
	title='invention'
	def build(self):
		return MainWid()
if _name=='main_':
	mainapp().run()