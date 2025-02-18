import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'HistoricalATR': 1.0
        })
    )
