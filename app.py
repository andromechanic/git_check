# Save this as app.py and run:
# pip install flask
# python app.py
#
# Then open: http://127.0.0.1:5000

from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Sooraj</title>

<style>
    *{
        margin:0;
        padding:0;
        box-sizing:border-box;
        font-family: Arial, Helvetica, sans-serif;
    }

    :root{
        --bg:#0f172a;
        --text:#ffffff;
        --card:rgba(255,255,255,0.06);
        --border:rgba(255,255,255,0.1);
    }

    body.light{
        --bg:#f4f4f5;
        --text:#111827;
        --card:rgba(255,255,255,0.7);
        --border:rgba(0,0,0,0.08);
    }

    body{
        background: var(--bg);
        color: var(--text);
        overflow:hidden;
        height:100vh;
        transition:0.4s ease;
        position:relative;
    }

    canvas{
        position:fixed;
        top:0;
        left:0;
        width:100%;
        height:100%;
        z-index:0;
    }

    .container{
        position:relative;
        z-index:2;
        height:100vh;
        display:flex;
        align-items:center;
        justify-content:center;
        flex-direction:column;
        text-align:center;
        padding:20px;
    }

    .glass{
        backdrop-filter: blur(14px);
        background: var(--card);
        border:1px solid var(--border);
        padding:40px;
        border-radius:24px;
        box-shadow:0 10px 40px rgba(0,0,0,0.2);
        animation: float 4s ease-in-out infinite;
    }

    h1{
        font-size: clamp(2rem, 6vw, 5rem);
        font-weight:800;
        letter-spacing:1px;
    }

    p{
        margin-top:15px;
        font-size:1.2rem;
        opacity:0.8;
    }

    .toggle{
        position:fixed;
        top:20px;
        right:20px;
        z-index:5;
        border:none;
        padding:12px 18px;
        border-radius:999px;
        cursor:pointer;
        background:rgba(255,255,255,0.1);
        color:white;
        backdrop-filter: blur(10px);
        transition:0.3s;
        font-size:14px;
    }

    body.light .toggle{
        color:black;
        background:rgba(0,0,0,0.08);
    }

    .toggle:hover{
        transform:scale(1.08);
    }

    @keyframes float{
        0%{ transform:translateY(0px); }
        50%{ transform:translateY(-10px); }
        100%{ transform:translateY(0px); }
    }
</style>
</head>
<body>

<button class="toggle" onclick="toggleTheme()">🌙 Toggle Mode</button>

<canvas id="bg"></canvas>

<div class="container">
    <div class="glass">
        <h1>Hi, I am Sooraj</h1>
        <p>Let's do something big 🚀</p>
    </div>
</div>

<script>
    const body = document.body;

    function toggleTheme(){
        body.classList.toggle("light");
    }

    // PARTICLE BACKGROUND
    const canvas = document.getElementById("bg");
    const ctx = canvas.getContext("2d");

    let w = canvas.width = window.innerWidth;
    let h = canvas.height = window.innerHeight;

    let mouse = {
        x: w / 2,
        y: h / 2
    };

    window.addEventListener("mousemove", (e)=>{
        mouse.x = e.clientX;
        mouse.y = e.clientY;
    });

    window.addEventListener("resize", ()=>{
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
    });

    class Particle{
        constructor(){
            this.x = Math.random() * w;
            this.y = Math.random() * h;
            this.size = Math.random() * 3 + 1;
            this.vx = (Math.random() - 0.5) * 1;
            this.vy = (Math.random() - 0.5) * 1;
        }

        update(){
            this.x += this.vx;
            this.y += this.vy;

            // Mouse interaction
            let dx = mouse.x - this.x;
            let dy = mouse.y - this.y;
            let dist = Math.sqrt(dx*dx + dy*dy);

            if(dist < 120){
                this.x -= dx * 0.01;
                this.y -= dy * 0.01;
            }

            if(this.x < 0 || this.x > w) this.vx *= -1;
            if(this.y < 0 || this.y > h) this.vy *= -1;
        }

        draw(){
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = body.classList.contains("light")
                ? "rgba(0,0,0,0.5)"
                : "rgba(255,255,255,0.7)";
            ctx.fill();
        }
    }

    const particles = [];

    for(let i=0;i<120;i++){
        particles.push(new Particle());
    }

    function connectParticles(){
        for(let a=0;a<particles.length;a++){
            for(let b=a;b<particles.length;b++){
                let dx = particles[a].x - particles[b].x;
                let dy = particles[a].y - particles[b].y;
                let distance = Math.sqrt(dx*dx + dy*dy);

                if(distance < 100){
                    ctx.beginPath();
                    ctx.strokeStyle = body.classList.contains("light")
                        ? "rgba(0,0,0,0.08)"
                        : "rgba(255,255,255,0.08)";
                    ctx.lineWidth = 1;
                    ctx.moveTo(particles[a].x, particles[a].y);
                    ctx.lineTo(particles[b].x, particles[b].y);
                    ctx.stroke();
                }
            }
        }
    }

    function animate(){
        ctx.clearRect(0,0,w,h);

        particles.forEach(p=>{
            p.update();
            p.draw();
        });

        connectParticles();

        requestAnimationFrame(animate);
    }

    animate();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)