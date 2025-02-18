import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
