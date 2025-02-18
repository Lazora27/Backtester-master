import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
