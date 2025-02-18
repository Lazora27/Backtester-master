import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
