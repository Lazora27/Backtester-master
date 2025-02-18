import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
