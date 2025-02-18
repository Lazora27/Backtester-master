import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'BuyingPressure': 1.0
        })
    )
