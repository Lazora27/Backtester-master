import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_HeikenAshiSmoothed_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und HeikenAshiSmoothed
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'HeikenAshiSmoothed': {
                'class': HeikenAshiSmoothed,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiSmoothed'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'HeikenAshiSmoothed': 1.0
        })
    )
