import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'CoppockCurve': 1.0
        })
    )
