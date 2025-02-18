import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PercentageVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PercentageVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PercentageVolumeOscillator': {
                'class': PercentageVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentageVolumeOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PercentageVolumeOscillator': 1.0
        })
    )
