function openDeleteConfirmationDialog($, event, modalId) {
    event.preventDefault();
    $(modalId).modal('show');
}

function deleteReservation($, modalId, formId) {
    $(formId).submit();
    $(modalId).modal('hide');
}

function cancelReservationDeletion($, modalId) {
    $(modalId).modal('hide');
}

module.exports = {
    openDeleteConfirmationDialog,
    deleteReservation,
    cancelReservationDeletion
};