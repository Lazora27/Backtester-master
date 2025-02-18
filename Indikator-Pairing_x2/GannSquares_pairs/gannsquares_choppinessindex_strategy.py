import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
