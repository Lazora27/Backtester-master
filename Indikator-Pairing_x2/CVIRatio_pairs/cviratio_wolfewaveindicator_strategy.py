import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
