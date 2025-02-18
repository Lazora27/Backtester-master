import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
