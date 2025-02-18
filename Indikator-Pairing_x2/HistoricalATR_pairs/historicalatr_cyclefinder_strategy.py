import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und CycleFinder
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'CycleFinder': 1.0
        })
    )
