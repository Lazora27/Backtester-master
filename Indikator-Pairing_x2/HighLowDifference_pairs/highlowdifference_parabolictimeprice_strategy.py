import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
