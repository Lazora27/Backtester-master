import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
