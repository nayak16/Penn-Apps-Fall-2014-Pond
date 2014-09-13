function AnimateIt(e, cont) {
    var theDiv = $(e),
        theContainer = $(cont),
        maxLeft = theContainer.width() - theDiv.width(),
        maxTop = theContainer.height() - theDiv.height(),
        leftPos = Math.floor(Math.random() * maxLeft),
        topPos = Math.floor(Math.random() * maxTop);
      
    
  
    theDiv.animate({
        "left": leftPos,
        "top": topPos
    }, 2000, AnimateIt);
}
