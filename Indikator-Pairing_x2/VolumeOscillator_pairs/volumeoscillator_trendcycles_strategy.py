import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
