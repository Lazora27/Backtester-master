import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
