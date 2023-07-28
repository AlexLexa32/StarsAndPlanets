const root = document.getElementById("cnvs");
const cnvs = root.getContext("2d");
let G = 2
let dt = 0.01

class Matter {
    constructor(m, r, x, y, vx, vy, clr) {
        this.m = m;
        this.r = r;
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.clr = clr;
    }
    date() {
        return {'m': this.m, 'x': this.x, 'y': this.y, 'vx': this.vx, 'vy': this.vy, 'clr': this.clr};
    }
    move() {
        this.x += this.vx*dt;
        this.y += this.vy*dt;
//        cnvs.arc(this.x, this.y, this.r, 0, 2*Math.PI, false);
//        cnvs.fillStyle = this.clr;
//        cnvs.fill();
        cnvs.fillStyle = this.clr;
        cnvs.fillRect(this.x, this.y, this.r, this.r);
    }
    upd(vx, vy) {
        this.vx += vx;
        this.vy += vy;
    }
}
let Matters = [
    new Matter(10000, 15, 240, 200, 0, 0, 'green'),
    new Matter(10, 15,  200, 200, -1, 23, 'black')
];

function rendering() {
    cnvs.fillStyle = 'white'
    //cnvs.fillRect(0, 0, 1600, 2500)
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
