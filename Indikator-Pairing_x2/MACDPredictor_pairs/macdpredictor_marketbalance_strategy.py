import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MarketBalance': 1.0
        })
    )
