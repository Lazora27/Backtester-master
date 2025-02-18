import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und MarketBalance
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'MarketBalance': 1.0
        })
    )
