
from system.core.router import routes

routes['default_controller'] = 'Dashboards'
routes['GET']['/'] = 'Dashboards#index'
routes['GET']['/register'] = 'Dashboards#register'
routes['POST']['/register/process'] = 'Dashboards#new'
routes['GET']['/signin'] = 'Dashboards#signin'
routes['POST']['/signin/validate'] = 'Dashboards#validate_login'
routes['GET']['/dashboard'] = 'Dashboards#dashboard'
routes['GET']['/logout'] = 'Dashboards#logout'
routes['GET']['/users/<int:id>/destroy'] = 'Dashboards#destroy'
routes['GET']['/users/<int:id>/edit'] = 'Dashboards#edit'
routes['POST']['/users/<int:id>/update'] = 'Dashboards#update'
routes['GET']['/users//edit'] = 'Dashboards#nocango'
routes['POST']['/users/<int:id>/update/description'] = 'Dashboards#update_description'
routes['POST']['/users/<int:id>/update/password'] = 'Dashboards#update_password'
routes['GET']['/users/admin_create'] = 'Dashboards#admin_create'
routes['POST']['/users/register/admin_create'] = 'Dashboards#admin_new'
