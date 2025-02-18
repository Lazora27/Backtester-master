import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
