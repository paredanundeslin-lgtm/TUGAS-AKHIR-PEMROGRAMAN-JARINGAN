<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
</head>
<body>

<input id="u" placeholder="user">
<input id="p" type="password" placeholder="pass">
<button onclick="login()">Login</button>

<h1 id="out">---</h1>

<script>
function login(){
 fetch("http://localhost:5000/login",{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify({username:u.value,password:p.value})
 }).then(r=>r.json()).then(d=>{
  if(d.status=="ok"){
   const s=io("http://localhost:5000")
   s.on("suhu",x=>{
    out.innerText="Suhu: "+x.nilai
   })
  }
 })
}
</script>

</body>
</html>