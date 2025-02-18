import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'BuyingPressure': 1.0
        })
    )
