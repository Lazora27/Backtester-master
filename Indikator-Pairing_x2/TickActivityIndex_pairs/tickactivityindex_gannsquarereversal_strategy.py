import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
