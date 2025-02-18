import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
