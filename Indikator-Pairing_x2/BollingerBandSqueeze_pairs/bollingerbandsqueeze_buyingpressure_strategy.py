import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'BuyingPressure': 1.0
        })
    )
