function getNearbyFiles() {
	$.ajax({
		method: "GET",
		url: "/nearby",
		success: function(json) {
			for (var i = 0; i < json.length; i++) {
				var file = json[i];
				var id = file.id;
				var filename = file.filename;
				var author = file.author;
				var isProtected = file.isProtected;


				var button = document.createElement("input");
				button.type = "button";
				$(button).click(function() {
					// Download the file
				});
			}
		}
	})
}