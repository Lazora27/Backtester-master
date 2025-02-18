import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'HistoricalATR': 1.0
        })
    )
