import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
