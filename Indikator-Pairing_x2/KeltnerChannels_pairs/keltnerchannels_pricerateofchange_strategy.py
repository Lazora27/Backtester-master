import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
