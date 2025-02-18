import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'HilbertTrendline': 1.0
        })
    )
