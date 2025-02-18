import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
