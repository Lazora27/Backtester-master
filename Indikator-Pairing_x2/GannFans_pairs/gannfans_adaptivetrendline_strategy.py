import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
