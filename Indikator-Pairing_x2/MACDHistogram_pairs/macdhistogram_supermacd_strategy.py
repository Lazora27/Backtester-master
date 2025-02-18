import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und SuperMACD
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'SuperMACD': 1.0
        })
    )
