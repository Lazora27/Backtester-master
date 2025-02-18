import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
