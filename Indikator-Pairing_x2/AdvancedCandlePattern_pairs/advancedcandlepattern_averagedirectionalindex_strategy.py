import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
