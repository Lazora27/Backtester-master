import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
