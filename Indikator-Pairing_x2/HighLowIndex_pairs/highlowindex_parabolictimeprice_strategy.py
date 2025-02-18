import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
