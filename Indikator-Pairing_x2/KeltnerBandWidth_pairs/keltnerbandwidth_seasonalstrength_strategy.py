import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'SeasonalStrength': 1.0
        })
    )
