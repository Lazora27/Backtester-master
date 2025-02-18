import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
