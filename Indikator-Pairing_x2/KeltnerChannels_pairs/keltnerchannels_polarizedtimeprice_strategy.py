import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
