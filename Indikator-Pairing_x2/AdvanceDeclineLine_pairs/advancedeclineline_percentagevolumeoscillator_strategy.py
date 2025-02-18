import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_PercentageVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und PercentageVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'PercentageVolumeOscillator': {
                'class': PercentageVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentageVolumeOscillator'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'PercentageVolumeOscillator': 1.0
        })
    )
