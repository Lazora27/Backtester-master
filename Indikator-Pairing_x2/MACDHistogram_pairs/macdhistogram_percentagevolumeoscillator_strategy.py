import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_PercentageVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und PercentageVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'PercentageVolumeOscillator': {
                'class': PercentageVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentageVolumeOscillator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'PercentageVolumeOscillator': 1.0
        })
    )
