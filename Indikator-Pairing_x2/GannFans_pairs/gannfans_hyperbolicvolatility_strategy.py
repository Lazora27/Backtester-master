import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
