const grid = document.getElementById("grid");
const svg = document.getElementById("line-svg");
const wordList = ["CODE", "JAVA", "HTML", "CSS", "PYTHON"];
let cells = [];
let selectedCells = [];

function createGrid() {
    // Tempatkan kata-kata dalam grid
    let gridData = Array(8).fill().map(() => Array(8).fill(null)); // Grid 8x8 yang berisi null

    // Tempatkan setiap kata
    wordList.forEach(word => {
        placeWord(word, gridData);
    });

    // Isi grid dengan huruf acak untuk sel yang masih kosong
    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            if (!gridData[row][col]) {
                gridData[row][col] = String.fromCharCode(65 + Math.floor(Math.random() * 26));
            }
        }
    }

    // Buat elemen grid di DOM
    gridData.forEach((row, rowIndex) => {
        row.forEach((cell, colIndex) => {
            let divCell = document.createElement("div");
            divCell.classList.add("cell");
            divCell.textContent = cell;
            divCell.addEventListener("mousedown", startSelection);
            divCell.addEventListener("mouseenter", highlightSelection);
            divCell.addEventListener("mouseup", endSelection);
            grid.appendChild(divCell);
            cells.push(divCell);
        });
    });
}

function placeWord(word, gridData) {
    let placed = false;

    while (!placed) {
        // Pilih posisi acak untuk kata (baris, kolom, arah)
        let row = Math.floor(Math.random() * 8);
        let col = Math.floor(Math.random() * 8);
        let direction = Math.random() > 0.5 ? 'horizontal' : 'vertical'; // Arah horizontal atau vertikal

        // Cek apakah kata bisa ditempatkan
        if (canPlaceWord(word, row, col, direction, gridData)) {
            // Tempatkan kata
            for (let i = 0; i < word.length; i++) {
                if (direction === 'horizontal') {
                    gridData[row][col + i] = word[i];
                } else {
                    gridData[row + i][col] = word[i];
                }
            }
            placed = true; // Kata berhasil ditempatkan
        }
    }
}

function canPlaceWord(word, row, col, direction, gridData) {
    if (direction === 'horizontal') {
        if (col + word.length > 8) return false; // Pastikan kata tidak keluar dari grid
        for (let i = 0; i < word.length; i++) {
            if (gridData[row][col + i] !== null) return false; // Pastikan sel kosong
        }
    } else { // Vertikal
        if (row + word.length > 8) return false;
        for (let i = 0; i < word.length; i++) {
            if (gridData[row + i][col] !== null) return false;
        }
    }
    return true;
}


function startSelection(event) {
    selectedCells = [];
    event.target.classList.add("highlight");
    selectedCells.push(event.target);
    clearSVG();
}

function highlightSelection(event) {
    if (selectedCells.length) {
        event.target.classList.add("highlight");
        selectedCells.push(event.target);
        drawLine();
    }
}

function endSelection() {
    const selectedWord = selectedCells.map(cell => cell.textContent).join("");
    if (wordList.includes(selectedWord)) {
        alert("Found: " + selectedWord);
    } else {
        selectedCells.forEach(cell => cell.classList.remove("highlight"));
    }
    selectedCells = [];
    clearSVG();
}

function drawLine() {
    if (selectedCells.length < 2) return;

    clearSVG();

    const startCell = selectedCells[0].getBoundingClientRect();
    const endCell = selectedCells[selectedCells.length - 1].getBoundingClientRect();

    const startX = startCell.left + startCell.width / 2;
    const startY = startCell.top + startCell.height / 2;
    const endX = endCell.left + endCell.width / 2;
    const endY = endCell.top + endCell.height / 2;

    // Draw line
    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", startX);
    line.setAttribute("y1", startY);
    line.setAttribute("x2", endX);
    line.setAttribute("y2", endY);
    line.setAttribute("stroke", "blue");
    line.setAttribute("stroke-width", "3");
    line.setAttribute("stroke-linecap", "round");
    svg.appendChild(line);

    // Draw circle at end
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", endX);
    circle.setAttribute("cy", endY);
    circle.setAttribute("r", 5);
    circle.setAttribute("fill", "blue");
    svg.appendChild(circle);
}

function clearSVG() {
    while (svg.firstChild) {
        svg.removeChild(svg.firstChild);
    }
}

createGrid();
