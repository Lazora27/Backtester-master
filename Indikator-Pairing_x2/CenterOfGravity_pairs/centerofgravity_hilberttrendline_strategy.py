import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'HilbertTrendline': 1.0
        })
    )
