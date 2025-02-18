import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
