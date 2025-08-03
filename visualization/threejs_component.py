import streamlit.components.v1 as components


def render_threejs(probas):
    html_content = f"""
    <div id="viz" style="width: 100%; height: 500px;"></div>
    <script type="module">
    import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, 1.6, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth * 0.8, 500);
    document.getElementById('viz').appendChild(renderer.domElement);

    const geometry = new THREE.BoxGeometry();
    const material = new THREE.MeshBasicMaterial({{ color: 0x00ff00, wireframe: true }});
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    camera.position.z = 5;
    const animate = function () {{
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera);
    }};
    animate();
    </script>
    """
    components.html(html_content, height=500)
