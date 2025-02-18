import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'HilbertTrendline': 1.0
        })
    )
