import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'SeasonalStrength': 1.0
        })
    )
