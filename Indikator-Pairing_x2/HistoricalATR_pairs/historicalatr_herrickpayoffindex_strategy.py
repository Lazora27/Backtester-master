import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
