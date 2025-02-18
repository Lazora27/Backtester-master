import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
