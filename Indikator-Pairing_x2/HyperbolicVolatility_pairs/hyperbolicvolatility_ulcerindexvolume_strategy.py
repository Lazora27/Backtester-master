import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
