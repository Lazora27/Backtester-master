import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
