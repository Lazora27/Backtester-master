import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'ProjectionBands': 1.0
        })
    )
