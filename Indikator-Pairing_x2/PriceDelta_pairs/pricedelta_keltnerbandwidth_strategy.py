import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
