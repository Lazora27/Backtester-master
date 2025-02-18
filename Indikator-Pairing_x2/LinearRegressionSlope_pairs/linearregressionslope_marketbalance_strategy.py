import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und MarketBalance
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'MarketBalance': 1.0
        })
    )
