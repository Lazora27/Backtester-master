import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'EaseOfMovement': 1.0
        })
    )
