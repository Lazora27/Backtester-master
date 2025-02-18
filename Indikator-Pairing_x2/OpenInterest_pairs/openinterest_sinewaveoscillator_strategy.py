import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
