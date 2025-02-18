import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'IchimokuCloud': 1.0
        })
    )
