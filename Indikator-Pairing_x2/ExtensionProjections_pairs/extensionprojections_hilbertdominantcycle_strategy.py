import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
