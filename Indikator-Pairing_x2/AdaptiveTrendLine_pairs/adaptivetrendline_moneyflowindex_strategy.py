import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
