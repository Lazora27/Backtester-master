import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
