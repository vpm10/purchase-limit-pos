odoo.define('pos_purchase_limit.POSValidateOverride', function(require) {
    'use strict';
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const POSValidateOverride = PaymentScreen =>
        class extends PaymentScreen {
            async validateOrder(isForceValidate) {
                console.log(this)
                if (this.env.pos.selectedOrder.partner == null){
                this.showPopup('ErrorPopup', { title:'No Customer error', body: 'Please add Customer'
                });
                }else if (this.env.pos.selectedOrder.selected_paymentline.amount > this.env.pos.selectedOrder.partner.set_limit){
                console.log(this)
                this.showPopup('ErrorPopup', { title:'Exceeded limit', body:'Purchase Limit is:' + this.env.pos.selectedOrder.partner.set_limit
                });
                }
                else {
                await super.validateOrder(isForceValidate);
                }
                }
        };

    Registries.Component.extend(PaymentScreen, POSValidateOverride);

    return PaymentScreen;
});
