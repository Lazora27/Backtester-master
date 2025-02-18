import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und MarketBalance
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'MarketBalance': 1.0
        })
    )
