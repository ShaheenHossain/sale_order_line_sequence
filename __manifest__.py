{
    "name": "Sale Order Line Number",
    "summary": "Propagates SO line number to invoices and stock picking.",
    "version": "12.0.1.0.0",
    "author": "Eagle ERP, "
              "Md. Shaheen Hossain, "
              "Eagle Group",
    "category": "Sales",
    "website": "https://eagle-erp.com",
    "license": "Open",
    'data': [
        'views/sale_view.xml',
        'views/report_saleorder.xml'
    ],
    "depends": [
        "sale",
    ],
    'post_init_hook': 'post_init_hook',
    "installable": True,
}
