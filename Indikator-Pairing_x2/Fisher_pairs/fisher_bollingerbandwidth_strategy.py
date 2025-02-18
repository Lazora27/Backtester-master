import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
