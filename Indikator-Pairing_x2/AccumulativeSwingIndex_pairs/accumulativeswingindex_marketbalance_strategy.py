import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulativeSwingIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulativeSwingIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AccumulativeSwingIndex': {
                'class': AccumulativeSwingIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulativeSwingIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AccumulativeSwingIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
