import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_KlingerVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und KlingerVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'KlingerVolumeOscillator': {
                'class': KlingerVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KlingerVolumeOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'KlingerVolumeOscillator': 1.0
        })
    )
