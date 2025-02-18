import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
