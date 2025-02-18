import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'TrendCycles': 1.0
        })
    )
