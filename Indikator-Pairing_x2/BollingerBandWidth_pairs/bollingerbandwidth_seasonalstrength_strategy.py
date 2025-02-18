import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'SeasonalStrength': 1.0
        })
    )
