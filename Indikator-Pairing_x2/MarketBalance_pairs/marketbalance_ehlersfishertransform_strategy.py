import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
