import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'VolumeOscillator': 1.0
        })
    )
