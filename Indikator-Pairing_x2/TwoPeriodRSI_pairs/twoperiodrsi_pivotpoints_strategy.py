import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und PivotPoints
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'PivotPoints': 1.0
        })
    )
