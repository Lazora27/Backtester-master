import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MultiTimeframeTrendFinder_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MultiTimeframeTrendFinder und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'MultiTimeframeTrendFinder': {
                'class': MultiTimeframeTrendFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MultiTimeframeTrendFinder'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'MultiTimeframeTrendFinder': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
