import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_MESAAdaptiveMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und MESAAdaptiveMovingAverage
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'MESAAdaptiveMovingAverage': {
                'class': MESAAdaptiveMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MESAAdaptiveMovingAverage'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'MESAAdaptiveMovingAverage': 1.0
        })
    )
