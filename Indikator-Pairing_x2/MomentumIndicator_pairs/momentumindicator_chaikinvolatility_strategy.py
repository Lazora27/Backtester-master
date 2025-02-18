import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
