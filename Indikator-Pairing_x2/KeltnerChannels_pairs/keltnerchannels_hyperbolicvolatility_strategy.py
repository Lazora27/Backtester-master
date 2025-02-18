import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
