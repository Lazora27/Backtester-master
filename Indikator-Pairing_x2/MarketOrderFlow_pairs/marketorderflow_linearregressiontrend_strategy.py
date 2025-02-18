import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
