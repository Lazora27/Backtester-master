import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'MarketBalance': 1.0
        })
    )
