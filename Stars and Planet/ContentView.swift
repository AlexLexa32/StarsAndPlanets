//
//  ContentView.swift
//  Stars and Planet
//
//  Created by Oleg Yakushin on 7/27/23.
//

import SwiftUI

let WIDTH: CGFloat = 600
let HEIGHT: CGFloat = 400
let R: CGFloat = 5
let G: CGFloat = 1
let dt: Double = 0.1
struct Matter: Identifiable {
    let id = UUID()
    var m: CGFloat
    var x: CGFloat
    var y: CGFloat
    var vx: CGFloat
    var vy: CGFloat
    var clr: String
    var speed: Double

    mutating func move() {
        x += vx * CGFloat(dt)
        y += vy * CGFloat(dt)
    }

    func calculateForces(_ other: Matter) -> (CGFloat, CGFloat) {
        let sx = x - other.x
        let sy = y - other.y
        let s = sqrt(sx * sx + sy * sy)
        let F = G * m * other.m / (s * s)
        let Fx = sx * F / s
        let Fy = sy * F / s
        return (-Fx * CGFloat(dt) / m, -Fy * CGFloat(dt) / m)
    }

    mutating func updateVelocity(_ fx: CGFloat, _ fy: CGFloat) {
        vx += fx
        vy += fy
    }
}

struct ContentView: View {
    @State private var matters: [Matter] = [
        Matter(m: 1, x: 280, y: 200, vx: 0, vy: 4, clr: "1", speed: 10),
        Matter(m: 10000, x: 200, y: 200, vx: 0, vy: 0, clr: "2", speed: 20),
        Matter(m: 1, x: 300, y: 300, vx: 0, vy: -5, clr: "3", speed: 15),
        Matter(m: -200, x: 150, y: 300, vx: 0, vy: -5, clr: "4", speed: 200),
        Matter(m: 1, x: 200, y: 240, vx: 5, vy: 0, clr: "5", speed: 1),
        
        
    ]
    @State private var rotationAngle: Angle = .degrees(0)
    let rotationSpeed: Double = 10

    private let timer = Timer.publish(every: dt, on: .main, in: .common).autoconnect()

    var body: some View {
        ZStack {
           // Color.black
            Image("Space")
                .resizable()
                //.scaledToFill()
                .ignoresSafeArea()

            ForEach(matters) { matter in
                Circle()
                
                 
                    .overlay(
                    Image(matter.clr)
                        .resizable()
                        .scaledToFit()
                        .cornerRadius(100)
                        .rotationEffect(rotationAngle)
                        
                 
                        
                    )
                    .frame(width: R * 10, height: R * 10)
                    .position(x: matter.x, y: matter.y)
                    .onAppear {
                        let timer = Timer.scheduledTimer(withTimeInterval: 0.05, repeats: true) { _ in
                            withAnimation {
                                rotationAngle += .degrees(matter.speed * 0.05)
                            }
                        }
                        timer.fire()
                    }
                   
            }
        }
       // .frame(width: WIDTH, height: HEIGHT)
        .onReceive(timer) { _ in
            updateSimulation()
        }
    }

    private func updateSimulation() {
        for i in matters.indices {
            for j in 0..<i {
                let (fxi, fyi) = matters[i].calculateForces(matters[j])
                let (fxj, fyj) = matters[j].calculateForces(matters[i])
                matters[i].updateVelocity(fxi, fyi)
                matters[j].updateVelocity(fxj, fyj)
            }
        }

        for i in matters.indices {
            matters[i].move()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}




