from django.urls import path

from . import views
app_name="myapp"
urlpatterns = [
    path('homepage/',views.homepage),
    path('get_provider_name/<nid>',views.get_provider_name),
    path('adm_add_charge/',views.adm_add_charge_profile),
    path('adm_add_charge_profile_post/',views.adm_add_charge_profile_post),
    path('adm_add_employee_area/',views.adm_add_employee_area),
    path('adm_add_employee_area_post/',views.adm_add_employee_area_post),
    path('adm_add_media_provider/',views.adm_add_media_provider),
    path('adm_add_media_provider_post/', views.adm_add_media_provider_post),
    path('adm_media_type/',views.adm_media_type),
    path('adm_media_type_post/',views.adm_media_type_post),
    path('adm_service_area/',views.adm_service_area),
    path('adm_service_area_post/',views.adm_service_area_post),
    path('adm_add_staff/',views.adm_add_staff),
    path('adm_add_staff_post/',views.adm_add_staff_post),
    path('adm_sent_reply_to_complaint/<str:id>',views.adm_sent_reply_to_complaint),
    path('adm_sent_reply_to_complaint_post/',views.adm_sent_reply_to_complaint_post),
    path('adm_view_complaint/',views.adm_view_complaint),
    path('adm_view_complaint_post/',views.adm_view_complaint_post),
    path('adm_view_expense/',views.adm_view_expense_mngt),
    path('adm_view_expense_post/',views.adm_view_expense_mngt_post),
    path('adm_view_installation/',views.adm_view_installation),
    path('adm_view_installation_post/',views.adm_view_installation_post),
    path('adm_view_maintance/',views.adm_view_maintance),
    path('adm_view_maintance_post/',views.adm_view_maintance_post),
    path('adm_view_new_request_more/<str:pk>',views.adm_view_new_request_more),
    path('adm_view_new_request_more_post/',views.adm_view_new_request_more_post),
    path('adm_view_new_request/',views.adm_view_new_request),
    path('adm_view_new_request_post/',views.adm_view_new_request_post),
    path('adm_view_created_media/',views.adm_view_created_media),
    path('adm_view_created_media_post/',views.adm_view_created_media_post),
    path('adm_view_media_more/<str:pk>',views.adm_view_media_more),
    path('adm_view_media_more_post/',views.adm_view_media_more_post),
    path('adm_view_registered_user/',views.adm_view_registered_user),
    path('adm_view_registered_user_post/',views.adm_view_registered_user_post),
    path('adm_view_rejected_request_more/<str:pk>',views.adm_view_rejected_request_more),
    path('adm_view_rejected_request/',views.adm_view_rejected_request),
    path('adm_view_rejected_request_post/',views.adm_view_rejected_request_post),
    path('adm_allocated_designer/',views.adm_allocate_to_designer),
    path('adm_edit_charge_profile/<str:pk>',views.adm_edit_charge_profile),
    path('adm_edit_charge_profile_post/',views.adm_edit_charge_profile_post),
    path('adm_edit_employee_area/<str:pk>',views.adm_edit_employee_area),
    path('adm_edit_employee_area_post/',views.adm_edit_employee_area_post),
    path('adm_edit_media_provider/<str:pk>',views.adm_edit_media_provider),
    path('adm_edit_media_provider_post/',views.adm_edit_media_provider_post),
    path('adm_edit_media_type/<str:pk>',views.adm_edit_media_type),
    path('adm_edit_media_type_post/',views.adm_edit_media_type_post),
    path('adm_edit_service_area/<str:pk>',views.adm_edit_service_area),
    path('adm_edit_service_area_post/',views.adm_edit_service_area_post),
    path('adm_edit_staff/<str:pk>',views.adm_edit_staff),
    path('adm_edit_staff_post/',views.adm_edit_staff_post),
    path('adm_login/',views.adm_login),
    path('adm_login_post/',views.adm_login_post),
    path('adm_monthly_settlement/',views.adm_monthly_settlement_entry),
    path('adm_monthly_settlement_post/', views.adm_monthly_settlement_entry_post),
    path('adm_view_advertisement_request_approve/',views.adm_view_advertisement_request_approve),
    path('adm_view_advertisement_request_approve_post/',views.adm_view_advertisement_request_approve_post),
    path('adm_view_advertisement_request_approve_more/<str:pk>',views.adm_view_advertisement_request_approved_more),
    path('adm_view_advertisement_request_approve_more_post/',views.adm_view_advertisement_request_approved_more_post),
    path('adm_view_charge_profile/',views.adm_view_charge_profile),
    path('adm_view_charge_profile_post/',views.adm_view_charge_profile_post),
    path('adm_view_charge_profile_del/<str:pk>',views.adm_view_charge_profile_del),
    path('adm_view_employee_area/',views.adm_view_employee_area),
    path('adm_view_employee_area_post/', views.adm_view_employee_area_post),
    path('adm_view_employee_area_del/<str:pk>', views.adm_view_employee_area_del),
    path('adm_view_rejected_request/',views.adm_view_rejected_request),
    path('adm_view_service_area_post/',views.adm_view_service_area_post),

    path('adm_view_feedback/',views.adm_view_feedback_reviews),
    path('adm_view_feedback_post/',views.adm_view_feedback_reviews_post),
    path('adm_view_media_provider/',views.adm_view_media_provider),
    path('adm_view_media_provider_del/<str:pk>',views.adm_view_media_provider_del),
    path('adm_view_media_provider_post/',views.adm_view_media_provider_post),
    path('adm_view_media_type/',views.adm_view_media_type),
    path('adm_view_media_type_del/<str:pk>',views.adm_view_media_type_del),
    path('adm_view_media_type_post/',views.adm_view_media_type_post),
    path('adm_view_monthly_settlement/',views.adm_view_monthy_settlement_entry),
    path('adm_view_monthly_settlement_post/',views.adm_view_monthy_settlement_entry_post),
    path('adm_view_registered_user_more/',views.adm_view_registered_user_more),
    path('adm_request_from_public_for_media_provider/',views.adm_request_from_public_for_media_provider),
    path('adm_request_from_public_for_media_provider_post/',views.adm_request_from_public_for_media_provider_post),
    path('adm_view_request_from_public/<str:pk>',views.adm_request_from_public),
    path('adm_view_service_area/',views.adm_view_service_area),
    path('adm_view_service_area_del/<str:pk>',views.adm_view_service_area_del),
    path('adm_view_staff/',views.adm_view_staff),
    path('adm_view_staff_del/<str:pk>',views.adm_view_staff_del),
    path('adm_view_staff_post/',views.adm_view_staff_post),
    path('adm_homepage/',views.adm_homepage),

    path('admin_index/',views.admin_index),


    path('designer_index/',views.designer_index),
    path('dsgnr_homepage/',views.dsgnr_homepage),
    path('dsgnr_edit_media/<str:pk>/<str:id2>',views.dsgnr_edit_create_media),
    path('dsgnr_edit_media_post/',views.dsgnr_edit_create_media_post),
    path('dsgnr_edit_profile/',views.dsgnr_edit_profile),
    path('dsgnr_edit_profile_post/',views.dsgnr_edit_profile_post),
    path('dsgnr_upload_media/',views.dsgnr_upload_media),
    path('dsgnr_upload_media_post/<str:id>',views.dsgnr_upload_media_post),
    path("desi_up_med_post2/",views.upload_media22),
    path('dsgnr_view_media/',views.dsgnr_view_media_uploaded),
    path('dsgnr_view_media_post/',views.dsgnr_view_media_uploaded_post),
    # path('dsgnr_view_media_del/<str:pk>',views.dsgnr_view_media_uploaded_del),
    path('dsgnr_view_profile/',views.dsgnr_view_profile),
    path('dsgnr_view_request_assigned/',views.dsgnr_view_request_assigned),
    path('dsgnr_view_request_post/',views.dsgnr_view_request_post),
    path('dsgnr_view_request_assigned_post/<str:id>',views.dsgnr_view_request_assigned_post),

    path('public_homepage/',views.public_homepage),
    path('public_public_to_admin/',views.public_to_admin),
    path('public_public_to_admin_post/',views.public_to_admin_post),
    path('public_view_charge_profile/',views.public_view_charge_profile),
    path('public_view_media_provider/',views.public_view_media_provider),
    path('public_view_media_types/',views.public_view_media_types),
    path('public_index/',views.public_index),
    # path('public_af/',views.public_af),

    path('semp_index/',views.semp_index),
    path('semp_homepage/',views.semp_homepage),
    path('semp_view_maintance/',views.semp_view_maintance),
    path('semp_view_maintance_post/',views.semp_view_maintance_post),
    path('semp_view_maintance_del/<str:pk>',views.semp_view_maintance_del),
    path('semp_edit_profile/',views.semp_edit_profile),
    path('semp_edit_profile_post/',views.semp_edit_profile_post),
    path('semp_expense_mngt/',views.semp_expense_mngt),
    path('semp_expense_mngt_post/',views.semp_expense_mngt_post),
    path('semp_installation/',views.semp_installation,name="semp_installation"),
    path('semp_installation_post/',views.semp_installation_post),
    path('semp_maintance/',views.semp_maintance,name='semp_maintance'),
    path('semp_maintance_post/',views.semp_maintance_post),
    path('semp_view_expense/',views.semp_view_expense),
    path('semp_view_expense_post/',views.semp_view_expense_post),
    path('semp_view_installation/',views.semp_view_installation),
    path('semp_view_installation_post/',views.semp_view_installation_post),
    path('semp_view_installation_del/<str:pk>',views.semp_view_installation_del),
    path('semp_view_profile/',views.semp_view_profile),
    path('semp_view_service_area/',views.semp_view_service_area),
    path('semp_view_service_area_post/',views.semp_view_service_area_post),



    path('and_user_login/',views.and_user_login),
    path('and_user_signup/',views.and_user_signup),
    path('and_user_view_service_area/',views.and_user_view_service_area),
    path('and_user_view_media_type/',views.and_user_view_media_type),
    path('and_user_view_media_provider/',views.and_user_view_media_provider),
    path('and_user_view_charge_profile/',views.and_user_view_charge_profile),
    path('and_user_change_password/',views.and_user_change_password),
    path('and_user_send_complaint/',views.and_user_send_complaint),
    path('and_user_view_complaint/',views.and_user_view_complaint),
    path('and_user_send_feedback/', views.and_user_send_feedback),
    path('and_user_view_feedback/',views.and_user_view_feedback),
    path('and_user_view_profile/',views.and_user_view_profile),
    path('and_user_update_profile/',views.and_user_update_profile),
    path('and_user_send_enquiry_adrequest/',views.and_user_send_enquiry_adrequest),
    path('and_user_view_enquiry_adrequest/',views.and_user_view_enquiry_adrequest),
    path('and_user_view_enquiry_adrequest_del/',views.and_user_view_enquiry_adrequest_del),







]
