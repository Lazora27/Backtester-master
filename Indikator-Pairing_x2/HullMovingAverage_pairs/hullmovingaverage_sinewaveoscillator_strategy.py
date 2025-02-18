import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
