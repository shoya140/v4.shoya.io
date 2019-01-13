const whiteColor = "#ffffff"
const brandColor = "#257985"
const grayColor = "#f6f6f6"
const blackColor = "#132238"

$(function(){
  $("a[href^='http']:not([href*='" + location.hostname + "'])").attr('target', '_blank')

  $(".card").hover(function () {
    rollIn($(this), brandColor)
  }, function () {
    rollOut($(this), whiteColor)
  })
  $(".card").click(function () {
    rollOut($(this))
  })

  $(".post-list-item").hover(function(){
    rollIn($(this), brandColor)
  }, function(){
    rollOut($(this), grayColor)
  })
  $(".post-list-item").click(function(){
    rollOut($(this))
  })

  $(".page-button").hover(function(){
    rollIn($(this), brandColor)
  }, function(){
    rollOut($(this), grayColor)
  })
  $(".page-button").click(function(){
    rollOut($(this), grayColor)
  })

  $(".tweet-button").hover(function(){
    rollIn($(this), "#55acee")
  }, function(){
    rollOut($(this), brandColor)
  })
  $(".tweet-button").click(function(){
    rollOut($(this), brandColor)
  })

  $(".facebook-button").hover(function(){
    rollIn($(this), "#3b5998")
  }, function(){
    rollOut($(this), brandColor)
  })
  $(".facebook-button").click(function(){
    rollOut($(this), brandColor)
  })

  $(".hatenabookmark-button").hover(function(){
    rollIn($(this), "#00a8df")
  }, function(){
    rollOut($(this), brandColor)
  })
  $(".hatenabookmark-button").click(function(){
    rollOut($(this), brandColor)
  })

  // image fade
  $(".image-fade").css('visibility','visible').hide().fadeIn(800)
})

function rollIn(body, color){
  body.stop().animate({backgroundColor:color, color:whiteColor}, 50)
  body.children("a").stop().animate({color:whiteColor}, 50)
  body.children("h2").stop().animate({color:whiteColor}, 50)
}

function rollOut(body, color){
  body.stop().animate({backgroundColor:color, color:blackColor}, 100)
  body.children("a").stop().animate({color:blackColor}, 100)
  body.children("h2").stop().animate({color:blackColor}, 100)
}

function mail(){
  var s="FI=;NCIHeBL?@tYG;CFNIqMBIS;eCMBCG;LOwAG;CFe=IGY",r="";
  for(i=0;i<s.length;i++)r+=String.fromCharCode((s.charCodeAt(i)+5)%93+33);eval(r);
}
