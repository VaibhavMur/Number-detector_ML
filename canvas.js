
window.addEventListener("load", () => {
  const canvas = document.querySelector("#canvas");
  const ctx = canvas.getContext("2d");
  const clear = document.querySelector("#clear");
  const predict = document.querySelector("#predict");


  // Resizing

  canvas.height = 128;
  canvas.width = 128;

  let painting = false;
  function startPosition(e) {
    painting = true;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    ctx.beginPath();
    ctx.moveTo(x, y);         
  }
  function endPosition() {
    painting = false;
    ctx.beginPath();
  }
  function draw(e) {
    if (!painting) return;

    // Get position relative to canvas
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    ctx.lineWidth = 18;       
    ctx.lineCap = "round";
    ctx.strokeStyle = "#ffffff";

    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();          
    ctx.moveTo(x, y);  
  }       

  function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

  function predictNumber() {
    document.getElementById("result").innerText = "Predicting...";

    const dataURL = canvas.toDataURL("image/png");

    fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ image: dataURL })
    })
    .catch(err => {
      console.error(err);
      document.getElementById("result").innerText = "Error";
    })
    .then(res => res.json())
    .then(data => {
      setTimeout(() => {
        console.log(data.prediction);
        document.getElementById("result").innerText = data.prediction;
      },0);
    })
  }


  //Event Listeners
  canvas.addEventListener('mousedown', startPosition);
  canvas.addEventListener('mouseup', endPosition);
  canvas.addEventListener('mousemove', draw);
  predict.addEventListener('click',predictNumber);
  clear.addEventListener('click', clearCanvas);
})



