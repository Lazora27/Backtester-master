import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
