import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentageVolumeOscillator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentageVolumeOscillator und MassIndex
    """
    
    params = (
        ('indicators', {
            'PercentageVolumeOscillator': {
                'class': PercentageVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentageVolumeOscillator'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'PercentageVolumeOscillator': 1.0,
            'MassIndex': 1.0
        })
    )
