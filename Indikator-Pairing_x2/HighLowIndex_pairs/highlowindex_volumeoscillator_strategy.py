import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
