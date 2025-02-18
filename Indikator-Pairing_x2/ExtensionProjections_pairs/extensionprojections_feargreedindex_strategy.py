import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'FearGreedIndex': 1.0
        })
    )
