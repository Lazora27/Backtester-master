import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
