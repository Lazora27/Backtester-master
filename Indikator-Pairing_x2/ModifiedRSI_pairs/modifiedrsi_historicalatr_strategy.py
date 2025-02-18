import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'HistoricalATR': 1.0
        })
    )
