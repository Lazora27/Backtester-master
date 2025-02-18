import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'SmoothedCycle': 1.0
        })
    )
