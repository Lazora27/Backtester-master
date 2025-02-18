import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
