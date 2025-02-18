import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
