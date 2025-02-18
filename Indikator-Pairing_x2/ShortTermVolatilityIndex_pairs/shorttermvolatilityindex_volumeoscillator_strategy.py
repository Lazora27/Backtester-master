import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ShortTermVolatilityIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ShortTermVolatilityIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'ShortTermVolatilityIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
