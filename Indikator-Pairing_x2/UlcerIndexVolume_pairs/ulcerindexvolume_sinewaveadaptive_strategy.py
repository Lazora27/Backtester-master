import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
