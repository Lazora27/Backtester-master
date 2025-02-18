import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
