import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
