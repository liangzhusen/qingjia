{
    "name": "Employee Leave Example",
    "author": "NewZN",
    "version": "0.2",
    "depends": ["base", "process", "hr"],
    "description": """《OpenERP应用和开发基础》代码模块开发示范例子greenbig修改。
    """,
    
     'data': [   
	'security/qingjia_security.xml',
        'security/ir.model.access.csv',
        'qingjia_view.xml',
        'qingjd_workflow.xml',
        'report/rpt_qingjd.xml',
        'qingjia_data.xml',
    ],
    "demo_xml": [],
    "installable": True,
}

