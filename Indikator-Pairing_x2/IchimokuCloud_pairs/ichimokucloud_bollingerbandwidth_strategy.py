import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
