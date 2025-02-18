import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'MACDPredictor': 1.0
        })
    )
