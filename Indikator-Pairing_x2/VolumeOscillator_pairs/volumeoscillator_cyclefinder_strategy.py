import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'CycleFinder': 1.0
        })
    )
