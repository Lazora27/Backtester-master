import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'BollingerPercentB': 1.0
        })
    )
