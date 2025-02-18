import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'ProjectionBands': 1.0
        })
    )
