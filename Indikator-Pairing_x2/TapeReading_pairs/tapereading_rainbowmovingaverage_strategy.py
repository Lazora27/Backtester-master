import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
