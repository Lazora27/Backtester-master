import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'LiquidityIndex': 1.0
        })
    )
