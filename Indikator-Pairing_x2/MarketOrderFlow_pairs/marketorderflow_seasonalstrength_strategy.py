import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'SeasonalStrength': 1.0
        })
    )
