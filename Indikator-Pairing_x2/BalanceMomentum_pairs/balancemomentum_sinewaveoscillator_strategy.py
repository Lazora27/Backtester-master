import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
