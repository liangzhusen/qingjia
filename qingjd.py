# -*- encoding: utf-8 -*-

from osv import osv, fields
class qingjia_qingjd(osv.osv):
    _name = 'qingjia.qingjd'
    _description = u'请假单'
    def get_employee(self, cr, uid, context={}):
        obj = self.pool.get('hr.employee')
        ids = obj.search(cr, uid, [('user_id','=',uid)])
        res = obj.read(cr, uid, ids, ['id','name'], context)
        return res and res[0]['id'] or 0

    _columns = {
        'shenqr': fields.many2one('hr.employee', u'申请人', required=True),
        'tians': fields.float(u'请假天数', required=True),
        'kaisrq': fields.date(u'开始日期', required=True),
        'shiyou': fields.text(u'请假事由'),
        'active': fields.boolean(u'有效'),
        'state': fields.selection([('draft',u'草稿'),('wait_prove',u'待批'),('proved',u'已批'),('rejected',u'被拒')], u'状态', required=True)
    }
    _defaults = {
        'shenqr': lambda self,cr,uid,context: self.get_employee(cr,uid,context),
        'active': lambda *a: 1,
        'state': lambda *a: 'draft',
    }
qingjia_qingjd()
