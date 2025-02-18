import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
