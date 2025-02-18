import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und WilliamsR
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'WilliamsR': 1.0
        })
    )
