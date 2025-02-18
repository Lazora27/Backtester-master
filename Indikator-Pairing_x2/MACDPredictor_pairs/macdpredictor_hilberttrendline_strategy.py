import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'HilbertTrendline': 1.0
        })
    )
