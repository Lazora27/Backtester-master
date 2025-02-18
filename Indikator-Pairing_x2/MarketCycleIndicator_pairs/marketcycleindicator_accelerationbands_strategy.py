import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'AccelerationBands': 1.0
        })
    )
