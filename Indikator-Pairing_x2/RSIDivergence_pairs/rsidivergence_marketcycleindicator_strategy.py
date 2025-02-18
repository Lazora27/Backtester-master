import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
