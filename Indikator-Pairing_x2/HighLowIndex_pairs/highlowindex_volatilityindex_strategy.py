import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'VolatilityIndex': 1.0
        })
    )
