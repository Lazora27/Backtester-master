import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'SmoothedCycle': 1.0
        })
    )
