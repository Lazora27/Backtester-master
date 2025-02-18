import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
