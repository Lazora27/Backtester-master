import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'TrendExhaustion': 1.0
        })
    )
