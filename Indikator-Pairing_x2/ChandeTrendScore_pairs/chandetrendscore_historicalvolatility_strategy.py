import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
