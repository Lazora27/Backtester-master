import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
