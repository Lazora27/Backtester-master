import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
