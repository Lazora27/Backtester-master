import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'SmoothedCycle': 1.0
        })
    )
