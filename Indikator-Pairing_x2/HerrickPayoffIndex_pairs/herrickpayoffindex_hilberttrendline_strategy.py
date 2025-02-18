import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
