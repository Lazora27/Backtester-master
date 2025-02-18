import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
