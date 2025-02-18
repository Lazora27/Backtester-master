import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und PriceDelta
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'PriceDelta': 1.0
        })
    )
