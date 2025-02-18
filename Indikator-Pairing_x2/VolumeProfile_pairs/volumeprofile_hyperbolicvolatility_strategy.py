import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
