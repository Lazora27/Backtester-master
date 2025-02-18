import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'VolumeOscillator': 1.0
        })
    )
