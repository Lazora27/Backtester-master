import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'WeightedCycle': 1.0
        })
    )
