import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
