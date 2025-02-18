import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'HilbertTrendline': 1.0
        })
    )
