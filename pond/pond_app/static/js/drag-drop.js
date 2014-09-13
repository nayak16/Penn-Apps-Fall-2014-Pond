if (window.FileReader) {
    var drop;
    var drop2;
    var fileNumber = 0;
    addEventHandler(window, 'load', function () {
        var status = document.getElementById('status');
        drop = document.getElementById('drop1');
        drop2 = document.getElementById('drop2');
        var list = document.getElementById('list');
        var list2 = document.getElementById('list2');


        function cancel(e) {
            if (e.preventDefault) {
                e.preventDefault();
            }
            return false;
        }

        // Tells the browser that we *can* drop on this target
        addEventHandler(drop, 'dragover', function (e) {
            e = e || window.event; // get window.event if e argument missing (in IE) 
            if (e.preventDefault) {
                e.preventDefault();
            }
            fileNumber = fileNumber + 1;
            status.innerHTML = fileNumber;
            $("#drop1").css("background-color", '#AA0000');

            return false;
        });
        // Tells the browser that we *can* drop on this target
        addEventHandler(drop, 'dragleave', function (e) {
            e = e || window.event; // get window.event if e argument missing (in IE) 
            if (e.preventDefault) {
                e.preventDefault();
            }
            fileNumber = fileNumber + 1;
            status.innerHTML = fileNumber;
            $("#drop1").css("background-color", '#FF0000');

            return false;
        });
        
        addEventHandler(drop, 'dragenter', cancel);
        addEventHandler(drop2, 'dragover', cancel);
        addEventHandler(drop2, 'dragenter', cancel);


        addEventHandler(drop, 'drop', function (e) {
            e = e || window.event; // get window.event if e argument missing (in IE)   
            if (e.preventDefault) {
                e.preventDefault();
            } // stops the browser from redirecting off to the image.

            var dt = e.dataTransfer;
            var files = dt.files;
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                var reader = new FileReader();

                //attach event handlers here...  
                reader.readAsDataURL(file);

                addEventHandler(reader, 'loadend', function (e, file) {
                    var bin = this.result;
                    var newFile = document.createElement('div');
                    newFile.innerHTML = 'Loaded : ' + file.name + ' size ' + file.size + ' B';
                    list.appendChild(newFile);
                    var fileNumber = list.getElementsByTagName('div').length;
                    status.innerHTML = fileNumber < files.length ? 'Loaded 100% of file ' + fileNumber + ' of ' + files.length + '...' : 'Done loading. processed ' + fileNumber + ' files.';

                    var img = document.createElement("img");
                    img.file = file;
                    img.src = bin;
                    list.appendChild(img);
                }.bindToEventHandler(file));
            }
            return false;
        });

        addEventHandler(drop2, 'drop', function (e) {
            e = e || window.event; // get window.event if e argument missing (in IE)   
            if (e.preventDefault) {
                e.preventDefault();
            } // stops the browser from redirecting off to the image.

            var dt = e.dataTransfer;
            var files = dt.files;
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                var reader = new FileReader();

                //attach event handlers here...  
                reader.readAsDataURL(file);

                addEventHandler(reader, 'loadend', function (e, file) {
                    var bin = this.result;
                    var newFile = document.createElement('div');
                    newFile.innerHTML = 'Loaded : ' + file.name + ' size ' + file.size + ' B';
                    list.appendChild(newFile);
                    var fileNumber = list.getElementsByTagName('div').length;
                    status.innerHTML = fileNumber < files.length ? 'Loaded2 100% of file ' + fileNumber + ' of ' + files.length + '...' : 'Done loading. processed ' + fileNumber + ' files.';

                    var img = document.createElement("img");
                    img.file = file;
                    img.src = bin;
                    list.appendChild(img);
                }.bindToEventHandler(file));
            }
            return true;
        });

        Function.prototype.bindToEventHandler = function bindToEventHandler() {
            var handler = this;
            var boundParameters = Array.prototype.slice.call(arguments);
            //create closure
            return function (e) {
                e = e || window.event; // get window.event if e argument missing (in IE)   
                boundParameters.unshift(e);
                handler.apply(this, boundParameters);
            }
        };
    });
} else {
    document.getElementById('status').innerHTML = 'Your browser does not support the HTML5 FileReader.';
}

function addFile(evt) {
    e = e || window.event; // get window.event if e argument missing (in IE)   
    if (e.preventDefault) {
        e.preventDefault();
    } // stops the browser from redirecting off to the image.

    var dt = e.dataTransfer;
    var files = dt.files;
    for (var i = 0; i < files.length; i++) {
        var file = files[i];
        var reader = new FileReader();

        //attach event handlers here...  
        reader.readAsDataURL(file);

        addEventHandler(reader, 'loadend', function (e, file) {
            var bin = this.result;
            var newFile = document.createElement('div');
            newFile.innerHTML = 'Loaded : ' + file.name + ' size ' + file.size + ' B';
            list.appendChild(newFile);
            var fileNumber = list.getElementsByTagName('div').length;
            status.innerHTML = fileNumber < files.length ? 'Loaded2 100% of file ' + fileNumber + ' of ' + files.length + '...' : 'Done loading. processed ' + fileNumber + ' files.';

            var img = document.createElement("img");
            img.file = file;
            img.src = bin;
            list.appendChild(img);
        }.bindToEventHandler(file));
    }
    return false;
}

//seperate event
function addEventHandler(obj, evt, handler) {
    if (obj.addEventListener) {
        // W3C method
        obj.addEventListener(evt, handler, false);
    } else if (obj.attachEvent) {
        // IE method.
        obj.attachEvent('on' + evt, handler);
    } else {
        // Old school method.
        obj['on' + evt] = handler;
    }
}