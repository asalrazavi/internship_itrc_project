$(function () {
  /* On Add/Change forms, use value of 'Custom Permissions' checkbox to hide/show
     widgets for selecting Groups and Users that should be assigned 'can_work_on'
     permissions for the model instance being added/changed */
  if (!$('#id_is_majority_voting').is(':checked')) {
    $('div.majority_count').hide();
  }
  $('#id_is_majority_voting').change(function() {
    $('div.majority_count').toggle();
  });
  if (!$('#id_custom_permissions').is(':checked')) {
    $('div.field-can_work_on_groups').hide();
    $('div.field-can_work_on_users').hide();
  }
  $('#id_custom_permissions').change(function() {
    $('div.field-can_work_on_groups').toggle();
    $('div.field-can_work_on_users').toggle();
  });
});

$(document).ready(function() {
    $('#project_analytics_information-group .add-row').click(function() {
        // Clone the last formset and change its IDs to make it unique
        var lastFormset = $('.project_analytics_information-group .form-row:last');
        var newFormset = lastFormset.clone();

        // Update IDs to be unique
        var formsetIndex = $('.project_analytics_information-group .form-row').length;
        newFormset.find(':input').each(function(){
            var name = $(this).attr('name').replace('-' + (formsetIndex - 1) + '-' + formsetIndex + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        });

        // Append the new formset to the group
        lastFormset.after(newFormset);
    });
});