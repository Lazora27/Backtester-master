import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
