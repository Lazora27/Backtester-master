import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
