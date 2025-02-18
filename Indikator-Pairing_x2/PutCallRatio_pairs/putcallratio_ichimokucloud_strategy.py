import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'IchimokuCloud': 1.0
        })
    )
