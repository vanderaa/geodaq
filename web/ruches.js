$(document).ready(function () {

setChartRange(3);
jQuery('#chart_timerange li').click( 
			function(e) {
					var o = jQuery(this);
					var r = o.index();
					o.addClass('active').siblings().removeClass('active');
					//var r = o.attr('range');
					console.log(r);
					setChartRange(r);
					}
			);


function setChartRange(r) 
{
	//var chart = document.getElementById('pricechart');
	var chart = $("#pricechart")
	//chart.parent().attr('href');
	//var link = chart.parent();
	console.log(chart.parent().attr('href'));
	//$.get(ChartBaseURL + "_" + r + ".svg", function(data){ console.log(data); });
	var td;
	switch(r)
	{
		case 0:
			td = "1y";
			break;
		case 1:
			td = "1m";
			break;
		case 2:
			td = "1w";
			break;
		case 3:
			td = "1d";
			break;
	}
	console.log(td);
	var ChartBaseURL = "img/plot";
	var oo = ChartBaseURL + "_" + td + ".svg";
					//chart.src = oo;
	chart.parent().attr('href',oo);
	chart.load(oo);
	//$("#pricechart").load(oo);
	console.log(oo);
	
	//var e = jQuery('#chart_timerange').children('li[range="' + r + '"]').addClass('active').siblings().removeClass('active');
					//	jQuery.cookie('chart_timerange', r);
}

		//var r = jQuery.cookie('chart_timerange');
		//if (!r) r = 60;
		//setChartRange(r);
});
