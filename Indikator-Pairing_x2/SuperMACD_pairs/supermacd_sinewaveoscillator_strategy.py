import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
