import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'BuyingPressure': 1.0
        })
    )
