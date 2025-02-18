import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
