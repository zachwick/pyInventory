var AppView = Backbone.View.extend({
	el: "#app-container",
	template: function() {
		return _.template($("#app-template").html());
	},
	events: {
		'submit #add-item-form': 'newItem'
	},
	initialize: function(options) {
		this.items = new Items();
		this.listenTo(this.items, 'all', this.render);

		this.render();
		this.items.fetch();
	},
	addOne: function(item) {
		var view = new ItemView({ model: item });
		this.$("#item-list").append(view.render().el);
	},
	addAll: function() {
		this.items.each(this.addOne, this);
	},
	newItem: function(e) {
		e.stopPropagation();
		e.preventDefault();
		var newItem = new Item({
			name: this.$("input[name='name']").val(),
			description: this.$("input[name='description']").val(),
			location: this.$("input[name='location']").val(),
			quantity: this.$("input[name='quantity']").val(),
			purchase_price: this.$("input[name='purchase_price']").val(),
			sale_price: this.$("input[name='sale_price']").val()
		});
		newItem.save();
		//this.items.add(newItem).save();
	},
	render: function() {
		this.$el.html(this.template());
		this.addAll();
	}
});
