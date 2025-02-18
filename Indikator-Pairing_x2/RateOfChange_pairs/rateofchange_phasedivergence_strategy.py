import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'PhaseDivergence': 1.0
        })
    )
