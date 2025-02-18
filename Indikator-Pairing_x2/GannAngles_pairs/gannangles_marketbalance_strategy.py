import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und MarketBalance
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'MarketBalance': 1.0
        })
    )
