from flet import *
from data import gird_list_image


gridcom = GridView(
	expand=3,
	runs_count=5,
	max_extent=150,
	child_aspect_ratio=1,
	spacing=15,
	run_spacing=15

	)

# LOOP IMAGE TO GRID COMPONENT
for x in gird_list_image:
	gridcom.controls.append(
		Card(
			elevation=20,
			content=Image(
				src=x,
			fit=ImageFit.COVER,
			border_radius=border_radius.all(10)

				)
			)

		)

gridscreen = Container(
	margin = margin.only(left=20),
	content= Column([
	Text("Now Showing",weight="bold",size=30,color="white"),
	gridcom

		],scroll="auto")

	)

