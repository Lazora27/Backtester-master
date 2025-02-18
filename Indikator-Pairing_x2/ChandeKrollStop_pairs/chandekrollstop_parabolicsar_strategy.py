import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'ParabolicSAR': 1.0
        })
    )
