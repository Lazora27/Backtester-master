import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
