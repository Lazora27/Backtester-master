import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
