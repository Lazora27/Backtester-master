import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'VolumeOscillator': 1.0
        })
    )
