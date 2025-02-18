import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
