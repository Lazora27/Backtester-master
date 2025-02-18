import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MarketBalance
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MarketBalance': 1.0
        })
    )
