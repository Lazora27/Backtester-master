import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
