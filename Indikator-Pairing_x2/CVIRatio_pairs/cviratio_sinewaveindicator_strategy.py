import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
