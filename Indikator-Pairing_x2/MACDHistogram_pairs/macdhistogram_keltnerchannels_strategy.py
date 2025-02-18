import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'KeltnerChannels': 1.0
        })
    )
