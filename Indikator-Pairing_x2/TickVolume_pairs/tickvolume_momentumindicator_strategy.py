import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MomentumIndicator': 1.0
        })
    )
