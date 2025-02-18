import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
