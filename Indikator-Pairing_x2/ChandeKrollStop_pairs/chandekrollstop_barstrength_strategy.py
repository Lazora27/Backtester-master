import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und BarStrength
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'BarStrength': 1.0
        })
    )
