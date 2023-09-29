// Parameters
$fn = 100; // High value to make circles appear as circles
width = 90; // Width of the rectangle
height = 55; // Height of the rectangle
border_thickness = 3.5; // Thickness of the extruded border
radius = 10; // Radius for rounded corners
text_line_height = 6.75; // Height of each line of text
text_line_spacing = 5; // Spacing between lines of text
text_lines = ["SecretReviewer", "Criterion"]; // Array containing the text lines

// Derived parameters
inner_width = width - 2 * border_thickness;
inner_height = height - 2 * border_thickness;
total_text_height = len(text_lines) * text_line_height + (len(text_lines) - 1) * text_line_spacing;

font_name = "Angkor";

// Function to create a rounded rectangle
module rounded_rectangle(w, h, r) {
    offset(r = r)
    square([w - 2 * r, h - 2 * r], center = true);
}

// Create the border by layering two rounded rectangles

difference() {
    linear_extrude(height = border_thickness, center = true)
    rounded_rectangle(width, height, radius); // Outer rectangle
    translate([0, 0, border_thickness+.5])
    linear_extrude(height = border_thickness * 2 , center = true)
    rounded_rectangle(inner_width-6, inner_height-4, 0); // Inner rectangle to be subtracted

scale([-1, 1, 1]) // Flipping the text
for(i = [0 : len(text_lines) - 1]) {
    translate([
        0, 
        (total_text_height / 3) - (i * (text_line_height + text_line_spacing)), 
        -2 
    ])
    linear_extrude(height = 2, center=true)
    text(text_lines[i], size = text_line_height, valign = "center", halign = "center", font = str(font_name));
}


}

// Place text lines in the middle of the rectangle
for(i = [0 : len(text_lines) - 1]) {
    translate([
        0, 
        (total_text_height / 3) - (i * (text_line_height + text_line_spacing)), 
        2
    ])
    linear_extrude(height = 1, center=true)
    text(text_lines[i], size = text_line_height, valign = "center", halign = "center", font = str(font_name));
}
