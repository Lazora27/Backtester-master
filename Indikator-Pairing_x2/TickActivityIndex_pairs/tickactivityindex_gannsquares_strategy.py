import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'GannSquares': 1.0
        })
    )
