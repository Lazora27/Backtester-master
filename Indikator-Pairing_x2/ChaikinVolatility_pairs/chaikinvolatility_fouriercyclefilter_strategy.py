import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
