import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
