import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'CCITurbo': 1.0
        })
    )
