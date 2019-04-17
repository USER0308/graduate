let canvas = document.getElementById('canvas')
let	ctx = canvas.getContext('2d')
let center = {x: canvas.width/2, y: canvas.height/2}
var circle = {
	x : center.x,    //圆心的x轴坐标值
    y : center.y,    //圆心的y轴坐标值
    r : 100      //圆的半径         
};
var orgRect = {
	width: circle.r*4,
	height: 200
}

var space = 10

//channel
ctx.beginPath();
ctx.strokeStyle = "blue";
var channel = {
	x : center.x,    //圆心的x轴坐标值
    y : center.y,    //圆心的y轴坐标值
    r : circle.r+space+orgRect.height      //圆的半径         
};
     //沿着坐标点(100,100)为圆心、半径为50px的圆的顺时针方向绘制弧线, start from 0 ,end to 2 pi, true is 逆时针
ctx.arc(channel.x, channel.y, channel.r, 0, Math.PI*2, false);    
    //按照指定的路径绘制弧线
ctx.fillStyle = "pink"
ctx.fill();

ctx.beginPath();
ctx.arc(channel.x, channel.y, channel.r-50, 0, Math.PI*2, false);    
//按照指定的路径绘制弧线
ctx.fillStyle = "white"
ctx.fill();


// orderer
ctx.beginPath();
// ctx.strokeStyle = "blue";

     //沿着坐标点(100,100)为圆心、半径为50px的圆的顺时针方向绘制弧线, start from 0 ,end to 2 pi, true is 逆时针
ctx.arc(circle.x, circle.y, circle.r, 0, Math.PI*2, false);    
    //按照指定的路径绘制弧线
//ctx.stroke();
ctx.fillStyle = 'blue'
ctx.fill()

ctx.fillStyle = 'red'
ctx.font="40px Arial";
ctx.fillText("Orderer",center.x-70,center.y+10);



//organization
ctx.beginPath();
ctx.rect(center.x-orgRect.width/2, center.y-circle.r-space-orgRect.height,orgRect.width,orgRect.height); // width 200, height 100
ctx.fillStyle="green";
ctx.fill();

// organization
ctx.beginPath();
ctx.rect(center.x-orgRect.width/2, center.y+circle.r+space,orgRect.width, orgRect.height); // width 200, height 100
ctx.fillStyle="green";
ctx.fill();

var peerNum = 2

var peerRect = {
	width: (orgRect.width-(peerNum+1)*space*2)/2,
	height:orgRect.height-space*2
}

//peer
ctx.beginPath();
ctx.rect(center.x-orgRect.width/2+space*2, center.y-circle.r-space*2-peerRect.height,peerRect.width,peerRect.height); // ,   
ctx.fillStyle="yellow";
ctx.fill();
// ctx.fillStyle = 'red'
// ctx.font="40px Arial";
// ctx.fillText("Peer",center.x-70,center.y+10);
//peer
ctx.beginPath();
ctx.rect(center.x+orgRect.width/2-space*2-peerRect.width, center.y-circle.r-space*2-peerRect.height,peerRect.width,peerRect.height); // ,   
ctx.fillStyle="yellow";
ctx.fill();

//peer
ctx.beginPath();
ctx.rect(center.x-orgRect.width/2+space*2, center.y+circle.r+space*2,peerRect.width,peerRect.height); // ,   
ctx.fillStyle="yellow";
ctx.fill();

//peer
ctx.beginPath();
ctx.rect(center.x+orgRect.width/2-space*2-peerRect.width, center.y+circle.r+space*2,peerRect.width,peerRect.height); // ,   
ctx.fillStyle="yellow";
ctx.fill();





canvas.addEventListener('click', function(e) {
	
}, false)


