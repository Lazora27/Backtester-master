import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
