import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'SmoothedCycle': 1.0
        })
    )
