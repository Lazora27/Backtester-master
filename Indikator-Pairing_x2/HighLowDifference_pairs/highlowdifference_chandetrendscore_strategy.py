import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
