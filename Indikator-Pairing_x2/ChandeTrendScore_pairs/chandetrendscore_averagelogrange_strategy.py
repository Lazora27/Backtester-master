import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'AverageLogRange': 1.0
        })
    )
