import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
