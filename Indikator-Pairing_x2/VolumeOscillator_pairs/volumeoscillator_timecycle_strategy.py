import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
