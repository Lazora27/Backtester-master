import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
