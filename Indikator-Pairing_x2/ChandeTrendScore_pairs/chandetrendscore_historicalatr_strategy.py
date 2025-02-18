import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'HistoricalATR': 1.0
        })
    )
