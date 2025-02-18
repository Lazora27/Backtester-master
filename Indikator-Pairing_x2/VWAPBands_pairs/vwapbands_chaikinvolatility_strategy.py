import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
