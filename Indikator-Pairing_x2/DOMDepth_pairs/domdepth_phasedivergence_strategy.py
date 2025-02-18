import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'PhaseDivergence': 1.0
        })
    )
