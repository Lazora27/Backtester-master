import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'HistoricalATR': 1.0
        })
    )
