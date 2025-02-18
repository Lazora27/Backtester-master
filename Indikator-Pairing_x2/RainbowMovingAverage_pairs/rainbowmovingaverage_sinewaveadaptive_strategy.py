import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
