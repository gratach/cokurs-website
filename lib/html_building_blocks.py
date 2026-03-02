dreidbox = """
<div class= "kasten">
	<a href = "%s"> 
		<img class="rm" src = "%s" title = "%s"/>
	</a>
</div>
"""
schriftbox = """
<div class= "kasten">
	<a href = "/font-test/lade.html?pfad=%s" target = "_top"> 
		<img class = "rm" src = "%s" title = "%s"/>
	</a>
</div>
"""
bitmapbox = """
<div class= "kasten">
	<a href = "%s" target = "_self"> 
		<img class="rm" src = "%s" title = "%s"/>
	</a>
</div>
"""
audiobox = """
<div class= "kasten musik">
		<div title = "%s">
			<audio controls>
				<source src="%s" type="audio/mpeg">
				Your browser does not support the audio element.
			</audio>
		</div>
	</div>
"""
gifbox = """
<div class= "kasten">
	<div class="hintergrund" style="background-image:url('%s')" title = "%s">
		<button class = "pisk" style = "background-image:url('%s')"/>
	</div>
</div>
"""
htmlbox = """
<a href = "%s" target = "_blank">
	<div class= "kasten textbox orange"  title = "%s">
		<p class = "text"/>%s</p>
	</div>
</a>
"""
scratchbox = """
<a href = "%s" target = "_blank">
	<div class= "kasten textbox gelb"  title = "%s">
		<p class = "text"/>%s</p>
	</div>
</a>
"""
svgbox = """
<div class= "kasten">
	<a href = "%s"> 
		<img class = "rm" src = "%s" title = "%s"/>
	</a>
</div>
"""
kopf = """
<html>
  <head>
    <title></title>
    <meta content="">
    <meta charset="utf-8">
    <style>
*{box-sizing: border-box; margin:0;border:0;padding:0;}
body, html {
  height: 100%;
  margin: 0;
	background-color: lightblue;
}
.kasten{
	width:14.2857%;
	height:14.2857vw;
  float: left;
   overflow: hidden;
}

@media screen and (max-width: 1200px) {
  .kasten {
	width:16.666667%;
	height:16.666667vw;
  }
}
@media screen and (max-width: 1000px) {
  .kasten {
	width:20%;
	height:20vw;
  }
}
@media screen and (max-width: 800px) {
  .kasten {
	width:25%;
	height:25vw;
  }
}
@media screen and (max-width: 600px) {
  .kasten {
	width:33.333333%;
	height:33.333333vw;
  }
}
@media screen and (max-width: 400px) {
  .kasten {
	width:50%;
	height:50vw;
  }
}
@media screen and (max-width: 200px) {
  .kasten {
	width:100%;
	height:100vw;
  }
}
.textbox{
	border-width: 1vmin;
	border-style: solid;
	border-color: black;
	position: relative;
}
.orange{
	background-color: orange;
}
.gelb{
	background-color: yellow;
}
.blau{
	color: darkblue;
}
.text{
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	font-size: 3vmin;
}
a, img, .seite{
	height:100%;
	width:100%;
}
.htmllink{
	background-image: url("logos/html.svg");
	background-position: center;
	  background-repeat: no-repeat;
	  background-size: cover;
	display: inline-block;
}
.musik{
	background-image: url("musikicon.svg");
	background-position: center;
	  background-repeat: no-repeat;
	  background-size: cover;
	display: inline-block;
}
.rm{
	image-rendering: pixelated;
	image-rendering: -moz-crisp-edges;
	image-rendering: crisp-edges;
}
.pisk{
	image-rendering: pixelated;
	image-rendering: -moz-crisp-edges;
	image-rendering: crisp-edges;
	width : 100%;
	height : 100%;
	background-color: lightblue;
	background-size: cover;
	opacity:0;
}
.pisk:focus{
	opacity:1;
}
.hintergrund{
	image-rendering: pixelated;
	image-rendering: -moz-crisp-edges;
	image-rendering: crisp-edges;
	width : 100%;
	height : 100%;
	background-size: cover;
}
</style>
  </head>
  <body>
"""
fuss = """
</body>
</html>
"""