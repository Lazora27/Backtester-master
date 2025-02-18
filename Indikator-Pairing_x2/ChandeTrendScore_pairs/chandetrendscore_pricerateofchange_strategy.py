import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
