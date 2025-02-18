import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'SmoothedRSI': 1.0
        })
    )
