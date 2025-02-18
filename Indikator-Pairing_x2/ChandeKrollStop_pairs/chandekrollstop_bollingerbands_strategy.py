import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'BollingerBands': 1.0
        })
    )
