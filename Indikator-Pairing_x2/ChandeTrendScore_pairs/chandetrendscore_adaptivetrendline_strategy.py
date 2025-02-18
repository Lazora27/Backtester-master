import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
