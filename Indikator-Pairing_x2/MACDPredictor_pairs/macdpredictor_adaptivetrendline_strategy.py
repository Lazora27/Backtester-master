import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
