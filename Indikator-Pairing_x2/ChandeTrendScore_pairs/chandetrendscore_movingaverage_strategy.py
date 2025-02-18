import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und MovingAverage
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'MovingAverage': 1.0
        })
    )
