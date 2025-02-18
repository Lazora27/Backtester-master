import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'SmoothedCycle': 1.0
        })
    )
