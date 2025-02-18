import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
