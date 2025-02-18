import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'HilbertTrendline': 1.0
        })
    )
