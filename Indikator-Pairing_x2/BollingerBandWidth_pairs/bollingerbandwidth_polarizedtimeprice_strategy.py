import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
