import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'VolumeOscillator': 1.0
        })
    )
