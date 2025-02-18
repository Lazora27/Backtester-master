import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und MarketBalance
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'MarketBalance': 1.0
        })
    )
