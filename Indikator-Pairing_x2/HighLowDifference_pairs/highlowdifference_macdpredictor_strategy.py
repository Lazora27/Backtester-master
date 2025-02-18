import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MACDPredictor': 1.0
        })
    )
