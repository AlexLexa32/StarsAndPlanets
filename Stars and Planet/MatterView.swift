//
//  MatterView.swift
//  Stars and Planet
//
//  Created by Oleg Yakushin on 7/27/23.
//

import SwiftUI

struct MatterView: View {
    @Binding var x: Double
    @Binding var y: Double
    var color: Color

    var body: some View {
        Circle()
            .frame(width: CGFloat(2 * R), height: CGFloat(2 * R))
            .position(x: CGFloat(x), y: CGFloat(y))
            .foregroundColor(color)
    }
}

