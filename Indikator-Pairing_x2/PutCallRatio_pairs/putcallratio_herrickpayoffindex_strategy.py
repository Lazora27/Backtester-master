import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
