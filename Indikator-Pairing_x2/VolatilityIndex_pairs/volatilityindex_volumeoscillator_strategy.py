import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
