import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'PhaseDivergence': 1.0
        })
    )
