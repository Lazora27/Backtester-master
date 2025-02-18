import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
