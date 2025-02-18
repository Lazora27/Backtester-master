import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
