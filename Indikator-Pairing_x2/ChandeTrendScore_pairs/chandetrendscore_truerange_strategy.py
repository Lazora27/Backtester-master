import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und TrueRange
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'TrueRange': 1.0
        })
    )
