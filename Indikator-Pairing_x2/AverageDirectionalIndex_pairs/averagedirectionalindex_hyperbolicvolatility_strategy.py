import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
