import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'VolumeOscillator': 1.0
        })
    )
