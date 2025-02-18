import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'GannSquares': 1.0
        })
    )
