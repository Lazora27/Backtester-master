import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'WeeklyCycle': 1.0
        })
    )
