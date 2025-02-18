import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentageVolumeOscillator_VerticalHorizontalFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentageVolumeOscillator und VerticalHorizontalFilter
    """
    
    params = (
        ('indicators', {
            'PercentageVolumeOscillator': {
                'class': PercentageVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentageVolumeOscillator'>
            },
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            }
        }),
        ('weights', {
            'PercentageVolumeOscillator': 1.0,
            'VerticalHorizontalFilter': 1.0
        })
    )
