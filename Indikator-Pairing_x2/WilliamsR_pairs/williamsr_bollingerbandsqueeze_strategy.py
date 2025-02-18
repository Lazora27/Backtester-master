import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
