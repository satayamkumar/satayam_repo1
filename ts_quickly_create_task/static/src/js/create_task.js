/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class CreateTaskSystrayButton extends Component {
    static template = "ts_quickly_create_task.CreateTaskSystrayButton";

    setup() {
        this.action = useService("action");
    }

    onClick() {
        this.action.doAction({
            type: "ir.actions.act_window",
            view_mode: "form",
            res_model: "quick.task.wizard",
            views: [[false, "form"]],
            target: "new",
            context: {
                form_view_ref: "sh_task_time_adv.QuicklyTaskCreateTemplate",
            },
        });
    }
}

export const systrayItem = {
    Component: CreateTaskSystrayButton,
    isDisplayed: () => true,
};

registry.category("systray").add("CreateTaskSystrayButton", systrayItem, { sequence: 2 });

export default CreateTaskSystrayButton;




///** @odoo-module **/
//
//import { registry } from "@web/core/registry";
//import { Component } from "@odoo/owl";
//import { useService } from "@web/core/utils/hooks";
//
//class CreateTaskSystrayButton extends Component {
//    static template = "ts_quickly_create_task.CreateTaskSystrayButton";
//
//    setup() {
//        this.action = useService("action");
//    }
//
//    onClick() {
//        this.action.doAction({
//            type: "ir.actions.act_window",
//            view_mode: "form",
//            res_model: "quick.task.wizard",
//            views: [[false, "form"]],
//            target: "new",
//            context: {
//                form_view_ref: "sh_task_time_adv.QuicklyTaskCreateTemplate",
//            },
//        });
//    }
//}
//
//// Register in the systray category to appear in the header
//export const systrayItem = {
//    Component: CreateTaskSystrayButton,
//    isDisplayed: () => true,
//};
//
//registry.category("systray").add("CreateTaskSystrayButton", systrayItem, { sequence: 2 });
//
//export default CreateTaskSystrayButton;
//


///** @odoo-module **/
//
//import { Component } from "@odoo/owl";
//import { registry } from "@web/core/registry";
//import { useService } from "@web/core/utils/hooks";
//
//class CreateTaskButton extends Component {
//    static template = "ts_quickly_create_task.CreateTaskButton";
//
//    setup() {
//        this.action = useService("action");
//    }
//
//    onClick() {
//        this.action.doAction({
//            type: "ir.actions.act_window",
//            view_mode: "form",
//            res_model: "quick.task.wizard", // Open the wizard instead of project.task
//            views: [[false, "form"]],
//            target: "new", // Open as a popup modal
//        });
//    }
//}
//
//registry.category("main_components").add("CreateTaskButton", { Component: CreateTaskButton });
//export default CreateTaskButton;
//


///** @odoo-module **/
//
//import { Component } from "@odoo/owl";
//import { registry } from "@web/core/registry";
//import { useService } from "@web/core/utils/hooks";
//
//class CreateTaskButton extends Component {
//    static template = "ts_quickly_create_task.CreateTaskButton";
//
//    setup() {
//        this.action = useService("action");
//    }
//
//    onClick() {
//        this.action.doAction({
//            type: "ir.actions.act_window",
//            view_mode: "form",
//            res_model: "project.task",
//            views: [[false, "form"]],
//            target: "current",
//        });
//    }
//}
//
//registry.category("main_components").add("CreateTaskButton", { Component: CreateTaskButton });
//export default CreateTaskButton;
//










//odoo.define("quickly_create_task.QuicklyTaskCreateTemplate", function (require) {
//    var core = require("web.core");
//    var Widget = require("web.Widget");
//    var rpc = require("web.rpc");
//    var SystrayMenu = require("web.SystrayMenu");
//
//    var QuickTask = Widget.extend({
//        template: "QuicklyTaskCreateTemplate",
//
//        events: {
//            "click #task_start": "_create_task_start",
//        },
//
//        init: function () {
//            this._super.apply(this, arguments);
//            var self = this;
//            this._rpc({
//                model: "res.users",
//                method: "search_read",
//                fields: ["task_id"],
//            }).then(function (data) {
//                if (data) {
//                    _.each(data, function (user) {
//                        if (user.task_id) {
//                            self.$("#task_start").css("display", "none");
//                        } else {
//                            self.$("#task_start").css("display", "flex");
//                        }
//                    });
//                }
//            });
//        },
//
//        _create_task_start: function (e) {
//            e.preventDefault();
//            this.do_action({
//                type: "ir.actions.act_window",
//                view_type: "form",
//                view_mode: "form",
//                views: [[false, "form"]],
//                res_model: "quick.task.wizard",
//                target: "new",
//                context: {
//                    form_view_ref: "quickly_create_task.QuicklyTaskCreateTemplate",
//                },
//            });
//        },
//    });
//    QuickTask.prototype.sequence = 3;
//    SystrayMenu.Items.push(QuickTask);
//
//    //return quick_menu;
//    return {
//        QuickTask: QuickTask,
//    };
//});
