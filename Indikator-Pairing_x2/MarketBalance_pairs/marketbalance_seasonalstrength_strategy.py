import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'SeasonalStrength': 1.0
        })
    )
