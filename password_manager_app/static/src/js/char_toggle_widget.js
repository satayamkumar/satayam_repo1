/** @odoo-module **/
import { registry } from "@web/core/registry";
import { CharField } from "@web/views/fields/char/char_field";
import { useRef } from "@odoo/owl";

export class CharTogglePassword extends CharField {
    setup() {
        super.setup();
        this.inputRef = useRef("input");
        this.state = { showPassword: false };
    }

    togglePasswordVisibility() {
        this.state.showPassword = !this.state.showPassword;
        this.render();
    }

    get showPassword() {
        return this.state.showPassword;
    }

    get inputType() {
        // Always start with password type (dots) by default
        return this.state.showPassword ? "text" : "password";
    }

    get displayValue() {
        // Show dots when password is hidden, actual value when shown
        if (!this.state.showPassword && this.props.value) {
            return "•".repeat(Math.min(this.props.value.length, 8)); // Show up to 8 dots
        }
        return this.props.value || "";
    }

    get shouldShowToggle() {
        // Always show toggle button for password fields
        return true;
    }

    onInput(ev) {
        // Handle input changes
        const value = ev.target.value;
        if (this.state.showPassword) {
            // If showing password, update normally
            this.props.update(value);
        } else {
            // If showing dots, don't update the actual value
            // The user should click the toggle button to edit
            return;
        }
    }
}

CharTogglePassword.template = "password_manager_app.CharTogglePassword";

registry.category("fields").add("char_toggle", CharTogglePassword);
