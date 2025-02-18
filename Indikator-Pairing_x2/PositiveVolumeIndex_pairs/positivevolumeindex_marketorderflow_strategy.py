import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
