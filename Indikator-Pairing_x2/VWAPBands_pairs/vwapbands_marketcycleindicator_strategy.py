import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
