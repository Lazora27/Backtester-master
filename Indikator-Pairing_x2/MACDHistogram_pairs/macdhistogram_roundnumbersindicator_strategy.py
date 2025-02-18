import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
