import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
