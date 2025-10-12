// --- Helper: make unique key for coordinates (x, y)
function getKey(x, y) {
  return `${x},${y}`;
}

// --- Main solver function ---
function solve(commands, target) {
  // Step 1: Sort commands by existing cube, then new cube
  commands.sort((a, b) => a.existing - b.existing || a.newCube - b.newCube);

  // Step 2: Maps to store cube placements
  const positions = new Map(); // cube → {x, y}
  const grid = new Map();      // "x,y" → cube

  // Step 3: Define movement for directions
  const dirDelta = {
    U: [0, 1], UP: [0, 1],
    D: [0, -1], DOWN: [0, -1],
    L: [-1, 0], LEFT: [-1, 0],
    R: [1, 0], RIGHT: [1, 0]
  };

  // Step 4: Helper function to place cube if not placed already
  function ensurePlaced(cube) {
    if (positions.has(cube)) return; // already placed
    let x = 0, y = 0;
    while (grid.has(getKey(x, y))) { // find a free spot
      x++;
      if (x > 50) { x = 0; y++; }
    }
    positions.set(cube, { x, y });
    grid.set(getKey(x, y), cube);
  }

  // Step 5: Process each command
  for (const cmd of commands) {
    const ex = cmd.existing;
    const nw = cmd.newCube;
    const dir = cmd.dir.toUpperCase();

    ensurePlaced(ex); // make sure existing cube has position
    const posEx = positions.get(ex);

    const delta = dirDelta[dir] || dirDelta[dir[0]];
    if (!delta) throw new Error("Invalid direction: " + dir);

    const nx = posEx.x + delta[0];
    const ny = posEx.y + delta[1];
    const key = getKey(nx, ny);

    // Remove new cube from its old place if already placed
    if (positions.has(nw)) {
      const old = positions.get(nw);
      grid.delete(getKey(old.x, old.y));
      positions.delete(nw);
    }

    // Replace any cube that already exists at target position
    if (grid.has(key)) {
      const oldCube = grid.get(key);
      positions.delete(oldCube);
      grid.delete(key);
    }

    // Place new cube
    positions.set(nw, { x: nx, y: ny });
    grid.set(key, nw);
  }

  // Step 6: Get target cube position
  if (!positions.has(target)) return [-1, -1, -1, -1];
  const p = positions.get(target);

  // Step 7: Get neighbours (Up, Down, Left, Right)
  const up = grid.get(getKey(p.x, p.y + 1)) || -1;
  const down = grid.get(getKey(p.x, p.y - 1)) || -1;
  const left = grid.get(getKey(p.x - 1, p.y)) || -1;
  const right = grid.get(getKey(p.x + 1, p.y)) || -1;

  return [up, down, left, right];
}

// --- Example Input ---
const commands = [
  { existing: 1, newCube: 2, dir: 'R' }, // cube 2 → right of cube 1
  { existing: 2, newCube: 3, dir: 'U' }, // cube 3 → up of cube 2
  { existing: 1, newCube: 4, dir: 'U' }  // cube 4 → up of cube 1
];

const target = 2;

// --- Run ---
const result = solve(commands, target);
console.log(result.join(' ')); // Output: 3 -1 1 -1
