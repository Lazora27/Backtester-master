import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
