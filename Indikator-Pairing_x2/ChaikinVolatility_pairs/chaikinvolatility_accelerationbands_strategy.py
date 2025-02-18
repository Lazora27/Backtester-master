import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'AccelerationBands': 1.0
        })
    )
