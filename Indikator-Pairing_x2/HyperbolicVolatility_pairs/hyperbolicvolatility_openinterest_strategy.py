import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und OpenInterest
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'OpenInterest': 1.0
        })
    )
