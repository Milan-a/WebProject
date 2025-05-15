document.addEventListener('DOMContentLoaded', function() {
    const deleteLinks = document.querySelectorAll('.delete-link');
    deleteLinks.forEach(function(deleteLink) {
        deleteLink.addEventListener('click', function(event) {
            event.preventDefault();
            const itemType = this.dataset.itemType;
            const message = "Вы уверены, что хотите удалить " + itemType + "?\nПосле удаления, данные нельзя будет восстановить.";
            const confirmed = confirm(message);
            if (confirmed) {
                window.location.href = this.href;
            }
        });
    });
});