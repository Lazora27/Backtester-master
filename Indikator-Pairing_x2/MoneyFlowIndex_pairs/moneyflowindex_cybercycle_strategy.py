import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
