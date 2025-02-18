import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
