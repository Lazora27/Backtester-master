import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MassIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MassIndex': 1.0
        })
    )
