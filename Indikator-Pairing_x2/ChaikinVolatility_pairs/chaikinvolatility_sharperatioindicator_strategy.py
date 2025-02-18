import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
