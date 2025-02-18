import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
