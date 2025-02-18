import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und MarketBalance
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'MarketBalance': 1.0
        })
    )
