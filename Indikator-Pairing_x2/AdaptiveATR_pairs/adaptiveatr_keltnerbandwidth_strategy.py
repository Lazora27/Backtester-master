import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
