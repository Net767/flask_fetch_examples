function handleKeyPress(e){
  console.log(e);
  var key=e.keyCode || e.which;
   if (key==13){
      console.log("Enter pressed");
   }
 }