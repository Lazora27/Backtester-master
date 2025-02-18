import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'CoppockCurve': 1.0
        })
    )
