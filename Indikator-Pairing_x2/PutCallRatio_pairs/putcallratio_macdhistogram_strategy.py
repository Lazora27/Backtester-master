import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MACDHistogram': 1.0
        })
    )
