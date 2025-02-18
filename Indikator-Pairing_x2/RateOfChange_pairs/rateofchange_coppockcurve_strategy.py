import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'CoppockCurve': 1.0
        })
    )
