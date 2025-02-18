import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'GannSquareReversal': 1.0
        })
    )
