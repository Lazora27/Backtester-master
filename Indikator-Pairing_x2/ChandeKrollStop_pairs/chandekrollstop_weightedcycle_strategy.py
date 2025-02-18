import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'WeightedCycle': 1.0
        })
    )
