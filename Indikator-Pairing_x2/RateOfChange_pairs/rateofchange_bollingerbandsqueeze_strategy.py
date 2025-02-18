import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
