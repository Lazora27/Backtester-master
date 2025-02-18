import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
