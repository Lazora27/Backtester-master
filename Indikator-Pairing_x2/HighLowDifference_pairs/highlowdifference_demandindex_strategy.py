import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und DemandIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'DemandIndex': 1.0
        })
    )
