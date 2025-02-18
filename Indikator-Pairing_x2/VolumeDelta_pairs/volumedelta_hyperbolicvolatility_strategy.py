import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
