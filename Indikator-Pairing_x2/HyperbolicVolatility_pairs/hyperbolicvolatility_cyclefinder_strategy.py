import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und CycleFinder
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'CycleFinder': 1.0
        })
    )
