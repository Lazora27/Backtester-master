import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und MassIndex
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'MassIndex': 1.0
        })
    )
