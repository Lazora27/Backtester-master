import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'VolumeOscillator': 1.0
        })
    )
