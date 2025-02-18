import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
