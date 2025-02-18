import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'VolatilityIndex': 1.0
        })
    )
