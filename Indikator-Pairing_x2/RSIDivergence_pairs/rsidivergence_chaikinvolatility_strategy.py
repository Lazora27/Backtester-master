import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
