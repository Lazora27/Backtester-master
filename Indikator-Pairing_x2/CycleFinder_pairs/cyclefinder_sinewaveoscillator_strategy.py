import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
