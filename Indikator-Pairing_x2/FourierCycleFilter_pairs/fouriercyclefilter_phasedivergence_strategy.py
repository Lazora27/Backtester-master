import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'PhaseDivergence': 1.0
        })
    )
