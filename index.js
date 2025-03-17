function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ noteID: noteId }), // Ensure it matches Flask's expected key
    }).then((_res) => {
        window.location.href = "/";
    });
}