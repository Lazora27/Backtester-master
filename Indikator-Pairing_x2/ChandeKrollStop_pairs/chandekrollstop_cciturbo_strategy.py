import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'CCITurbo': 1.0
        })
    )
