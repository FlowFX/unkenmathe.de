$( function() {
    // init Isotope
    var $container = $('#container');
    // init
    $container.isotope({
        // options
        itemSelector: '.item',
        // layoutMode
        masonry: {
            columnWidth: '.item'/2
        }
    });

    // store filter for each group
    var filters = {};

    $('#filters').on( 'click', '.btn', function() {
        var $this = $(this);
        // get group key
        var $buttonGroup = $this.parents('.btn-group');
        var filterGroup = $buttonGroup.attr('data-filter-group');
        // set filter for group
        filters[ filterGroup ] = $this.attr('data-filter');
        // combine filters
        var filterValue = '';
        for ( var prop in filters ) {
            filterValue += filters[ prop ];
        }
        // set filter for Isotope
        $container.isotope({ filter: filterValue });
    });

    // change is-checked class on buttons
    $('.btn-group').each( function( i, buttonGroup ) {
        var $buttonGroup = $( buttonGroup );
        $buttonGroup.on( 'click', 'button', function() {
            $buttonGroup.find('.active').removeClass('active');
            $( this ).addClass('active');
        });
    });

});