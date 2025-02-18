import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
