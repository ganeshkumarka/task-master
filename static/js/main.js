// function editTask(taskId) {
//     fetch(`/get_task/${taskId}`)
//         .then(response => response.json())
//         .then(task => {
//             document.getElementById('editContent').value = task.content;
//             document.getElementById('editCategory').value = task.category;
//             document.getElementById('editDueDate').value = task.due_date || '';
//             document.getElementById('editStatus').value = task.status;
//             document.getElementById('editForm').action = `/update_task/${taskId}`;
//             document.getElementById('editModal').classList.remove('hidden');
//         });
// }

function editTask(button) {
    var taskId = button.getAttribute('data-task-id');
    // do something with the task ID
    fetch(`/get_task/${taskId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(task => {
            console.log('Received task:', task);  // For debugging
            document.getElementById('editContent').value = task.content;
            document.getElementById('editCategory').value = task.category;
            document.getElementById('editDueDate').value = task.due_date || '';
            document.getElementById('editStatus').value = task.status;
            document.getElementById('editForm').action = `/update_task/${taskId}`;
            document.getElementById('editModal').classList.remove('hidden');
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while fetching the task data.');
        });
} 
// function editTask(taskId) {
//     fetch(`/get_task/${taskId}`)
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             return response.json();
//         })
//         .then(task => {
//             console.log('Received task:', task);  // For debugging
//             document.getElementById('editContent').value = task.content;
//             document.getElementById('editCategory').value = task.category;
//             document.getElementById('editDueDate').value = task.due_date || '';
//             document.getElementById('editStatus').value = task.status;
//             document.getElementById('editForm').action = `/update_task/${taskId}`;
//             document.getElementById('editModal').classList.remove('hidden');
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             alert('An error occurred while fetching the task data.');
//         });
// }
function closeModal() {
    document.getElementById('editModal').classList.add('hidden');
}

// Close modal when clicking outside
window.onclick = function(event) {
    let modal = document.getElementById('editModal');
    if (event.target == modal) {
        closeModal();
    }
}