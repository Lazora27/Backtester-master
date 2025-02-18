import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'SeasonalStrength': 1.0
        })
    )
