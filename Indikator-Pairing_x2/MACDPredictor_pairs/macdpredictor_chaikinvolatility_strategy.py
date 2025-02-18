import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
