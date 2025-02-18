import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'AverageTrueRange': 1.0
        })
    )
