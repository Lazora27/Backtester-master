import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ModifiedRSI': 1.0
        })
    )
