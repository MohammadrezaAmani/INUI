$('#switch-toggle-all [data-toggle-all]' ).click(function () {
  $( '#switch-toggle-all input[type="checkbox"]').prop('checked', this.checked)
})
