import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
