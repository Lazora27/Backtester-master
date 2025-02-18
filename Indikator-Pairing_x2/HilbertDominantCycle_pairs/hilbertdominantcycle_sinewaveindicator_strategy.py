import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
