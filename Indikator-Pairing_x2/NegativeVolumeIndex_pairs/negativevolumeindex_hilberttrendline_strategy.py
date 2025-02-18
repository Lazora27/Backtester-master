import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
