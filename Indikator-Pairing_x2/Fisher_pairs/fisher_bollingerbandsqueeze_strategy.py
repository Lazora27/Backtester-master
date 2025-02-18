import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
