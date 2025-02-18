import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'HilbertTrendline': 1.0
        })
    )
