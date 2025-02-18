import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MACDHistogram': 1.0
        })
    )
