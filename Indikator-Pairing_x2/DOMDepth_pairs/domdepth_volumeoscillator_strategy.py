import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'VolumeOscillator': 1.0
        })
    )
