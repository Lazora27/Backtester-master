import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
