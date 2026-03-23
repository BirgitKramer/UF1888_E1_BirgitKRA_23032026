<odoo>
    <record id="view_partner_form_inherit_nivel_cliente" model="ir.vi.view">
        <field name="name">res.partner.form.nivel.cliente</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_form"/>
        <field name="arch" type="xml"/>
            <xpath expr="//field[@name='category_id']" position "after"
                <field name="nivel_cliente"/>
            <xpath>
        <field>
    </record>
</odoo>                
