import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
