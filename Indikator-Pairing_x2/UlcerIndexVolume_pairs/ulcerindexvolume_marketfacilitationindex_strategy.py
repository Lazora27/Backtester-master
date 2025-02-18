import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
