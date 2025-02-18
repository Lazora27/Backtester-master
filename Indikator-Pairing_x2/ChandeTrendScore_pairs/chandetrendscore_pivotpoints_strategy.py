import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und PivotPoints
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'PivotPoints': 1.0
        })
    )
