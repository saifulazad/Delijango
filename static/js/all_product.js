/**
 * Created by Azad on 26-Mar-16.
 */


var Product = React.createClass({


  render: function() {
      return (
          <div className="product-item col-md-4">
          <div className="image-wrapper" >
          <a className="circle sale" href=""><span>Sale</span></a>
          <a href="single_products"><img src="../static/assets/longgrainrice_medium.jpeg"/></a>
        </div>
        <div >
          <p className="title">
            <a href="">
              Austin East Ciders Gold Top
            </a>
          </p>
          <p className="vendor"><a href="" title="">The Deli Co</a></p>
          <p className="price">
            <span className="money" data-currency-cad="$2.99" data-currency-usd="$2.17 USD" data-currency="USD">$2.17 USD</span>
            <em className="marked-down-from">Was <span className="money" data-currency-cad="$4.99" data-currency-usd="$3.61 USD" data-currency="USD">$3.61 USD</span></em>
          </p>
        </div>
      </div>
    );
  }
});

var Products = React.createClass({


    render: function () {
        var my_change = []

        for (var i = 0; i < 14; i++) {
            //var comment = this.props.data[i];
            var p = <Product/>;

            my_change.push(p);
        }

        return(
        <div className="product-grid clearfix">
            <div className="clearfix">
            </div>
            {my_change}
        </div>

    );
    }


});

ReactDOM.render(
  <Products />,
  document.getElementById('products')
);