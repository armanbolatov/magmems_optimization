import os
import numpy as np
import svgwrite

try:
    import cairosvg
except Exception:
    cairosvg = None

def create_neural_network_diagram(output_file='figs/network_diagram.pdf', width=500, height=300, hidden_band_ratio=0.4):
    layers = [2, 64, 128, 64, 32, 4]

    margin = 0
    content_width = width
    content_height = height

    dwg = svgwrite.Drawing(size=(f'{content_width}px', f'{content_height}px'), profile='tiny')
    dwg.viewbox(0, 0, content_width, content_height)
    dwg['preserveAspectRatio'] = 'xMidYMid meet'

    horizontal_spacing = content_width / (len(layers) + 1)
    neuron_radius = 5

    max_visible_neurons = {
        2: 2,
        64: 8,
        128: 10,
        32: 6,
        4: 4
    }

    layer_colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']
    layer_centers = []

    hidden_layer_height = content_height * hidden_band_ratio

    for i, layer_size in enumerate(layers):
        x_pos = margin + (i + 1) * horizontal_spacing
        visible_neurons = min(layer_size, max_visible_neurons.get(layer_size, 5))
        if 0 < i < len(layers) - 1:
            if visible_neurons > 1:
                vertical_spacing = hidden_layer_height / (visible_neurons - 1)
            else:
                vertical_spacing = 0
            layer_height = hidden_layer_height
        else:
            if visible_neurons > 1:
                vertical_spacing = min(hidden_layer_height / (visible_neurons - 1), 22)
            else:
                vertical_spacing = 0
            layer_height = (visible_neurons - 1) * vertical_spacing

        layer_center_y = content_height / 2
        layer_centers.append((x_pos, layer_center_y))
        neurons_y_positions = []

        for j in range(visible_neurons):
            y_pos = layer_center_y - layer_height/2 + j * vertical_spacing
            if i == 0 or i == len(layers) - 1:
                color = layer_colors[min(i, len(layer_colors) - 1)]
            else:
                color = '#d3d3d3'
            dwg.add(dwg.circle(center=(x_pos, y_pos), r=neuron_radius, fill=color, stroke='black', stroke_width=1))
            neurons_y_positions.append(y_pos)

        if 0 < i < len(layers) - 1:
            dwg.add(dwg.text(str(layer_size), insert=(x_pos - 10, layer_center_y - layer_height/2 - 15), 
                              font_size='12px', font_weight='bold'))

        if i == 0:
            dwg.add(dwg.text('K', insert=(x_pos - 15, neurons_y_positions[0] + 5), font_size='14px', font_style='italic'))
            dwg.add(dwg.text('ξ', insert=(x_pos - 15, neurons_y_positions[1] + 5), font_size='14px', font_style='italic'))

        if i == len(layers) - 1:
            output_labels = ['ω', 'α', 'β', 'γ']
            for j, label in enumerate(output_labels):
                y_pos = neurons_y_positions[j]
                dwg.add(dwg.text(label, insert=(x_pos + 15, y_pos + 5), font_size='14px', font_style='italic'))

        if i > 0:
            prev_x, prev_center_y = layer_centers[i-1]
            prev_visible = min(layers[i-1], max_visible_neurons.get(layers[i-1], 5))
            # Match the spacing logic used for the previous layer regarding hidden vs input/output
            if 0 < i-1 < len(layers) - 1:
                if prev_visible > 1:
                    prev_spacing = hidden_layer_height / (prev_visible - 1)
                else:
                    prev_spacing = 0
                prev_height = hidden_layer_height
            else:
                if prev_visible > 1:
                    # Match the IO compact spacing cap
                    prev_spacing = min(hidden_layer_height / (prev_visible - 1), 22)
                else:
                    prev_spacing = 0
                prev_height = (prev_visible - 1) * prev_spacing
            prev_positions = [prev_center_y - prev_height/2 + j * prev_spacing for j in range(prev_visible)]

            for j, prev_y in enumerate(prev_positions):
                for curr_y in neurons_y_positions:
                    if i == 1 and j == 1:
                        dwg.add(dwg.line(start=(prev_x + neuron_radius, prev_y), 
                                         end=(x_pos - neuron_radius, curr_y), 
                                         stroke='#aaaaaa', stroke_width=0.5, stroke_dasharray="2,2"))
                    else:
                        dwg.add(dwg.line(start=(prev_x + neuron_radius, prev_y), 
                                         end=(x_pos - neuron_radius, curr_y), 
                                         stroke='#aaaaaa', stroke_width=0.5))

    out_dir = os.path.dirname(output_file)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    svg_bytes = dwg.tostring().encode('utf-8')
    if output_file.lower().endswith('.pdf'):
        if cairosvg is None:
            fallback_svg = os.path.splitext(output_file)[0] + '.svg'
            with open(fallback_svg, 'wb') as f:
                f.write(svg_bytes)
            print("CairoSVG is not installed. Install it with 'pip install cairosvg' to export PDF."
                  f" SVG saved to {fallback_svg} instead.")
        else:
            cairosvg.svg2pdf(bytestring=svg_bytes, write_to=output_file, output_width=content_width, output_height=content_height)
            print(f"Neural network diagram saved to {output_file}")
    else:
        with open(output_file, 'wb') as f:
            f.write(svg_bytes)
        print(f"Neural network diagram saved to {output_file}")

if __name__ == "__main__":
    create_neural_network_diagram()
