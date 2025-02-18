import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'GannSquareReversal': 1.0
        })
    )
