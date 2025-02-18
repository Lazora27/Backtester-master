import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
