import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPTimeCycleIndicator_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPTimeCycleIndicator und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'VWAPTimeCycleIndicator': {
                'class': VWAPTimeCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPTimeCycleIndicator'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'VWAPTimeCycleIndicator': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
