import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'HistoricalATR': 1.0
        })
    )
