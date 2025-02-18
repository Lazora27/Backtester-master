import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
