import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
