import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'AverageLogRange': 1.0
        })
    )
