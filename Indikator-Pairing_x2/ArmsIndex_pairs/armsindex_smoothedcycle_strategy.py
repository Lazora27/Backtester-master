import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
