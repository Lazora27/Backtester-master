import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
