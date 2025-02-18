import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'MassIndex': 1.0
        })
    )
