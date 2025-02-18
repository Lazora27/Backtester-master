import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'PriceSquawk': 1.0
        })
    )
