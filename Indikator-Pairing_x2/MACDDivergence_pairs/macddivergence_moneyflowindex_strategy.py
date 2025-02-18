import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
