import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
