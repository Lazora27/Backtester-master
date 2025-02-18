import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'ModifiedATR': 1.0
        })
    )
