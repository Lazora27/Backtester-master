import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'VolumeOscillator': 1.0
        })
    )
