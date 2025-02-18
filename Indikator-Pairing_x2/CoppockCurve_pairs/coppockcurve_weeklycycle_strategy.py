import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'WeeklyCycle': 1.0
        })
    )
