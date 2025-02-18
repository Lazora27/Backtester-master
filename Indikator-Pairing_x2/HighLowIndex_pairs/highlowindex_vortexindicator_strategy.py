import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'VortexIndicator': 1.0
        })
    )
