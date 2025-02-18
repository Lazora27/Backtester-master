import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
