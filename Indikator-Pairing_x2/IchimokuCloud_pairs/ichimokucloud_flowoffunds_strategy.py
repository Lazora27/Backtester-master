import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'FlowOfFunds': 1.0
        })
    )
