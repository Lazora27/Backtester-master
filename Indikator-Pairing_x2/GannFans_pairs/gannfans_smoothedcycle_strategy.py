import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'SmoothedCycle': 1.0
        })
    )
