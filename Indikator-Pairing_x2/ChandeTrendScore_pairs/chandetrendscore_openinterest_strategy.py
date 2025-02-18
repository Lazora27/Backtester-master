import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'OpenInterest': 1.0
        })
    )
