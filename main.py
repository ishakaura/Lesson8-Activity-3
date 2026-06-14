# CSS Animation Example

css_animation = """
@keyframes moveBox {
    from {
        left: 0px;
    }
    to {
        left: 200px;
    }
}

.box {
    position: relative;
    animation: moveBox 3s infinite;
}
"""

print(css_animation)