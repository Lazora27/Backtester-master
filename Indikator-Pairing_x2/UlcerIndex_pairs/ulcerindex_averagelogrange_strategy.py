import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
