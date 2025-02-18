import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'PhaseDivergence': 1.0
        })
    )
