import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und GannSquares
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'GannSquares': 1.0
        })
    )
