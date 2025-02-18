import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'HilbertTrendline': 1.0
        })
    )
