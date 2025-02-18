import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
