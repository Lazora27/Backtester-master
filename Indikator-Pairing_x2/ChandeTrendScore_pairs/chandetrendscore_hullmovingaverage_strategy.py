import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'HullMovingAverage': 1.0
        })
    )
