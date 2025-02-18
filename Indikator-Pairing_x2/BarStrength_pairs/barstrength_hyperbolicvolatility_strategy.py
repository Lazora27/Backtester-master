import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
