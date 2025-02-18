import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'VortexIndicator': 1.0
        })
    )
