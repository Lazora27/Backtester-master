import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'KeltnerChannels': 1.0
        })
    )
