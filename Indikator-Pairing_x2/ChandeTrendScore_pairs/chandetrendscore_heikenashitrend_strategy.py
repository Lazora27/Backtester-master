import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
