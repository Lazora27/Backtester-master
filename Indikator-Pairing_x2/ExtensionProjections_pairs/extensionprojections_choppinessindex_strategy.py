import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
