google.load('visualization', '1', {'packages':['annotatedtimeline']});
google.setOnLoadCallback(initialize);

var chart = null;
var data = null;
var query = null;
var base_url = 'http://'+window.location.hostname+':'+window.location.port;

google.load("visualization", "1", {packages:["annotatedtimeline"]});
google.setOnLoadCallback(initialize);


function initialize() {
    console.log(base_url);
    query = new google.visualization.Query(base_url+'/query?start=20-11-2009&stop=30-12-2009');
    query.send( handleResponse );
}

function init_with_date(range) 
{
//    range.start.setDate(range.start.getDate()-10); 
    var range = chart.getVisibleChartRange();
    var sy = range.start.getFullYear();
    var sm = range.start.getMonth();
    var sd = range.start.getDay();
    var ey = range.end.getFullYear();
    var em = range.end.getMonth();
    var ed = range.end.getDay();
    console.log('-----');
    console.log(range.start);
    console.log(range.end);
    console.log(sd+'-'+sm+'-'+sy);
    console.log(ed+'-'+em+'-'+ey);
     query = new google.visualization.Query(base_url+'/query?start=20-10-2009&stop=30-12-2009');
    query.send( handleResponse );

}


function readyChart() {
    console.log('ready');
    var range = chart.getVisibleChartRange();
    console.log(range.start);
    range.start.setDate(range.start.getDate()+10);
   chart.setVisibleChartRange(range.start, range.end);
}

function handleResponse(response) {
    if (!response.isError()) {
        if (data == null) {
            chart = new google.visualization.AnnotatedTimeLine(
                    document.getElementById("chart_div"));
            google.visualization.events.addListener(chart, "rangechange", init_with_date);
            google.visualization.events.addListener(chart, "ready", readyChart);
        }

        data = response.getDataTable();
        chart.draw(data, {title: 'Weight'});

    } 
    else {
        displayInfo("Error in query: " + response.getMessage() +
                    " " + response.getDetailedMessage());
    }
}

