import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
