import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'HilbertTrendline': 1.0
        })
    )
