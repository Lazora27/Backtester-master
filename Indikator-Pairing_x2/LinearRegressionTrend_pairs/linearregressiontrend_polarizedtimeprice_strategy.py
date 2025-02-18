import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
