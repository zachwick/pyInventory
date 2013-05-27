var ItemView = Backbone.View.extend({
	tagName: "tr",
	template: function() {
		return _.template($("#item-template").html());
	},
	events: {
		'click .delete':'deleteSelf',
		'click .edit':'toggleEditingState'
	},
	deleteSelf: function(e) {
		e.stopPropagation();
		e.preventDefault();
		this.model.destroy();
	},
	toggleEditingState: function(e) {

	},
	initialize: function() {
		this.listenTo(this.model, "change", this.render);
		this.listenTo(this.model, "destroy", this.remove);
	},
	render: function() {
		this.$el.html(this.template()(this.model.toJSON()));
		return this;
	}
});
