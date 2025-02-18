import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'CycleFinder': 1.0
        })
    )
