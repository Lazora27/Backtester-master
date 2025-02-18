import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'HilbertTrendline': 1.0
        })
    )
