import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TickActivityIndex': 1.0
        })
    )
