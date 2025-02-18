import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'GannSquares': 1.0
        })
    )
