import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
