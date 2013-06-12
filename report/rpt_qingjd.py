

import time
from report import report_sxw
from osv import osv

class rpt_qingjd(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(rpt_qingjd, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'time': time,
        })
report_sxw.report_sxw('report.qingjia.rpt_qingjd','qingjia.qingjd','addons/qingjia/report/rpt_qingjd.rml',parser=rpt_qingjd,header=False)


