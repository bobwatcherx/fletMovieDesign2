from flet import *

appmenu = Row([
	CircleAvatar(
		foreground_image_url="https://images.unsplash.com/photo-1562904403-a5106bef8319?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aW5kb25lc2lhbiUyMHdvbWFufGVufDB8fDB8fA%3D%3D&w=1000&q=80"
	),
	Container(
		margin = margin.symmetric(vertical=40),
		content=Row([
			Icon(name="pin_drop",color="white"),
			Text("Bekasi City",color="white"),
			Icon(name="search",color="white"),

			])
		)


	],alignment="spaceAround")