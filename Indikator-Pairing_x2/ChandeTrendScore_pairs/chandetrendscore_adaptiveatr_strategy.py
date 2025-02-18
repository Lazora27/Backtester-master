import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'AdaptiveATR': 1.0
        })
    )
