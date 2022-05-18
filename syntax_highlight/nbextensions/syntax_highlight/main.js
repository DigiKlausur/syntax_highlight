define([
	'base/js/namespace',
	'notebook/js/codecell'
], function(Jupyter, codecell) {

	function register_highlight_modes() {
		let highlight_modes = {
			'text/x-java': {
				'reg': [/^%%syntax\s+java/]
			},
			'text/x-csrc': {
				'reg': [/^%%syntax\s+c/]
			},
			'text/x-sql': {
				'reg': [/^%%syntax\s+sql/]
			},
		};

		for (const [key, value] of Object.entries(highlight_modes)) {
			codecell.CodeCell.options_default.highlight_modes[key] = value;
		}

		Jupyter.notebook.events.one('kernel_ready.Kernel', function() {
			Jupyter.notebook.get_cells().map(function(cell) {
				if (cell.cell_type == 'code') {
					cell.auto_highlight();
				}
			});
		});
	}

	function load_ipython_extension() {
		return Jupyter.notebook.config.loaded.then(register_highlight_modes);
	}

	return {
		load_ipython_extension: load_ipython_extension
	}
})