import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'IchimokuCloud': 1.0
        })
    )
