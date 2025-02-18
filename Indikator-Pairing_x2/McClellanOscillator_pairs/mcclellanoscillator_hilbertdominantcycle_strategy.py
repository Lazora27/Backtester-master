import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
