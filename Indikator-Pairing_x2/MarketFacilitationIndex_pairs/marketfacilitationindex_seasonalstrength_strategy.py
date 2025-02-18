import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
