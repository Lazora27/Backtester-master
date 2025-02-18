import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
