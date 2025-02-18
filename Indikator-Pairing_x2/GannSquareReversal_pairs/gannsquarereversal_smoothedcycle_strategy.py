import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'SmoothedCycle': 1.0
        })
    )
