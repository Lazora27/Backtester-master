import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
