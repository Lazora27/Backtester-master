import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
