import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
