import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
