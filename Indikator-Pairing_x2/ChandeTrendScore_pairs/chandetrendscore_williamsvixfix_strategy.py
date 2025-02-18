import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
