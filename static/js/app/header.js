const initRequest = function(url) {

	var objSearchType, objAddress, objItemCategory, objVendorwithin;



	jQuery.support.cors = true;
	$("#divsearchresult").html("");

	function getResults() {
		$("#divsearchresult").html("");

		var APIurl = 'https://a827-donatenyc.nyc.gov/DonateNYCAPI'

		$.ajax({
				url: APIurl + '/api/users/SearchVendors?address=' + objAddress + '&buySellDonate=' + objSearchType + '&categoryID=' + objItemCategory + '&pickup=' + 'false' + '&radius=' + objVendorwithin + '&clLatitude=&clLongitude',
				type: 'GET',
				dataType: 'json',
				async: true,
				success: function(data) {
					console.log(data);
					var total;
					if (data) {
						total = data.length;
					}
					if (total > 0) {
						$.each(data, function(i, item) {
								var row = '<tr>'+
									'<th scope="row">'+ (i+1) +'</th>'+
									'<td>'+item.VendorName+'</td>'+
									'<td>'+ item.HouseNo+ ' '+item.Street +' ' + item.AptNo+ ' ' + item.Borough+ ' ' +item.Zip +'</td>'+
									'<td>'+item.PublicPhone+'</td>'+
								'</tr>'

								$('#divsearchresult').append(row);
							})
						}
						else {
							$('#divsearchresult').append("<div class='span12' style='margin: 3px 0px; width: 260px;'><b>No searches found</b></div>");
						}
					}
				});
		}

		function validateItems() {
		  var i = 0;
		  $(':checkbox:checked').each(function() {
		    i++;
		  });

		  if (i === 0) {
		    $(".divItemCategory input:checkbox:first").attr("class", "tooltipstered error");
		    $(".divItemCategory input:checkbox:first").attr("aria-invalid", true);
		    $(".divItemCategory input:checkbox:first").tooltipster('update', "Please select atleast one checkbox");
		    $(".divItemCategory input:checkbox:first").tooltipster('show');
		    return false;
		  } else {
		    $(".divItemCategory input:checkbox:first").attr("class", "tooltipstered");
		    $(".divItemCategory input:checkbox:first").removeAttr("aria-invalid");
		    return true;
		  }
		}

		$("#btnSearch").click(function() {
		  if ($('#txtAddress').val() == "") {
		    $('#txtAddress').tooltipster('show');
		  } else if (validateItems()) {

		    objAddress = $('#txtAddress').val();
		    objVendorwithin = $("#ddlDistance option:selected").val();
		    objSearchType = $("#ddlSearchType option:selected").val();
		    var ItemCategory = [];
		    $('.divItemCategory input:checked').each(function() {
		      ItemCategory.push(this.name);
		    });

		    objItemCategory = ItemCategory.toString();

		    localStorage.setItem('OnlyShowPickup', false);
		    localStorage.setItem('SearchAddress', $('#txtAddress').val());
		    localStorage.setItem('SearchRadius', $("#ddlDistance option:selected").val());
		    localStorage.setItem('SearchType', $("#ddlSearchType option:selected").val());
		    var divItemCategory = [];
		    $('.divItemCategory input:checked').each(function() {
		      divItemCategory.push(this.name);
		    });
		    localStorage.setItem('SearchFlag', '1');
		    localStorage.setItem("ItemCategory", divItemCategory.toString());

		    getResults();
		  }
		});


}
