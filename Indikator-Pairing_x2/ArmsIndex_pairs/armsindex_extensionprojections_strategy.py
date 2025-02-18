import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'ExtensionProjections': 1.0
        })
    )
