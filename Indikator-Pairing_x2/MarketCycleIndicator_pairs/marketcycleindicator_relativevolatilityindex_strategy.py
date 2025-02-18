import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_RelativeVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und RelativeVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'RelativeVolatilityIndex': {
                'class': RelativeVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVolatilityIndex'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'RelativeVolatilityIndex': 1.0
        })
    )
