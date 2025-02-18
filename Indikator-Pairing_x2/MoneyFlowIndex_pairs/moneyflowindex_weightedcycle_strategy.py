import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
