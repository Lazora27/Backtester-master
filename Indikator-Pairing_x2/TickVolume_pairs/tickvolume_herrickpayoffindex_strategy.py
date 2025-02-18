import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
