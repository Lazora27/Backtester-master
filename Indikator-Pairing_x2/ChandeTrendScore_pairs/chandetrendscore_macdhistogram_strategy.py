import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'MACDHistogram': 1.0
        })
    )
