const root = document.getElementById("cnvs");
const cnvs = root.getContext("2d");
let G = 0.667
let dt = 0.0001

class Matter {
    constructor(m, r, x, y, vx, vy, src) {
        this.m = m;
        this.r = r;
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.img = new Image();
        this.img.src = src;
    }
    date() {
        return {'m': this.m, 'x': this.x, 'y': this.y, 'vx': this.vx, 'vy': this.vy, 'img': this.img};
    }
    move() {
        this.x += this.vx*dt;
        this.y += this.vy*dt;
//        cnvs.arc(this.x, this.y, this.r, 0, 2*Math.PI, false);
//        cnvs.fillStyle = this.clr;
//        cnvs.fill();
        cnvs.drawImage(this.img, this.x - this.r, this.y - this.r, this.r<<1, this.r<<1);
    }
    upd(vx, vy) {
        this.vx += vx;
        this.vy += vy;
    }
}
let Matters = [
    new Matter(198892000000, 25, 349.5, 200, 0, 0, 'red_planet.png'),
    new Matter(597420, 25,  200, 200, 0, 29765, 'Earth.png')
];

function rendering() {
    cnvs.fillStyle = 'white'
    cnvs.fillRect(0, 0, 1600, 2500)
    for (let i = 0; i < 2; ++i) {
        for (let j = 0; j < i; ++j) {
            let a = Matters[i].date();
            let b = Matters[j].date();
            let sx = a['x'] - b['x'];
            let sy = a['y'] - b['y'];
            let s = Math.sqrt(sx*sx+sy*sy);
            let F = G * a['m'] * b['m'] / (s * s);
            let Fx = sx * F / s;
            let Fy = sy * F / s;
            Matters[i].upd(-Fx * dt / a['m'], -Fy * dt / a['m']);
            Matters[j].upd(Fx * dt / b['m'], Fy * dt / b['m']);
        }
        //console.log(Matters[i].date());
        Matters[i].move();
    }
}

let w = setInterval(rendering, 10);
