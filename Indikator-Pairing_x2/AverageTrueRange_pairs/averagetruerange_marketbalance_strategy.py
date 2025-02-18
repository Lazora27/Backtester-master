import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'MarketBalance': 1.0
        })
    )
