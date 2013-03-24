# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1364121142.71421
_enable_loop = True
_template_filename = '/home/sunya7a/Hive/abstrackr-web/abstrackr/templates/accounts/dashboard.mako'
_template_uri = '/accounts/dashboard.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'../site.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n\n<script type="text/javascript" src="/scripts/jquery.alerts.js"></script>\n<link href="/scripts/jquery.alerts.css"  rel="stylesheet" type="text/css" media="screen" />\n\n<script language="javascript">\n\n    $(document).ready(function() { \n  \n\n        $("#export").dialog({\n            height: 500,\n            width:500, \n            modal: true,\n            autoOpen: false,\n            show: "blind",\n        });\n        \n        \n        \n    });\n</script>\n\n\n<div id="export" class="dialog">\n</div>\n\n\t\n')
        # SOURCE LINE 31
        if c.my_projects:
            # SOURCE LINE 32
            __M_writer(u'    <a class="tab" href = "')
            __M_writer(escape(url(controller='account', action='my_work')))
            __M_writer(u'">my work</a>\n    <a class="active_tab" href="')
            # SOURCE LINE 33
            __M_writer(escape(url(controller='account', action='my_projects')))
            __M_writer(u'">my projects</a>\n')
            # SOURCE LINE 34
        elif c.my_work:
            # SOURCE LINE 35
            __M_writer(u'    <a class="active_tab" href = "')
            __M_writer(escape(url(controller='account', action='my_work')))
            __M_writer(u'">my work</a>\n    <a class="tab" href="')
            # SOURCE LINE 36
            __M_writer(escape(url(controller='account', action='my_projects')))
            __M_writer(u'">my projects</a>\n')
        # SOURCE LINE 38
        __M_writer(u'<div class="content">\n\n<br/> \n')
        # SOURCE LINE 41
        if c.my_projects:
            # SOURCE LINE 42
            __M_writer(u'\n')
            # SOURCE LINE 43
            if len(c.leading_projects) > 0:
                # SOURCE LINE 44
                __M_writer(u'        <h1>projects you\'re leading</h1>\n        <center>\n\n        <br/>\n        <table class="list_table">\n        \n')
                # SOURCE LINE 50
                for i,review in enumerate(c.leading_projects):
                    # SOURCE LINE 51
                    __M_writer(u'        <tr class="')
                    __M_writer(escape('odd' if i%2 else 'even'))
                    __M_writer(u'">\n            <td><a href="')
                    # SOURCE LINE 52
                    __M_writer(escape(url(controller='review', action='show_review', id=review.id)))
                    __M_writer(u'">')
                    __M_writer(escape(review.name))
                    __M_writer(u'</td>           \n            <td class="inline-actions"><a href="')
                    # SOURCE LINE 53
                    __M_writer(escape(url(controller='review', action='admin', id=review.id)))
                    __M_writer(u'">admin \n                         <img src = "../../admin_sm.png"></a></td> \n            <td class="inline-actions">\n            <a href="#" onclick="javascript:    \n                      $(\'#export\').load(\'')
                    # SOURCE LINE 57
                    __M_writer(escape(url(controller="review", action="get_fields", review_id=review.id)))
                    __M_writer(u'\', \n                        function() {\n                            $(\'#export\').dialog(\'open\');\n                            $(\'#selectable\').selectable();\n                      });\n                      ">\n                      export<img src = "../../export_sm.png"></a></td>\n                    \n')
                    # SOURCE LINE 65
                    if c.statuses[review.id]:
                        # SOURCE LINE 66
                        __M_writer(u'                <td class="inline-actions"><a href="')
                        __M_writer(escape(url(controller='review', action='predictions_about_remaining_citations', id=review.id)))
                        __M_writer(u'">predictions\n                            <img src = "../../Robot-icon.png"></a></td>\n')
                        # SOURCE LINE 68
                    else:
                        # SOURCE LINE 69
                        __M_writer(u'                <td class="inline-actions"><i>no predictions yet</i></td>\n')
                    # SOURCE LINE 71
                    __M_writer(u'            \n            <td id="conflict_button_')
                    # SOURCE LINE 72
                    __M_writer(escape(review.id))
                    __M_writer(u'">loading...</td>\n            <script language="javascript">\n                $("#conflict_button_')
                    # SOURCE LINE 74
                    __M_writer(escape(review.id))
                    __M_writer(u'").load("/review/get_conflict_button_fragment/')
                    __M_writer(escape(review.id))
                    __M_writer(u'");\n            </script>\n            \n')
                    # SOURCE LINE 77
                    if c.do_we_have_a_maybe:
                        # SOURCE LINE 78
                        __M_writer(u'                <td class="inline-actions"><a href="')
                        __M_writer(escape(url(controller='review', action='review_maybes', id=review.id)))
                        __M_writer(u'">\n                    maybes<img src = "../../maybe_sm.png"></a></td>\n')
                        # SOURCE LINE 80
                    else:
                        # SOURCE LINE 81
                        __M_writer(u'                <td class="inline-actions"><i>no maybes yet</i></td>\n')
                    # SOURCE LINE 83
                    __M_writer(u'            \n            <td class="inline-actions">\n                <a href="#" onclick="javascript:jConfirm(\'are you sure you want to delete this review? all labels will be lost!\', \n                     \'delete review?\', function(r) {\n                        if(r) window.location = \'')
                    # SOURCE LINE 87
                    __M_writer(escape(url(controller='review', action='delete_review', id=review.id)))
                    __M_writer(u'\'; \n                   });">delete<img src = "../../delete.png"></a></td> \n        </tr>\n')
                # SOURCE LINE 91
                __M_writer(u'        </table>\n        <br/><br/><br/>\n        </center>\n')
            # SOURCE LINE 95
            __M_writer(u' \n')
            # SOURCE LINE 96
            if len(c.participating_projects) > 0:
                # SOURCE LINE 97
                __M_writer(u'        <h1>projects in which you\'re participating</h1>\n        <table class="list_table">\n')
                # SOURCE LINE 99
                for i,review in enumerate(c.participating_projects):
                    # SOURCE LINE 100
                    __M_writer(u'        <tr class="')
                    __M_writer(escape('odd' if i%2 else 'even'))
                    __M_writer(u'">\n            <td><a href="')
                    # SOURCE LINE 101
                    __M_writer(escape(url(controller='review', action='show_review', id=review.id)))
                    __M_writer(u'">')
                    __M_writer(escape(review.name))
                    __M_writer(u'</td>    \n            <td class="inline-actions"><a href="')
                    # SOURCE LINE 102
                    __M_writer(escape(url(controller='review', action='review_labels', review_id=review.id)))
                    __M_writer(u'">review my labels</td>  \n            <td class="inline-actions"><a href="')
                    # SOURCE LINE 103
                    __M_writer(escape(url(controller='review', action='leave_review', id=review.id)))
                    __M_writer(u'" \n                           onclick="javascript:return confirm(\'are you sure you want to leave this review?\')">\n            leave review</a></td>      \n        </tr>\n')
                # SOURCE LINE 108
                __M_writer(u'        </table>\n')
                # SOURCE LINE 109
            else:
                # SOURCE LINE 110
                if len(c.leading_projects) > 0:
                    # SOURCE LINE 111
                    __M_writer(u"            <h2>you're not participating in any projects yet (aside from those you're leading).</h2>\n")
                    # SOURCE LINE 112
                else:
                    # SOURCE LINE 113
                    __M_writer(u"            <h2>you're not participating in any projects yet.</h2>\n")
            # SOURCE LINE 116
            __M_writer(u'    <br/>\n    \n    <br/><br/>\n\n    <center>\n     <div class="actions">\n\n')
            # SOURCE LINE 123
            if len(c.leading_projects) > 1:
                # SOURCE LINE 124
                __M_writer(u'        <a href="')
                __M_writer(escape(url(controller='account', action='show_merge_review_screen')))
                __M_writer(u'"><img src ="../../merge_sm.png">merge reviews ...</a>\n')
            # SOURCE LINE 126
            __M_writer(u'    <a href="')
            __M_writer(escape(url(controller='review', action='create_new_review')))
            __M_writer(u'"><img src ="../../add.png">start a new project/review</a>\n    </center>    \n    </div>\n\n    \n')
            # SOURCE LINE 131
        elif c.my_work:
            # SOURCE LINE 132
            __M_writer(u'\n')
            # SOURCE LINE 133
            if len(c.outstanding_assignments) > 0:
                # SOURCE LINE 134
                __M_writer(u'        <h1>work you should be doing </h1>\n        <center>\n        <table class="list_table" align="center>>\n                <tr align="center">\n                <th width="25%">review</th><th >number to screen</th><th>screened so far</th><th width="20%">assigned</th><th width="10%">due</th><th width="30%">actions</th>\n                </tr>\n')
                # SOURCE LINE 140
                for i, assignment in enumerate(c.outstanding_assignments):
                    # SOURCE LINE 141
                    __M_writer(u'                    <tr>\n                    <td><a href="')
                    # SOURCE LINE 142
                    __M_writer(escape(url(controller='review', action='show_review', id=assignment.project_id)))
                    __M_writer(u'">\n                            ')
                    # SOURCE LINE 143
                    __M_writer(escape(c.review_ids_to_names_d[assignment.project_id]))
                    __M_writer(u'</td>          \n')
                    # SOURCE LINE 144
                    if not assignment.assignment_type == "perpetual":
                        # SOURCE LINE 145
                        __M_writer(u'                        <td>')
                        __M_writer(escape(assignment.num_assigned))
                        __M_writer(u'</td>\n')
                        # SOURCE LINE 146
                    else:
                        # SOURCE LINE 147
                        __M_writer(u'                        <td>--</td>\n')
                    # SOURCE LINE 149
                    __M_writer(u'                    \n                    <td>')
                    # SOURCE LINE 150
                    __M_writer(escape(assignment.done_so_far))
                    __M_writer(u'</td>\n                    <td>')
                    # SOURCE LINE 151
                    __M_writer(escape(assignment.date_assigned.month))
                    __M_writer(u'/')
                    __M_writer(escape(assignment.date_assigned.day))
                    __M_writer(u'/')
                    __M_writer(escape(assignment.date_assigned.year))
                    __M_writer(u'</td>\n')
                    # SOURCE LINE 152
                    if not assignment.assignment_type == "perpetual" and assignment.date_due is not None:
                        # SOURCE LINE 153
                        __M_writer(u'                        <td>')
                        __M_writer(escape(assignment.date_due.month))
                        __M_writer(u'/')
                        __M_writer(escape(assignment.date_due.day))
                        __M_writer(u'/')
                        __M_writer(escape(assignment.date_due.year))
                        __M_writer(u'</td>\n')
                        # SOURCE LINE 154
                    else:
                        # SOURCE LINE 155
                        __M_writer(u'                        <td>--</td>\n')
                    # SOURCE LINE 157
                    __M_writer(u'                    <td class="inline-actions">\n                    <a href="')
                    # SOURCE LINE 158
                    __M_writer(escape(url(controller='review', action='screen', review_id=assignment.project_id, assignment_id=assignment.id)))
                    __M_writer(u'">\n                    screen <img src="../../arrow_right.png"></img></a>\n                    <a href="')
                    # SOURCE LINE 160
                    __M_writer(escape(url(controller='review', action='review_labels', review_id=assignment.project_id, assignment_id=assignment.id)))
                    __M_writer(u'">review labels <img src="../../arrow_right.png"></a>\n                    </td>\n                    </tr>\n')
                # SOURCE LINE 164
                __M_writer(u'        </table>\n        </center>\n         <br/><br/>\n')
                # SOURCE LINE 167
            else:
                # SOURCE LINE 168
                __M_writer(u"        <h2>hurray, you've no outstanding assignments!</h2><br/><br/>\n")
            # SOURCE LINE 170
            __M_writer(u'    \n')
            # SOURCE LINE 171
            if len(c.finished_assignments) > 0:
                # SOURCE LINE 172
                __M_writer(u'        <h1>assignments you\'ve completed</h1>\n        <center>\n        <table width=80% class="list_table" align="center>>\n                <tr align="center">\n<th width="25%">review</th><th >number to screen</th><th>screened so far</th><th width="20%">assigned</th><th width="10%">due</th><th width="30%">actions</th>\n                </tr>\n')
                # SOURCE LINE 178
                for i,assignment in enumerate(c.finished_assignments):
                    # SOURCE LINE 179
                    __M_writer(u'                    <tr>\n                    <td><a href="')
                    # SOURCE LINE 180
                    __M_writer(escape(url(controller='review', action='show_review', id=assignment.project_id)))
                    __M_writer(u'">\n                            ')
                    # SOURCE LINE 181
                    __M_writer(escape(c.review_ids_to_names_d[assignment.project_id]))
                    __M_writer(u'</td>          \n')
                    # SOURCE LINE 182
                    if not assignment.assignment_type == "perpetual":
                        # SOURCE LINE 183
                        __M_writer(u'                        <td>')
                        __M_writer(escape(assignment.num_assigned))
                        __M_writer(u'</td>\n')
                        # SOURCE LINE 184
                    else:
                        # SOURCE LINE 185
                        __M_writer(u'                        <td>--</td>\n')
                    # SOURCE LINE 187
                    __M_writer(u'                    <td>')
                    __M_writer(escape(assignment.done_so_far))
                    __M_writer(u'</td>\n                    <td>')
                    # SOURCE LINE 188
                    __M_writer(escape(assignment.date_assigned.month))
                    __M_writer(u'/')
                    __M_writer(escape(assignment.date_assigned.day))
                    __M_writer(u'/')
                    __M_writer(escape(assignment.date_assigned.year))
                    __M_writer(u'</td>\n')
                    # SOURCE LINE 189
                    if not assignment.assignment_type == "perpetual" and assignment.date_due is not None:
                        # SOURCE LINE 190
                        __M_writer(u'                        <td>')
                        __M_writer(escape(assignment.date_due.month))
                        __M_writer(u'/')
                        __M_writer(escape(assignment.date_due.day))
                        __M_writer(u'/')
                        __M_writer(escape(assignment.date_due.year))
                        __M_writer(u'</td>\n')
                        # SOURCE LINE 191
                    else:
                        # SOURCE LINE 192
                        __M_writer(u'                        <td>--</td>\n')
                    # SOURCE LINE 194
                    __M_writer(u'                        <td class="inline-actions">\n                                      <a href="')
                    # SOURCE LINE 195
                    __M_writer(escape(url(controller='review', action='review_labels', review_id=assignment.project_id, assignment_id=assignment.id)))
                    __M_writer(u'">review labels <img src="../../arrow_right.png"></a>\n                        </td>\n                    </td>\n                    </tr>\n')
                # SOURCE LINE 200
                __M_writer(u'        </table>\n        </center>\n')
        # SOURCE LINE 204
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'home')
        return ''
    finally:
        context.caller_stack._pop_frame()

