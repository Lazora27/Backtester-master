import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und MarketBalance
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'MarketBalance': 1.0
        })
    )
