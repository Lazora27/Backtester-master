import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
