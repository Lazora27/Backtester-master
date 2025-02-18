import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'CoppockCurve': 1.0
        })
    )
