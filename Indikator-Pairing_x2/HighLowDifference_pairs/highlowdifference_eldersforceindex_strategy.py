import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'EldersForceIndex': 1.0
        })
    )
