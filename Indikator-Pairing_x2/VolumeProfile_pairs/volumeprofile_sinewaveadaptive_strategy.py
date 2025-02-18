import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
