import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SeasonalStrength_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SeasonalStrength und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'SeasonalStrength': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
