import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
