import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
