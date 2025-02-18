import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'EldersForceIndex': 1.0
        })
    )
