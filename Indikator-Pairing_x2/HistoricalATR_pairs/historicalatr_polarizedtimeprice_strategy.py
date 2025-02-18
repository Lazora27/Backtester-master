import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
