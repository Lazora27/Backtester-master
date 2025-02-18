import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'PriceSquawk': 1.0
        })
    )
