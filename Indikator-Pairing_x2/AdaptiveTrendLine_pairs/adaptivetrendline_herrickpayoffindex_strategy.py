import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
