import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
