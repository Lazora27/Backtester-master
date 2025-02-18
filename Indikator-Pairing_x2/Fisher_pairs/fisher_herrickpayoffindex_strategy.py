import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
