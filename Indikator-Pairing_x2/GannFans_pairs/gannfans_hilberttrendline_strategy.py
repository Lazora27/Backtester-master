import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'HilbertTrendline': 1.0
        })
    )
