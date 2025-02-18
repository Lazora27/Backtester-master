import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
