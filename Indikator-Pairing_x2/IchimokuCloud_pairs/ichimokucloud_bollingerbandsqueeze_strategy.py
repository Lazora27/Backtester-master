import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
