import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'CyberCycle': 1.0
        })
    )
