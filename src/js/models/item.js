var Item = Backbone.Model.extend({
	defaults: {
		name: "New Item",
		description: "To Be Written",
		quantity: 0,
		purchase_price: 0.00,
		sale_price: 0.00
	}
});

var Items = Backbone.Collection.extend({
	model: Item,
	url: '/items/'
});
