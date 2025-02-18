import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
