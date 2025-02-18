import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'MACDHistogram': 1.0
        })
    )
