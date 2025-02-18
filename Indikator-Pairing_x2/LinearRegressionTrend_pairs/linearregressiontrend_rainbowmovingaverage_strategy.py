import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
