import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'HilbertTrendline': 1.0
        })
    )
