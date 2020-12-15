var alanBtnInstance = alanBtn({
    key: "8b6418beba0d6efb08f43260570725672e956eca572e1d8b807a3e2338fdd0dc/stage",
    onCommand: function (commandData) {
        if (commandData.command === "submit") {
            //call client code that will react on the received command
            submit();
        }
        else if (commandData.command === "fetch_results_neutral") {
            fetch_results_neutral();
        }
        else if (commandData.command === "fetch_results_positive") {
            fetch_results_positive();
        }
        else if (commandData.command === "fetch_results_negative") {
            fetch_results_negative();
        }
        else if (commandData.command === "play_video"){
            play_video();
        }
    },
    rootEl: document.getElementById("alan-btn"),
});
function submit() {
    document.getElementById("analyzeCommentsButton").click();
    console.log("Submitted");
}
function fetch_results_positive() {
    console.log("Feteched positive results")
}
function fetch_results_negative() {
    console.log("Feteched negative results")
}
function fetch_results_neutral() {
    console.log("Feteched neutral results")
}
function play_video() {
    jQuery(function ($) {
        $("#videoPlayer")[0].src += "?rel=0&autoplay=1";
        console.log($("#videoPlayer")[0].src)
    });
}
function validateForm() {
    document.getElementById("errorMessage").style.display = "none";
    var ytURL = document.forms["youtubeURLForm"].elements[0].value
    // console.log(ytURL)
    pattern = /https:\/\/www.youtube.com\/watch\?v=.{11}/
    // console.log(pattern.test(ytURL))
    if (ytURL == "") {
        document.getElementById("errorMessage").style.display = "block";
        // console.log("Invalid URL")
        return false;
    }        
    else if(pattern.test(ytURL) == false){
        document.getElementById("errorMessage").style.display = "block";
        // console.log("Invalid URL")
        return false;
    }
    else{
    document.getElementById("errorMessage").style.display = "none";
    return true;
    }
}