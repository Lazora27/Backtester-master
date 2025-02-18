import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
