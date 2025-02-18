import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_McClellanOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und McClellanOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'McClellanOscillator': 1.0
        })
    )
