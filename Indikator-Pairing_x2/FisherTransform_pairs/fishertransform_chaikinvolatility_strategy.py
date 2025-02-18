import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
