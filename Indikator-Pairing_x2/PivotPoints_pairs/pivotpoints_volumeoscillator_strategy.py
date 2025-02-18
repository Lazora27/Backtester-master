import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'VolumeOscillator': 1.0
        })
    )
