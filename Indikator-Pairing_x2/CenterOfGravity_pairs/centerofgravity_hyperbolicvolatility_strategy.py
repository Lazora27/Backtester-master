import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
