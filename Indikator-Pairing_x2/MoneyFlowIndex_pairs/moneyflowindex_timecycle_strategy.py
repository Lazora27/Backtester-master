import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
