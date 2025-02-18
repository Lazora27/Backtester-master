import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'SmoothedCycle': 1.0
        })
    )
