import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
