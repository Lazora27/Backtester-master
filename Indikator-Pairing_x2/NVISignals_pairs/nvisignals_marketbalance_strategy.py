import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MarketBalance
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MarketBalance': 1.0
        })
    )
