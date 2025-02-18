import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'BuyingPressure': 1.0
        })
    )
