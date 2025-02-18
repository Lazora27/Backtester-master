import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'AverageLogRange': 1.0
        })
    )
