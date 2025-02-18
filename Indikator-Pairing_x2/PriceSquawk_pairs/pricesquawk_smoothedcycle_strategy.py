import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'SmoothedCycle': 1.0
        })
    )
