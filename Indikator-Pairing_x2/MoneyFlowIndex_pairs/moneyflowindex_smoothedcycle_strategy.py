import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
