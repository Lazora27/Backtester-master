import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
