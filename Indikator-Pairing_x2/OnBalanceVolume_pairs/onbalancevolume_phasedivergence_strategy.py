import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'PhaseDivergence': 1.0
        })
    )
