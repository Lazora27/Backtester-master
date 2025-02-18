import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'PhaseDivergence': 1.0
        })
    )
