import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und GannSquares
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'GannSquares': 1.0
        })
    )
