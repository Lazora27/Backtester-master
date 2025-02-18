import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
