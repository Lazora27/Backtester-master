import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
