import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'CoppockCurve': 1.0
        })
    )
