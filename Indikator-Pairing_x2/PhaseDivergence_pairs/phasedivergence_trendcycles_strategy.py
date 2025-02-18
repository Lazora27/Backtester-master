import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und TrendCycles
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'TrendCycles': 1.0
        })
    )
