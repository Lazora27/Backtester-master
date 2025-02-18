import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
