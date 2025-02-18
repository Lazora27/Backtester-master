import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und PriceDelta
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'PriceDelta': 1.0
        })
    )
