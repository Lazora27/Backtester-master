import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'HilbertTrendline': 1.0
        })
    )
