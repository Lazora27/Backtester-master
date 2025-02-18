import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
