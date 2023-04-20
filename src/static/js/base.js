import addDragAndDropListeners from './drag_and_drop.js';

Date.prototype.toShortFormat = function () {
    const day = this.getDate();
    const month = this.getMonth() + 1;
    const year = this.getFullYear();

    return `${month.toString().padStart(2, '0')}/${day.toString().padStart(2, '0')}/${year}`;
}

window.onload = () => {
    addDragAndDropListeners();

    let newTaskBtn = document.getElementById('new-task-btn');
    newTaskBtn.onclick = () => {
        showNewTaskForm();
    };
    let closeFormBtn = document.getElementById('close-form-btn');
    closeFormBtn.onclick = () => {
        closeNewTaskForm();
    }

    const newTaskModal = document.getElementById('new-task-modal');
    const showNewTaskForm = () => {
        newTaskModal.classList.remove('hidden');
    };
    const closeNewTaskForm = () => {
        newTaskModal.classList.add('hidden');
    };

    async function deleteTask() {
        let parentElement = this.parentNode.parentNode;
        let taskId = parentElement.dataset.item;
        let csrfToken;
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${'csrftoken'}=`);
        if (parts.length === 2) csrfToken = parts.pop().split(';').shift();
        let headers = new Headers({
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        });
        await fetch(`api/board/tasks/${taskId}/`, {
            headers,
            method: 'DELETE',
            credentials: 'same-origin',
        });
        parentElement.remove()
    }

    let deleteTaskBtns = document.querySelectorAll('.delete-task');
    deleteTaskBtns.forEach((item) => {
        item.addEventListener('click', deleteTask);
    });

    let taskForm = document.getElementById('task-form');
    taskForm.onsubmit = async (event) => {
        event.preventDefault();
        let body = new FormData(event.target);
        let response = await fetch('/api/board/tasks/', {
            method: 'POST',
            body: body
        });
        let data = await response.json();
        closeNewTaskForm();
        event.target.reset();
        console.log(data);

        let column = document.getElementById(`column-${data.column}`);
        let taskList = column.querySelector('#tasks');
        taskList.innerHTML += `
        <div draggable="true" id="task-${data.id}" data-item="${data.id}"
             class="task p-2 bg-white border border-white rounded drop-shadow-sm cursor-grab">
            <h3 class="text-base">${data.name}</h3>
                <div class="flex flex-row justify-between">
                    <p class="text-xs text-gray-500">${new Date(data.created).toShortFormat()}</p>
                    <button class="delete-task cursor-pointer text-red-500">x</button>
                </div>
        </div>
    `;
        let deleteTaskBtns = document.querySelectorAll('.delete-task');
        deleteTaskBtns.forEach((item) => {
            item.addEventListener('click', deleteTask);
        });
        addDragAndDropListeners();
    };
};



