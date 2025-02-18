import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
