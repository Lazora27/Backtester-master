import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
