import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
