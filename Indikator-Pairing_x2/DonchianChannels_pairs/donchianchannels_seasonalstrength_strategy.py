import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'SeasonalStrength': 1.0
        })
    )
