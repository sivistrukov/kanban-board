function onDragStart(event) {
    event.dataTransfer.setData('dragItem', this.dataset.item);
    this.classList.remove('bg-white', 'border-white');
    this.classList.add('opacity-60', 'bg-gray-300', 'border-gray-300');
}

function onDragOver(event) {
    event.preventDefault();
}

function onDragEnter(event) {
    event.preventDefault();
}

function onDragLeave(event) {
}

function onDragEnd(event) {
    this.classList.add('bg-white', 'border-white');
    this.classList.remove('opacity-60', 'bg-gray-300', 'border-gray-300');
}

async function onDrop(event) {
    event.preventDefault();
    event.stopPropagation();
    const dragId = event.dataTransfer.getData('dragItem');
    const draggable = document.getElementById(`task-${dragId}`);
    this.appendChild(draggable);

    let csrfToken;
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${'csrftoken'}=`);
    if (parts.length === 2) csrfToken = parts.pop().split(';').shift();

    let headers = new Headers({
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
    })
    await fetch(`api/board/tasks/${dragId}/`, {
        method: 'PATCH',
        headers,
        body: JSON.stringify({
            column: this.dataset.id,
        }),
        credentials: 'same-origin',
    });
}

function addDragAndDropListeners() {
    let dropAreas = document.querySelectorAll('#tasks');
    dropAreas.forEach((item) => {
        item.addEventListener('dragenter', onDragEnter);
        item.addEventListener('dragleave', onDragLeave);
        item.addEventListener('dragover', onDragOver);
        item.addEventListener('drop', onDrop);
    });

    let items = document.querySelectorAll('.task');
    items.forEach((item) => {
        item.addEventListener('dragstart', onDragStart);
        item.addEventListener('dragend', onDragEnd);
    });
}

export default addDragAndDropListeners;