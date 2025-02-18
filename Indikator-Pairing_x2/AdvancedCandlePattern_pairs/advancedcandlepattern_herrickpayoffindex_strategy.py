import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
