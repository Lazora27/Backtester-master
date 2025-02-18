import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
