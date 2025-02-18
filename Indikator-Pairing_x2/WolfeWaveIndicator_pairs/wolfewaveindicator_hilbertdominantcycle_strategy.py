import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
