import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und SuperTrend
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'SuperTrend': 1.0
        })
    )
