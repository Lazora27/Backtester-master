import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
