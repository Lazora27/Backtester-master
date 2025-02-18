import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
