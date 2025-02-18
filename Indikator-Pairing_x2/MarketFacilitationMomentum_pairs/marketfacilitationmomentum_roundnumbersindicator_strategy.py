import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationMomentum_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationMomentum und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationMomentum': {
                'class': MarketFacilitationMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationMomentum'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'MarketFacilitationMomentum': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
