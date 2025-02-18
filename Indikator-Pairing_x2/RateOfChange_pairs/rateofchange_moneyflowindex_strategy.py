import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
