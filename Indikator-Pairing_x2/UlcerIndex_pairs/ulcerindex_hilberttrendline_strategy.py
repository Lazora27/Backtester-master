import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
