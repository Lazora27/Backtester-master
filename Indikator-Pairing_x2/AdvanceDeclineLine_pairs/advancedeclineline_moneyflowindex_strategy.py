import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
