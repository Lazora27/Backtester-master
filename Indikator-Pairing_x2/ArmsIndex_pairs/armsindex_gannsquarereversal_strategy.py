import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
