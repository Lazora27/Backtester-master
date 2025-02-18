import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'BuyingPressure': 1.0
        })
    )
