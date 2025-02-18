import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
