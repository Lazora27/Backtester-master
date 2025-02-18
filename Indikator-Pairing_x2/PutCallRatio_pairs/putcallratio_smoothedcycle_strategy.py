import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'SmoothedCycle': 1.0
        })
    )
