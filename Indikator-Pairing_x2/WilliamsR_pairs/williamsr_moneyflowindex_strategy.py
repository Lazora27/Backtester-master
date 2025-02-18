import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
