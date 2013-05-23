var items = new Items();
items.fetch({
	success: function(collection, response, options) {
		collection.each(function(item) {
			console.log(item);
			var view = new ItemView({ model: item });
			this.$("#item-list").append(view.render().el);
		});
	}
});
