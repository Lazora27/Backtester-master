import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
