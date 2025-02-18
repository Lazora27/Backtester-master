import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
