from flet import *
from data import data_movie


listmovie = Row()

for x in data_movie:
	listmovie.controls.append(
		Stack([
			Container(
				width=240,
				height=170,
				border_radius = border_radius.all(30),
				content=Image(
					# IMAGE RENDER 
					src=x['image'],
					width=300,
					height=270,
					border_radius=border_radius.all(30),
					fit=ImageFit.COVER
					)
				),
			# FOR TITLE AND DESCRIPTION FOR IMAGE POSTER
			Container(
			width=240,
			padding=padding.only(left=10),
			gradient=LinearGradient(
			begin= alignment.bottom_center,
			end = alignment.top_center,
			colors=["black","#48"]
			# 48 IS FOR TRANSPARENT BLACK
			),
			bottom=10,
			content=Column([
		Text(x["title"],weight="bold",size=18,color="white"),
		Text("Now Showing",color="white",size=12)

			],spacing=0)
		)

			])


		)


section2 = Container(
	margin = margin.only(left=20),
	content= Column([
	Text("For You",weight="bold",size=25,color="white"),
	Row([
		listmovie
		# THIS FOR SCROLL HORIZONTAL
		],scroll="always")

		],spacing=1)

	)