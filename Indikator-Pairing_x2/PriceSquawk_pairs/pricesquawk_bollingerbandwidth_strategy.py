import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
