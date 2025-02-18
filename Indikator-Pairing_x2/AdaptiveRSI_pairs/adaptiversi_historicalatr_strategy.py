import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'HistoricalATR': 1.0
        })
    )
